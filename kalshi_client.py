#!/usr/bin/env python3
"""
Kalshi API client — Trade-desk integration.

Usage examples:
  python kalshi_client.py market KXATPMATCH-26APR28MENZVE
  python kalshi_client.py search --series KXATPMATCH
  python kalshi_client.py watch KXATPMATCH-26APR28MENZVE --interval 10
  python kalshi_client.py orderbook KXATPMATCH-26APR28MENZVE
  python kalshi_client.py trades KXATPMATCH-26APR28MENZVE
  python kalshi_client.py portfolio
  python kalshi_client.py fills
  python kalshi_client.py order KXATPMATCH-26APR28MENZVE yes buy 5 57
  python kalshi_client.py cancel <order-uuid>

Auth: set KALSHI_API_KEY_ID and KALSHI_PRIVATE_KEY_PATH env vars,
      or pass --api-key and --key-file flags.
      Add --demo to target the sandbox environment.
"""

import argparse
import base64
import datetime
import json
import os
import sys
import time
from pathlib import Path
from typing import Optional

import requests
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

PROD_BASE = "https://trading-api.kalshi.com/trade-api/v2"
DEMO_BASE = "https://demo-api.kalshi.co/trade-api/v2"

# Path prefix used when building the signing string (must match the API path prefix)
API_PATH_PREFIX = "/trade-api/v2"


# ── Client ────────────────────────────────────────────────────────────────────

class KalshiClient:
    def __init__(self, api_key_id: str, private_key_path: str, demo: bool = False):
        self.api_key_id = api_key_id
        self.base_url = DEMO_BASE if demo else PROD_BASE
        self.session = requests.Session()
        self.session.headers["Content-Type"] = "application/json"

        with open(private_key_path, "rb") as f:
            self.private_key = serialization.load_pem_private_key(f.read(), password=None)

    # ── Auth ──────────────────────────────────────────────────────────────────

    def _auth_headers(self, method: str, path: str) -> dict:
        # Kalshi signs: timestamp_ms + METHOD + /trade-api/v2<path>
        ts = str(int(datetime.datetime.now(datetime.timezone.utc).timestamp() * 1000))
        full_path = API_PATH_PREFIX + path
        message = f"{ts}{method.upper()}{full_path}".encode()
        sig = self.private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.DIGEST_LENGTH,
            ),
            hashes.SHA256(),
        )
        return {
            "KALSHI-ACCESS-KEY": self.api_key_id,
            "KALSHI-ACCESS-TIMESTAMP": ts,
            "KALSHI-ACCESS-SIGNATURE": base64.b64encode(sig).decode(),
        }

    # ── HTTP ──────────────────────────────────────────────────────────────────

    def _request(
        self,
        method: str,
        path: str,
        params: Optional[dict] = None,
        body: Optional[dict] = None,
        auth: bool = False,
    ) -> dict:
        url = self.base_url + path
        headers = self._auth_headers(method, path) if auth else {}

        backoff = 1
        for attempt in range(5):
            try:
                resp = self.session.request(
                    method, url, params=params, json=body, headers=headers, timeout=10
                )
                if resp.status_code == 429:
                    if attempt < 4:
                        time.sleep(backoff)
                        backoff *= 2
                        continue
                resp.raise_for_status()
                return resp.json() if resp.content else {}
            except requests.RequestException as exc:
                if attempt < 4:
                    time.sleep(backoff)
                    backoff *= 2
                else:
                    raise RuntimeError(f"API error: {exc}") from exc
        return {}

    def _get(self, path: str, params: Optional[dict] = None, auth: bool = False) -> dict:
        return self._request("GET", path, params=params, auth=auth)

    def _post(self, path: str, body: Optional[dict] = None) -> dict:
        return self._request("POST", path, body=body, auth=True)

    def _delete(self, path: str) -> dict:
        return self._request("DELETE", path, auth=True)

    # ── Market data (no auth needed) ──────────────────────────────────────────

    def get_market(self, ticker: str) -> dict:
        return self._get(f"/markets/{ticker}").get("market", {})

    def search_markets(
        self,
        series_ticker: Optional[str] = None,
        event_ticker: Optional[str] = None,
        status: str = "open",
        limit: int = 100,
    ) -> list:
        params: dict = {"status": status, "limit": limit}
        if series_ticker:
            params["series_ticker"] = series_ticker
        if event_ticker:
            params["event_ticker"] = event_ticker
        return self._get("/markets", params=params).get("markets", [])

    def get_orderbook(self, ticker: str) -> dict:
        return self._get(f"/markets/{ticker}/orderbook").get("orderbook_fp", {})

    def get_market_trades(self, ticker: str, limit: int = 20) -> list:
        return self._get(f"/markets/{ticker}/trades", params={"limit": limit}).get("trades", [])

    # ── Portfolio (auth required) ─────────────────────────────────────────────

    def get_balance(self) -> dict:
        return self._get("/portfolio/balance", auth=True)

    def get_positions(self, ticker: Optional[str] = None) -> list:
        params = {"ticker": ticker} if ticker else {}
        return self._get("/portfolio/positions", params=params, auth=True).get("market_positions", [])

    def get_fills(self, ticker: Optional[str] = None, limit: int = 50) -> list:
        params: dict = {"limit": limit}
        if ticker:
            params["ticker"] = ticker
        return self._get("/portfolio/fills", params=params, auth=True).get("fills", [])

    def get_orders(self, status: Optional[str] = None) -> list:
        params = {"status": status} if status else {}
        return self._get("/portfolio/orders", params=params, auth=True).get("orders", [])

    def place_order(
        self,
        ticker: str,
        side: str,
        action: str,
        count: int,
        price_cents: int,
        order_type: str = "limit",
    ) -> dict:
        body = {
            "ticker": ticker,
            "side": side,
            "action": action,
            "type": order_type,
            "count": count,
            "yes_price" if side == "yes" else "no_price": price_cents,
            "client_order_id": f"tradedesk-{int(time.time())}",
        }
        return self._post("/portfolio/orders", body=body)

    def cancel_order(self, order_id: str) -> dict:
        return self._delete(f"/portfolio/orders/{order_id}")


