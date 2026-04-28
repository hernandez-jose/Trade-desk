# Advanced Betting Strategies

## 1. Sharp Money Identification

### What Makes a Bettor "Sharp"?
Sharp bettors are professional or semi-professional gamblers whose action consistently moves lines. Books respect their opinion and adjust accordingly.

**Signs of sharp action:**
- Line moves in the *opposite* direction of public betting percentage (reverse line movement)
- Steam moves: multiple books move simultaneously within seconds
- Line jumps off a key number (e.g., goes from -3 to -3.5 quickly)
- The move happens in the morning when sharps typically bet (not before prime time when public bets)

**How to use it on Klashi:**
- Open the game in the morning and note the opening line
- Check back 2–3 hours before game time — if the line has moved against the public %, follow the steam
- You won't always get the best number, but you're on the right side of the action

## 2. Closing Line Value (CLV) System

The most reliable metric for evaluating a betting system's true edge is CLV.

**Protocol:**
1. Record your pick and the line you got at time of bet
2. Record the closing line for that game
3. Calculate the difference in implied probability

```
Bet: Celtics -5.5 (you got this line)
Closed: Celtics -7
Line movement: +1.5 points in your favor
CLV: Positive — you beat the market
```

If your picks consistently beat the closing line, your process is sound even during a losing streak.

## 3. Middling

Middling exploits significant line movement to create a position where both bets can win.

```
Example:
  Monday: Bet Chiefs +3 at Klashi
  Thursday: Chiefs move to -3.5 (public piles on Chiefs)
  Bet Raiders +3.5 on the other side

  If Chiefs win by exactly 3: You win the +3 and lose the Raiders bet
  If Chiefs win by 0–2 or 4+: One side wins, one loses (wash)
  If Chiefs win by exactly 3.5: You WIN BOTH (middle hit)
```

Look for middling opportunities when a line crosses key numbers (3, 7 in NFL).

## 4. First-Half and First-Quarter Betting

First-half (1H) and first-quarter (1Q) lines offer underexploited angles:

- **Coaching matchup edges** are magnified in the first half — some coaches are notoriously slow starters or exploit early game plans before halftime adjustments
- **Public bias resets** — the public is betting the full game; 1H books attract sharper, smaller volume
- **Rest-disadvantaged teams** often start slowly and find their rhythm by the second half
- **Home underdog** first-halves are historically profitable — crowd energy peaks early

## 5. Alternate Lines

Klashi (like most books) offers alternate spreads and totals at adjusted odds.

**When to buy points:**
- Buying off 3 in NFL (e.g., -2.5 to -3 or +3 to +3.5) — costs roughly -120 to -125 but is mathematically worth it on key numbers
- Buying a half-point off 7 in NFL — also often worth the juice

**When to sell points:**
- If your model says the game will be a blowout, selling from -6.5 to -4 at better odds increases profit on a likely winner

**Alternate totals:**
- If you love the under but the total seems slightly high, buying 2–3 points down is often worth the juice in low-scoring sports

## 6. Situational Betting

Situational analysis is one of the clearest sources of sustainable edges.

### NFL Situational Spots

| Spot | Angle |
|------|-------|
| Short rest (Thu after Sun) | Road teams on short rest cover less often |
| West Coast team traveling East for 1pm kick | Fade the road team |
| Division underdog at home | Historically beats the spread |
| Team off their bye | Often sharp: well-rested, game-planned |
| Letdown after upset | Emotional hangover — fade the team |

### NBA Situational Spots

| Spot | Angle |
|------|-------|
| 4th game in 5 nights | Offensive output drops, fade the over |
| Back-to-back road game | Home team advantage amplified |
| Team resting stars on b2b | Public still bets them — fade |
| Revenge game vs. last season's eliminator | Overpriced, fade |

### MLB Situational Spots

| Spot | Angle |
|------|-------|
| Ace pitcher facing a cold lineup | Lean under |
| Bullpen game (opener) | Trust over in the late innings |
| West Coast team playing 4pm ET game | Late-sleeping squad, lean home underdog |
| Team playing 7th game in a row | Fatigue spot, lean over if they have the offense |