# ── Formatting helpers ────────────────────────────────────────────────────────

def _d(dollars_str) -> float:
    try:
        return float(dollars_str) * 100
    except (TypeError, ValueError):
        return 0.0


def cents_to_american(c: float) -> str:
    p = c / 100.0
    if p <= 0 or p >= 1:
        return "N/A"
    if p >= 0.5:
        return f"{-(p / (1 - p)) * 100:+.0f}"
    return f"+{((1 - p) / p) * 100:.0f}"


def _print_market(m: dict):
    yes_bid = _d(m.get("yes_bid_dollars"))
    yes_ask = _d(m.get("yes_ask_dollars"))
    last    = _d(m.get("last_price_dollars"))
    vol24   = float(m.get("volume_24h_fp", 0))
    result  = m.get("result", "")

    print(f"\n{'─'*62}")
    print(f"  Ticker : {m.get('ticker')}")
    if m.get("yes_sub_title"):
        print(f"  YES    : {m['yes_sub_title']}")
    if m.get("no_sub_title"):
        print(f"  NO     : {m['no_sub_title']}")
    print(f"  Status : {m.get('status','').upper()}"
          + (f"  →  Result: {result.upper()}" if result else ""))
    print(f"  Closes : {m.get('close_time','')[:19].replace('T',' ')} UTC")
    print(f"{'─'*62}")
    print(f"  {'':22} {'YES':>10}   {'NO':>10}")
    print(f"  {'Bid':22} {yes_bid:>9.0f}¢   {100-yes_ask:>9.0f}¢")
    print(f"  {'Ask':22} {yes_ask:>9.0f}¢   {100-yes_bid:>9.0f}¢")
    print(f"  {'Last price':22} {last:>9.0f}¢   {100-last:>9.0f}¢")
    print(f"  {'Implied probability':22} {last:>9.1f}%   {100-last:>9.1f}%")
    print(f"  {'American odds equiv':22} {cents_to_american(last):>10}   {cents_to_american(100-last):>10}")
    print(f"  {'24h Volume ($)':22} {vol24:>10,.0f}")
    print(f"{'─'*62}")


def _print_orderbook(ticker: str, ob: dict):
    yes_levels = ob.get("yes_dollars", [])[:8]
    no_levels  = ob.get("no_dollars", [])[:8]
    rows = max(len(yes_levels), len(no_levels))

    print(f"\n  Orderbook — {ticker}")
    print(f"  {'YES BID':>22}   {'NO BID':>22}")
    print(f"  {'Price':>10}  {'Qty ($)':>10}   {'Price':>10}  {'Qty ($)':>10}")
    print(f"  {'─'*10}  {'─'*10}   {'─'*10}  {'─'*10}")
    for i in range(rows):
        y = yes_levels[i] if i < len(yes_levels) else None
        n = no_levels[i]  if i < len(no_levels)  else None
        yp = f"{float(y[0])*100:.0f}¢" if y else "—"
        ys = f"${float(y[1]):,.0f}"    if y else "—"
        np_ = f"{float(n[0])*100:.0f}¢" if n else "—"
        ns  = f"${float(n[1]):,.0f}"    if n else "—"
        print(f"  {yp:>10}  {ys:>10}   {np_:>10}  {ns:>10}")


def _print_balance(data: dict):
    bal  = data.get("balance", 0)
    port = data.get("portfolio_value", 0)
    print(f"\n  Cash balance    : ${bal/100:>10,.2f}")
    print(f"  Portfolio value : ${port/100:>10,.2f}")
    print(f"  Total           : ${(bal+port)/100:>10,.2f}")


def _print_positions(positions: list):
    if not positions:
        print("  No open positions.")
        return
    print(f"\n  {'Ticker':<38} {'Pos':>5} {'Exposure':>10} {'Realized P&L':>14}")
    print(f"  {'─'*38} {'─'*5} {'─'*10} {'─'*14}")
    for p in positions:
        pos = float(p.get("position_fp", 0))
        exp = float(p.get("market_exposure_dollars", 0))
        pnl = float(p.get("realized_pnl_dollars", 0))
        print(f"  {p['ticker']:<38} {pos:>+5.0f} ${exp:>9.2f} ${pnl:>+13.2f}")


def _print_fills(fills: list):
    if not fills:
        print("  No fills found.")
        return
    print(f"\n  {'Time (UTC)':<20} {'Ticker':<38} {'Side':<5} {'Act':<5} {'Ct':>4} {'Price':>6}")
    print(f"  {'─'*20} {'─'*38} {'─'*5} {'─'*5} {'─'*4} {'─'*6}")
    for f in fills:
        ts    = f.get("created_time", "")[:19].replace("T", " ")
        side  = f.get("side", "")
        price = f.get("yes_price") if side == "yes" else f.get("no_price", 0)
        print(
            f"  {ts:<20} {f['ticker']:<38} {side:<5} "
            f"{f.get('action',''):<5} {f.get('count',0):>4} {price:>5}¢"
        )


def _print_trades(ticker: str, trades: list):
    if not trades:
        print("  No trades found.")
        return
    print(f"\n  Recent trades — {ticker}")
    print(f"\n  {'Time (UTC)':<20} {'Taker':>6} {'YES price':>10} {'Size ($)':>10}")
    print(f"  {'─'*20} {'─'*6} {'─'*10} {'─'*10}")
    for t in trades:
        ts    = t.get("created_time", "")[:19].replace("T", " ")
        side  = t.get("taker_side", "")
        price = float(t.get("yes_price_dollars", 0)) * 100
        size  = float(t.get("count_fp", 0))
        print(f"  {ts:<20} {side:>6} {price:>9.0f}¢ {size:>10,.0f}")