## 7. Weather Handicapping (NFL & MLB)

### NFL
- **Wind >15 mph**: Reduce total by 1–2 points per every 5 mph above 15
- **Snow/rain**: Expect 10–15% reduction in scoring; bet unders and conservative spreads
- **Cold (<25°F)**: Fade passing offenses, favor rushing teams

### MLB
- **Wind blowing out (>12 mph)**: Consider the over, especially in hitter-friendly parks
- **Wind blowing in**: Lean under, especially in pitcher-friendly parks
- **Humidity/heat**: Slightly inflates offensive output
- Check the wind direction on the field specifically — "blowing out" only matters if it's to center field or the power alleys

## 8. Player Props Strategy

Player props are the most inefficient market on most books.

**Edges:**
- Books set props based on season averages — exploit when a player has a clear matchup edge (e.g., a WR against a corner known to give up yards)
- Injury reports affect team props before player props are adjusted
- **Late scratch**: If a key player is ruled out after props are posted, bet the backup's prop immediately before Klashi adjusts

**Prop correlation parlays:**
- A QB throwing for 300+ yards correlates strongly with the total going over
- These parlay legs at Klashi add expected value if both are independently +EV
- Avoid same-game parlays from the book's parlay builder — the juice is hidden

## 9. Arbitrage (Sure Bets) — Full Math

Arbitrage guarantees profit by covering all outcomes across different books where odds diverge enough that combined implied probability is below 100%.

### Step 1 — Check if an arb exists

```
Arb % = (1/Odds_A_decimal) + (1/Odds_B_decimal)

If Arb % < 1.00 → arb exists
Profit margin = 1 − Arb %

Example:
  Klashi: Team A +110  → decimal 2.10 → 1/2.10 = 0.476
  Book B: Team B −105  → decimal 1.952 → 1/1.952 = 0.512
  Arb % = 0.476 + 0.512 = 0.988 → ARBS (1.2% guaranteed profit)
```

### Step 2 — Calculate stakes (2-outcome arb)

```
Stake on Outcome A = Total Investment × (1/Odds_A_decimal) / Arb %
Stake on Outcome B = Total Investment × (1/Odds_B_decimal) / Arb %

Example with $1,000 total:
  Stake A = $1,000 × (0.476 / 0.988) = $481.78 on Team A at +110
  Stake B = $1,000 × (0.512 / 0.988) = $518.22 on Team B at −105

  If A wins: $481.78 × 2.10 = $1,011.74
  If B wins: $518.22 × 1.952 = $1,011.57
  → ~$11–12 guaranteed profit on $1,000 risked (1.2%)
```

### 3-Outcome Arb (e.g., Soccer with draw)

```
Arb % = (1/Home_decimal) + (1/Draw_decimal) + (1/Away_decimal)

If < 1.00 → arb exists
Each stake = Total × (1/outcome_decimal) / Arb %
```

### Arb Speed Rules
- NFL/NBA major markets: arbs close in 2–5 minutes — act immediately
- Minor markets / props: may stay open 10–20 minutes
- Typical arb returns: 1–5% per opportunity, most under 1.2%
- Use separate accounts; arbing aggressively triggers limits within weeks

### What a True Arb Looks Like

```
NO ARB:
  Klashi: Team A −110 (52.4%) + Book B: Team B −105 (51.2%) = 103.6% → no arb

ARB:
  Klashi: Team A +110 (47.6%) + Book B: Team B −105 (51.2%) = 98.8% → 1.2% arb
```

---

## 10. Hedging — Lock In Profit or Limit Loss

Hedging places a bet on the opposite outcome of an existing position to guarantee a result regardless of the game's outcome.

### Formula: Guaranteed-Profit Hedge