# ── Commands ──────────────────────────────────────────────────────────────────

def cmd_market(client: KalshiClient, args):
    m = client.get_market(args.ticker)
    if not m:
        sys.exit(f"Market not found: {args.ticker}")
    _print_market(m)


def cmd_search(client: KalshiClient, args):
    markets = client.search_markets(
        series_ticker=args.series,
        event_ticker=args.event,
        status=args.status,
        limit=args.limit,
    )
    if not markets:
        print("No markets found.")
        return
    print(f"\nFound {len(markets)} market(s):\n")
    print(f"  {'Ticker':<42} {'Last':>6}  {'Status':<10} {'Closes'}")
    print(f"  {'─'*42} {'─'*6}  {'─'*10} {'─'*10}")
    for m in markets:
        last = _d(m.get("last_price_dollars"))
        print(
            f"  {m['ticker']:<42} {last:>5.0f}¢  "
            f"{m.get('status',''):<10} {m.get('close_time','')[:10]}"
        )


def cmd_orderbook(client: KalshiClient, args):
    ob = client.get_orderbook(args.ticker)
    if not ob:
        sys.exit(f"No orderbook data for {args.ticker}")
    _print_orderbook(args.ticker, ob)


def cmd_trades(client: KalshiClient, args):
    trades = client.get_market_trades(args.ticker, limit=args.limit)
    _print_trades(args.ticker, trades)


def cmd_watch(client: KalshiClient, args):
    ticker   = args.ticker
    interval = args.interval
    print(f"Watching {ticker} — refreshing every {interval}s.  Ctrl+C to stop.\n")
    prev_last = None
    try:
        while True:
            m = client.get_market(ticker)
            if not m:
                print("  (no data)")
                time.sleep(interval)
                continue

            ts      = datetime.datetime.now().strftime("%H:%M:%S")
            last    = _d(m.get("last_price_dollars"))
            yes_bid = _d(m.get("yes_bid_dollars"))
            yes_ask = _d(m.get("yes_ask_dollars"))
            status  = m.get("status", "")
            result  = m.get("result", "")

            arrow = ""
            if prev_last is not None:
                arrow = " ▲" if last > prev_last else (" ▼" if last < prev_last else " –")
            prev_last = last

            print(
                f"[{ts}]  YES {yes_bid:.0f}¢ bid / {yes_ask:.0f}¢ ask"
                f"   last {last:.0f}¢{arrow}  ({cents_to_american(last)})"
                f"   [{status.upper()}]"
                + (f"  RESULT: {result.upper()}" if result else "")
            )

            if status in ("closed", "settled"):
                print(f"\n  Market has settled. Result: {result.upper() or 'pending'}")
                break
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopped.")


def cmd_portfolio(client: KalshiClient, args):
    print("\n── Balance ──────────────────────────────────")
    _print_balance(client.get_balance())
    print("\n── Open Positions ───────────────────────────")
    _print_positions(client.get_positions())


def cmd_fills(client: KalshiClient, args):
    fills = client.get_fills(ticker=getattr(args, "ticker", None), limit=args.limit)
    label = f" ({args.ticker})" if getattr(args, "ticker", None) else ""
    print(f"\n── Recent Fills{label} ──────────────────────────")
    _print_fills(fills)


def cmd_order(client: KalshiClient, args):
    cost = args.count * args.price / 100
    print(f"\n  Placing order:")
    print(f"    Ticker : {args.ticker}")
    print(f"    Side   : {args.side.upper()}")
    print(f"    Action : {args.action.upper()}")
    print(f"    Count  : {args.count} contract(s)")
    print(f"    Price  : {args.price}¢  (American: {cents_to_american(args.price)})")
    print(f"    Cost   : ~${cost:.2f}")
    confirm = input("\n  Confirm? [y/N] ").strip().lower()
    if confirm != "y":
        print("  Cancelled.")
        return
    result = client.place_order(
        ticker=args.ticker,
        side=args.side,
        action=args.action,
        count=args.count,
        price_cents=args.price,
    )
    print(f"\n  Order placed:\n{json.dumps(result, indent=4)}")


def cmd_cancel(client: KalshiClient, args):
    result = client.cancel_order(args.order_id)
    print(f"Cancel response:\n{json.dumps(result, indent=2)}")


# ── CLI setup ─────────────────────────────────────────────────────────────────

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Kalshi API client — Trade-desk",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--api-key",  metavar="UUID",  help="Kalshi API Key ID")
    parser.add_argument("--key-file", metavar="PATH",  help="Path to RSA private key PEM")
    parser.add_argument("--demo",     action="store_true", help="Use sandbox environment")

    sub = parser.add_subparsers(dest="cmd", required=True)

    # market
    p = sub.add_parser("market", help="Show market details and current prices")
    p.add_argument("ticker")

    # search
    p = sub.add_parser("search", help="Search markets")
    p.add_argument("--series", metavar="SERIES_TICKER", help="e.g. KXATPMATCH")
    p.add_argument("--event",  metavar="EVENT_TICKER")
    p.add_argument("--status", default="open",
                   choices=["open", "closed", "settled", "unopened"])
    p.add_argument("--limit", type=int, default=50)

    # orderbook
    p = sub.add_parser("orderbook", help="Show top-of-book depth")
    p.add_argument("ticker")

    # trades
    p = sub.add_parser("trades", help="Show recent public trades")
    p.add_argument("ticker")
    p.add_argument("--limit", type=int, default=20)

    # watch
    p = sub.add_parser("watch", help="Stream live prices until settlement")
    p.add_argument("ticker")
    p.add_argument("--interval", type=int, default=10, metavar="SECS")

    # portfolio
    sub.add_parser("portfolio", help="Show balance and open positions")

    # fills
    p = sub.add_parser("fills", help="Show your recent fills")
    p.add_argument("--ticker", help="Filter by market ticker")
    p.add_argument("--limit", type=int, default=50)

    # order
    p = sub.add_parser("order", help="Place a limit order (prompts for confirmation)")
    p.add_argument("ticker")
    p.add_argument("side",   choices=["yes", "no"])
    p.add_argument("action", choices=["buy", "sell"])
    p.add_argument("count",  type=int, help="Number of contracts")
    p.add_argument("price",  type=int, help="Price in cents (1–99)")

    # cancel
    p = sub.add_parser("cancel", help="Cancel an open order by UUID")
    p.add_argument("order_id")

    return parser


def _load_client(args) -> KalshiClient:
    api_key  = args.api_key  or os.environ.get("KALSHI_API_KEY_ID", "")
    key_path = args.key_file or os.environ.get("KALSHI_PRIVATE_KEY_PATH", "kalshi_private_key.pem")

    if not api_key:
        sys.exit("Error: provide --api-key or set KALSHI_API_KEY_ID")
    if not Path(key_path).exists():
        sys.exit(f"Error: private key not found at '{key_path}'")

    return KalshiClient(api_key, key_path, demo=args.demo)


DISPATCH = {
    "market":    cmd_market,
    "search":    cmd_search,
    "orderbook": cmd_orderbook,
    "trades":    cmd_trades,
    "watch":     cmd_watch,
    "portfolio": cmd_portfolio,
    "fills":     cmd_fills,
    "order":     cmd_order,
    "cancel":    cmd_cancel,
}


def main():
    parser = _build_parser()
    args   = parser.parse_args()
    client = _load_client(args)
    DISPATCH[args.cmd](client, args)


if __name__ == "__main__":
    main()