```
Hedge Stake = Original Stake × Original Decimal Odds / Hedge Decimal Odds

OR equivalently:
Hedge Stake = Original Potential Payout / Hedge Decimal Odds

Example:
  Original bet: $100 on Team A at +500 (decimal 6.0) → potential payout $600
  Team A reaches the final. Opponent is now +110 (decimal 2.10)
  Hedge Stake = $600 / 2.10 = $285.71 on the opponent

  If Team A wins: ($600 original win) − ($285.71 hedge stake) = $314.29 profit
  If Opponent wins: ($285.71 × 2.10) − ($100 original loss) = $499.99 − $100 = $399.99 profit
  → Profit guaranteed regardless of outcome
```

### Hedge for Equal Profit on Both Sides

```
To guarantee the same profit on both outcomes:
  Equal Profit Hedge = (Payout_A − Payout_B) / (1 + Decimal_Hedge_Odds)

  Or use: Hedge Stake = Original Payout / (1 + Hedge Decimal Odds)

Simpler: use the hedge formula above and accept slightly different profits per outcome.
```

### When to Hedge

| Scenario | Action |
|----------|--------|
| Futures ticket deep in a tournament | Hedge to lock in guaranteed profit |
| Live game — your team is winning comfortably | Lay the other side to green up |
| Original bet is now a heavy favorite | Hedge if guaranteed profit exceeds expected value of riding it |
| Original bet is losing value rapidly | Partial hedge to limit loss exposure |

### Hedge vs. Ride Decision

```
Ride if: Your team's true probability has NOT changed since you bet
Hedge if: Lock-in profit > Kelly-optimal expected value of letting it ride

Expected value of riding = (True Win Prob × Full Win) − (True Loss Prob × Original Stake)
Compare to guaranteed hedge profit → take the higher number
```

### Partial Hedge
- Hedge only a portion of exposure to reduce risk while preserving some upside
- Partial hedge stake = Full hedge stake × hedge fraction (e.g., 50% hedge)
- Leaves upside on a portion of the original position

---

## 11. Betting Exchange Trading — The Stock Market Method

Betting exchanges (Betfair, BetterEdge, PropSwap) let you act as both bettor and bookmaker — the closest analog to stock market trading in sports.

### Back vs. Lay

| Action | Equivalent | Wins When |
|--------|-----------|-----------|
| Back | Buy long | Selection wins |
| Lay | Short sell | Selection loses or draws |

### Back-to-Lay (Buy Low, Sell High)

```
Strategy: Back a selection at HIGH odds, then lay it at LOWER odds once
odds shorten (price drops = selection is now more favored)

Example:
  Monday: Back Chiefs to win Super Bowl at +800 (8.0 decimal) — $100
  Chiefs win conference. Odds drop to +250 (3.5 decimal)
  Lay Chiefs at 3.5 for stake = ($100 × 8.0) / 3.5 = $228.57

  If Chiefs win: Back wins $800 − Lay loses $228.57 = $571.43 profit
  If Chiefs lose: Back loses $100 + Lay wins = net positive
  → Profit locked regardless — Green Book achieved
```

### Lay-to-Back (Short First, Buy Later)

```
Strategy: Lay a selection at LOW odds (you think odds will drift up)
then Back at HIGHER odds to lock profit

Example:
  Lay Team A to win at 1.5 (−200 equivalent) — liability $50
  Team A has setback, odds drift to 2.5 (+150 equivalent)
  Back Team A at 2.5 to offset the lay position

  Green up: price moved in your favor → profit locked
```

### Greening Up — Equalizing Profit Across All Outcomes

```
Green up stake = (Back stake × Back decimal odds) / Current lay odds

This places an opposing bet that equalizes profit/loss across all outcomes.
Result: Same positive number regardless of who wins.
```

### Exchange vs. Sportsbook

| Feature | Sportsbook (Klashi) | Exchange |
|---------|---------------------|----------|
| Bet against | The house | Other bettors |
| Account limits | Yes (if winning) | No |
| Lay bets | Not available | Yes |
| In-play trading | Limited | Full |
| Commission | Built into odds | 2–5% on net wins |
| Price efficiency | Lower | Higher (sharper) |

### Use exchanges when:
- You want to lock in a futures profit without waiting for the outcome
- You're trading in-play and want to exit a position at better odds
- Your sportsbook account has been limited — exchanges don't limit winners
- You want to lay a team (bet against them) as a pure strategy
