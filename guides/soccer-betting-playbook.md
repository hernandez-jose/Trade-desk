# Soccer Betting Playbook — Complete Operational Guide

> This guide covers every operational layer of soccer betting: how to place bets, when to place them, which markets to prefer, how to size stakes across 3-outcome markets, how to trade in-play, and how to stay disciplined across an entire matchday. Read this before placing any soccer wager on Klashi.

---

## Table of Contents

1. [Step-by-Step Bet Placement Process](#1-step-by-step-bet-placement-process)
2. [Timing of Bets — When to Enter Each Market](#2-timing-of-bets--when-to-enter-each-market)
3. [Line Shopping for Soccer](#3-line-shopping-for-soccer)
4. [Staking and Unit Sizing for Soccer](#4-staking-and-unit-sizing-for-soccer)
5. [Live Betting in Soccer](#5-live-betting-in-soccer)
6. [Asian Handicap Deep Dive](#6-asian-handicap-deep-dive)
7. [Traps to Avoid](#7-traps-to-avoid)
8. [Record Keeping for Long-Term EV Tracking](#8-record-keeping-for-long-term-ev-tracking)
9. [World Cup Specific Considerations](#9-world-cup-specific-considerations)

---

## 1. Step-by-Step Bet Placement Process

### 1.1 Pre-Match Process (Full Workflow)

This is the complete sequence every time you consider a soccer pre-match bet. Do not skip steps.

#### Step 1 — Build Your Own Line (BOYL) Before Looking at the Market

Before opening Klashi, derive your own probability for each of the three outcomes (home win / draw / away win). This prevents anchoring to the book's number.

Inputs to consider:
- **Expected Goals (xG)** from the last 6–8 matches for each team (use FBref, Understat, or SofaScore)
- **Head-to-head record** at this venue (not just H2H overall — home/away matters in soccer)
- **Squad strength delta** — confirmed lineups, suspensions, Europa/UCL fixture within 72 hours
- **Travel and rest** — away team flight distance, days since last match, whether they played midweek
- **Referee** — some referees produce significantly more/fewer yellows, penalties, and added minutes
- **League table pressure** — see the motivation tier table in `sports/soccer/overview.md`
- **Home advantage adjustment** — approximately +8–12% win probability shift toward the home side in top-5 leagues

Document your estimated probabilities. Example format:
```
Home win: 48%
Draw:     27%
Away win: 25%
Total:   100%  (probabilities must sum to 100%)
```

#### Step 2 — Convert Your Probabilities to Implied Odds

For each outcome, convert your true probability to the American odds that would be fair:

```
If true probability = P%:
  When P > 50%: Fair odds = −(P / (1 − P)) × 100
  When P < 50%: Fair odds = ((1 − P) / P) × 100  [positive]

Example:
  Home win at 48% → +((1 − 0.48) / 0.48) × 100 = +108 fair odds
  Draw at 27%     → +((1 − 0.27) / 0.27) × 100 = +270 fair odds
  Away win at 25% → +((1 − 0.25) / 0.25) × 100 = +300 fair odds
```

#### Step 3 — Open Klashi and Compare

Pull up the match on Klashi. Record:
- The posted 1X2 odds (moneyline)
- Asian Handicap lines and juice
- O/U goals lines and juice
- BTTS yes/no juice

Compare each market to your BOYL. A bet exists only where the posted odds are **worse for the book than your fair line** — i.e., where you are being offered better than fair value.

| Your Fair Line | Klashi Posted | Verdict |
|----------------|---------------|---------|
| Home win +108  | Home win -110 | Pass — book pricing implies 52.4%, you said 48%: no edge |
| Home win +108  | Home win +115 | Bet — you're getting 5¢+ better than fair |
| Draw +270      | Draw +280     | Marginal — 3% edge, consider 0.5 unit |
| Draw +270      | Draw +310     | Bet — clear edge on the draw |

**Minimum threshold**: Only bet where your edge is +5¢ in American odds terms or +2% in probability terms after accounting for juice.

#### Step 4 — Check Injury and Lineup Confirmations

For pre-match bets placed 24–48 hours in advance:
- Confirm starting lineups once they drop (typically 60–75 minutes before kickoff in Europe)
- If a key player is ruled out after you place the bet and your model assumed they played, reassess immediately
- For Asian HCP bets: a missing striker changes goal-line markets more than 1X2 markets

Sources to check before placing:
- Official club Twitter/X accounts (lineup confirmation)
- BBC Sport / L'Equipe / Marca for injury updates
- Understat.com for recent xG and lineup history

#### Step 5 — Identify the Best Market for Your Edge

Your edge may be strongest in one market type, not another. Map your edge to the right market:

| Edge Type | Preferred Market |
|-----------|-----------------|
| Team A wins but the margin is uncertain | Asian HCP -0.5 or ML |
| Team A probably wins by 1–2 but not 3+ | Asian HCP -0.5 or -0.75 |
| You expect a tight game with few chances | Under 2.5 goals |
| You think the away team's defense will crack | BTTS Yes |
| Home team heavy favorite but draw is possible | Asian HCP -0.5 (removes draw risk) |
| You think draw is mispriced at the book | 1X2 Draw |

#### Step 6 — Apply Stake Sizing (See Section 4 for Full Framework)

Before submitting, calculate your stake using the soccer-adjusted Kelly method. Do not bet more than 3 units on any single market regardless of confidence.

#### Step 7 — Log the Pick Before Submitting

Open the appropriate picks file (`picks/2026/<month>.md`) and fill in the pick template **before** confirming the bet on Klashi. This prevents rationalization after the fact and enforces pre-commitment to your stated edge.

Required fields to log:
- Match date, teams, kickoff time
- Market selected, odds obtained, unit size
- Your estimated probability vs. implied probability
- Edge amount
- Key reasoning (1–3 lines maximum — if you cannot explain the edge concisely, the edge may not be real)

#### Step 8 — Submit the Bet on Klashi

- Navigate to the match
- Select the correct market and line
- Double-check the odds displayed match what you recorded (lines can shift in the seconds before submission)
- If the odds have moved unfavorably by the time you submit, do not accept the worse number unless your edge still clears the minimum threshold at the new odds
- Submit and capture a screenshot or note the bet ID for verification

---

### 1.2 Live Bet Placement Process

Live betting requires a faster decision framework. See Section 5 for full live-betting strategy. Mechanically:

1. Have the match open in Klashi's live interface before kickoff — do not scramble to navigate during play
2. Identify 2–3 pre-game triggers you will act on if they occur (e.g., "if home team goes down 1-0 in the first 20 minutes, I will check the HCP line")
3. When a trigger event occurs, immediately note the current score, time, and Klashi's offered odds
4. Apply the 60-second rule: if you cannot complete the mental probability check in under 60 seconds, skip the bet — the advantage window in live betting is narrow
5. Live bets are typically smaller (0.5–1 unit max) because the odds move faster and the edge is harder to quantify

---

## 2. Timing of Bets — When to Enter Each Market

Timing is one of the most important and underappreciated edges in soccer betting. Different markets have different liquidity curves, and sharp action enters at predictable intervals.

### 2.1 The Soccer Betting Week — When Lines Open and Move

| Time Before Kickoff | What Happens | Implication |
|---------------------|-------------|-------------|
| 5–7 days out | Opening lines posted (top leagues only) | Lowest liquidity — widest spreads, sharp bettors set tone |
| 72–96 hours | Sharp money enters if they see early value | First steam moves; watch for early line movement |
| 48 hours | Public begins betting; books adjust to balance action | Public sides get worse; sharp sides may still be available |
| 24 hours | Injury and lineup news breaks | Major repricing events; watch for late confirmation |
| 60–75 min before kickoff | Official lineups confirmed | Last chance to act on lineup-based edges |
| 30 min before kickoff | Market most efficient; closing line approaching | If you haven't bet by now, assess whether you still have edge |
| Kickoff | Pre-match markets close or suspend | Switch to live markets |

### 2.2 Market-by-Market Timing Guide

#### Moneyline (1X2)

- **Best time to bet**: 48–72 hours before kickoff
  - Sharpest value exists before the public piles on heavy favorites
  - Heavy public sides (big home favorites) get worse as the week progresses
- **Avoid betting late if**: You were waiting on lineup news — once lineups drop, the 1X2 reprices within minutes
- **Exception**: If you identify an injury announcement that the market hasn't fully digested, the window is 10–20 minutes after the news breaks — act fast

#### Asian Handicap (AH)

- **Best time to bet**: Open market (5–7 days out) for top-league matches where you have a strong model
- **Second best**: 24–48 hours before kickoff after initial injury news
- **Why AH moves differently**: The half-ball and quarter-ball lines allow sharps to express more precise opinions, so the AH market is typically sharper than 1X2 at the same point in time
- **Late-breaking lineup news**: AH lines often lag 1X2 lines in repricing after a major team news announcement by 5–15 minutes — that window is an exploitable edge

#### Over/Under Goals

- **Best time to bet**: 3–5 days before kickoff
  - O/U lines are heavily influenced by weather and team news, but the base xG-driven line is set early
  - Sharp under bettors in particular are active early in the week
- **Weather edge**: If you see a forecast of heavy rain or strong wind 24 hours before a game that wasn't in the model when the line opened, the weather adjustment hasn't fully priced in yet — bet the under before books adjust
- **Avoid**: Betting over totals late when public has been hammering the over all week — the number has already moved unfavorably

#### BTTS (Both Teams to Score)

- **Best time to bet**: 24–48 hours before kickoff, after injury news for attacking players
  - BTTS is heavily dependent on specific attackers; a missing striker is a bigger repricing event here than in AH
- **Live BTTS**: The BTTS No market post-first-goal is valuable — see Section 5
- **Efficiency note**: BTTS is less liquid than O/U or AH in most books, so lines are slower to move and may retain value longer

#### First-Half Markets

- **Best time to bet**: Opening of the market (48–72 hours out)
- First-half lines receive less public volume, so the market is less efficient
- Coaching matchup and press-trap angles play out most clearly in the first half
- Books apply less analytical rigor to first-half totals — this is where modeling edges last longer

### 2.3 How Line Movement Differs in Soccer vs. Other Sports

Soccer lines move differently from NFL or NBA because:

1. **The draw creates three-way markets** — public action is split three ways instead of two, so consensus is slower to form
2. **Liquidity is global, 24/7** — European sharp bettors act during US overnight hours; wake up and check lines each morning before US markets open
3. **Asian books (Pinnacle, SBOBet) set the line** — they are the sharpest operators in soccer; their lines are the benchmark, not Klashi's or US-facing books
4. **Late lineup news reprices more than in NFL** — soccer is 11 vs. 11 with no substitutions to start; one missing top striker changes the game more than an NFL skill-position reserve

**The golden rule on timing**: If you love a side on Tuesday for a Saturday game and you are acting on data and model, bet it Tuesday. Do not wait hoping the line improves — if your reasoning is sound, the line is more likely to move against you as the week progresses and the market catches up to your read.

---

## 3. Line Shopping for Soccer

Line shopping in soccer is more impactful than in any other major sport because:
- Three-way markets create more variability across books on the draw
- Juice structures vary enormously (Pinnacle at ~2% margin vs. retail books at 7–10%)
- Asian Handicap spreads can differ by quarter-ball between books, which significantly changes the bet

### 3.1 The Soccer Line-Setting Hierarchy

Understanding which books lead vs. follow is essential to knowing when you are getting true value.

| Book Type | Role in Soccer Market | Speed |
|-----------|----------------------|-------|
| Asian books (Pinnacle, Betfair Exchange) | Line setters — sharpest | Fastest to reprice |
| European exchanges (Betfair, Smarkets) | Efficient market via peer-to-peer betting | Very fast |
| European retail books (bet365, William Hill, Unibet) | Fast followers, slightly wider margins | Fast |
| US-licensed sportsbooks (DraftKings, FanDuel, Klashi) | Slower followers; soccer is a secondary market | Slow to medium |
| Regional/smaller US books | Slowest to reprice soccer — best for closing line delays | Slowest |

**Practical implication**: Klashi operates as a follower, not a line setter in soccer. When major news breaks, Klashi may lag the Pinnacle or exchange prices by 10–30 minutes. That lag is a window for you. Monitor Pinnacle or Betfair Exchange as your reference line — when Klashi hasn't moved yet, that's your edge window.

### 3.2 How to Compare Lines Across Books for Soccer

#### Step 1 — Establish a Reference Line

Use Pinnacle's Asian Handicap or Betfair Exchange market as your true line. These are sharpest because:
- Pinnacle accepts sharp bettors and doesn't limit winners
- Betfair Exchange sets prices by aggregating thousands of bettors with real money at stake

If Pinnacle shows Manchester City -1 (-106) on the Asian HCP, that is your benchmark.

#### Step 2 — Convert All Odds to Decimal or No-Vig Implied Probability

Comparing American odds across books is confusing when juice differs. Convert to decimal odds for clean comparison:

```
American to Decimal:
  Negative odds: Decimal = (|odds| + 100) / |odds|
    Example: -110 → 210/110 = 1.909
  Positive odds: Decimal = (odds + 100) / 100
    Example: +130 → 230/100 = 2.30
```

Or use no-vig implied probability for each side to strip the margin:

```
No-vig probability = raw implied prob / (sum of raw implied probs for all outcomes)

Example 1X2 with raw implied probs: Home 52%, Draw 28%, Away 25% (sums to 105%)
  No-vig home = 52/105 = 49.5%
  No-vig draw = 28/105 = 26.7%
  No-vig away = 25/105 = 23.8%
```

This removes the vig so you can compare books on a level playing field.

#### Step 3 — Identify Which Book Has the Best Line for Each Outcome

Aggregate your comparison into a table before placing:

| Outcome | Klashi | Pinnacle | Reference Prob | Best Book |
|---------|--------|----------|----------------|-----------|
| Home win | -130 | -125 | 54.2% | Pinnacle |
| Draw | +260 | +255 | 26.7% | Klashi |
| Away win | +320 | +330 | 22.3% | Pinnacle |

#### Step 4 — Always Bet at the Best Available Line

If Klashi is +20 on the draw vs. Pinnacle's +255 offering you +260, bet the draw at Klashi. This is a structural edge that compounds over time.

### 3.3 Which Markets to Line-Shop Most Aggressively

| Market | Line Shopping Priority | Reason |
|--------|----------------------|--------|
| Asian Handicap | Very High | Quarter-ball line differences are common |
| 1X2 Draw | High | Books differ most on draw pricing |
| Over/Under | Medium | Lines tend to converge quickly |
| BTTS | High | Less liquid = more variability across books |
| First-half O/U | Very High | Books apply less rigor here; differences are large |
| Anytime scorer props | Very High | Most books set these independently |

### 3.4 Line Shopping for World Cup Markets

World Cup is covered in detail in Section 9, but for line shopping purposes:
- **Outrights and futures**: Pinnacle and Betfair Exchange are dramatically sharper than US retail books on national team futures; the variance across books is 20–30% on mid-tier nations
- **Match betting**: The WC generates exceptional US book liquidity, so US books (including Klashi) are closer to sharp lines than in regular club play — but still trail Asian books on Asian HCP
- **Group stage lines**: Open 6–8 weeks before the group stage starts; the sharpest bettors build detailed national team models over months; early lines have the most inefficiency before the market catches up
- **Knockout lines**: Open 24–48 hours after qualification is confirmed; the first hours are the window before sharp money floods in

---

## 4. Staking and Unit Sizing for Soccer

Soccer requires different staking logic than binary-outcome sports because outcomes are distributed across three results. Standard two-outcome Kelly does not apply directly to 1X2 markets.

### 4.1 The Three-Outcome Kelly Problem

The Kelly Criterion in its standard form assumes two outcomes (win/loss). In 1X2 soccer markets, you face three outcomes: you can win the bet, lose the bet, or — if you bet a side — also have the "draw" scenario depending on the market.

#### For Asian Handicap (Two-Outcome Market After HCP Applied)

Standard Kelly applies directly because AH reduces the bet to two outcomes (win or lose the handicap):

```
Kelly % = (b × p − q) / b

Where:
  b = net decimal odds − 1
  p = your estimated probability of winning the AH bet
  q = 1 − p

Example:
  Bet: Home team Asian HCP -0.5 at odds -110 (decimal 1.909)
  Your estimated probability home team wins outright: 58%
  Note: AH -0.5 pays if home wins; loses if draw or away win
  
  b = 1.909 − 1 = 0.909
  p = 0.58
  q = 0.42
  Kelly = (0.909 × 0.58 − 0.42) / 0.909
        = (0.527 − 0.42) / 0.909
        = 0.107 / 0.909
        = 11.8% → Half-Kelly = 5.9% → Cap at 3 units
```

Always use Half-Kelly and always cap at 3 units (3% of bankroll using the 1% base unit definition from `guides/bankroll-management.md`).

#### For 1X2 Markets (Three-Outcome Market)

Use the **fractional Kelly for multi-outcome markets**:

```
For a three-outcome market, calculate Kelly for the outcome you are betting as if the other
two outcomes collectively represent the "loss" scenario.

Effective Kelly for betting Home Win in 1X2:
  b = net odds on home win
  p = your estimated probability of home win
  q = 1 − p  (i.e., draw + away win probability combined)
  
  Kelly % = (b × p − q) / b
```

This works because from the perspective of your wager on Home Win, you either win (home wins) or lose (draw or away win) — exactly two outcomes.

**Important**: The 1X2 Kelly will typically produce a smaller stake than AH Kelly because the draw creates more variance in your equity.

#### For Totals and BTTS

Standard two-outcome Kelly applies directly. These are binary markets.

### 4.2 Kelly Quick Reference for Soccer

| Market | Est. Win Prob | Odds | Full Kelly | Half Kelly | Suggested Units |
|--------|---------------|------|-----------|-----------|-----------------|
| AH -0.5 | 55% | -110 | 5.5% | 2.75% | 1.5 units |
| AH -0.5 | 58% | -110 | 11.8% | 5.9% | 3 units (cap) |
| AH -0.5 | 52% | -110 | 0.9% | 0.45% | 0.5 units |
| 1X2 Home | 50% | +110 | 14.5% | 7.25% | 3 units (cap) |
| 1X2 Draw | 30% | +260 | 4.1% | 2.05% | 1 unit |
| O/U 2.5 | 55% | -110 | 5.5% | 2.75% | 1.5 units |
| BTTS Yes | 57% | -105 | 12.4% | 6.2% | 3 units (cap) |

### 4.3 Flat Betting vs. Kelly in Soccer

**Kelly** is theoretically optimal if your probability estimates are accurate. In practice, soccer probability estimation is harder than NFL/NBA because:
- Three outcomes mean a miscalibrated estimate for the draw propagates into both other outcomes
- xG models have higher variance per match in soccer than per-game models in basketball or American football
- Upsets (lower league teams beating top league teams, major international upsets) are more common than models predict

**Recommendation**: Use a hybrid approach.
- **Kelly for your strongest picks** (high-confidence edges above 5%): use Half-Kelly sizing
- **Flat 1 unit for standard picks** (edges of 2–5%): standardize to 1 unit to reduce Kelly overcalculation risk
- **Flat 0.5 unit for marginal picks**: where your edge is real but thin

#### Flat Betting as a Safety Net

Flat betting at 1 unit per play removes the risk of Kelly overcalculation errors. Over a large sample (100+ bets), flat betting at 1 unit with a true edge performs almost as well as Kelly with less variance.

| Strategy | Edge | Over 200 Bets | Variance |
|----------|------|---------------|----------|
| Full Kelly | 5% | +20 units | Very high |
| Half Kelly | 5% | +15 units | High |
| Flat 1 unit | 5% | +14 units | Low |

For soccer, flat 1 unit is the preferred default for new plays. Reserve Kelly sizing for your highest-conviction models where probability estimates are well-calibrated.

### 4.4 Handling Parlays Across a Matchday

Soccer matchdays (Premier League Saturdays, Champions League midweeks) present the temptation to parlay several picks from the same day. Rules:

- **Maximum parlay exposure**: 0.5 units total for all parlay bets on a given matchday
- **Only parlay legs that are independently +EV**: If you would not bet each leg individually at 1 unit, do not include it in a parlay
- **Correlated parlay trap**: In soccer, a parlay of "home win" + "over 2.5" is correlated — the events that cause a home win (strong home attack) are the same events that cause the over. Most books allow this, but it creates negative expected value because the true combined probability is lower than the product of the individual probabilities
- **Best soccer parlays**: Combine picks from different games in different leagues/competitions — no event-to-event correlation

**The matchday parlay protocol**:
1. Identify your solo +EV plays first; allocate units to those
2. After solo plays are capped, use any remaining daily budget (up to 0.5 units) for one 2–3 leg parlay
3. Never add a leg to a parlay that you would not bet individually
4. Never chase a bad day by adding parlay legs in the afternoon after morning picks lost

---

## 5. Live Betting in Soccer

In-play (live) betting is where soccer diverges most sharply from American sports. Because soccer is continuous (no time-outs, play clock, or down-and-distance structure), live lines respond to continuous probability shifts. The edges are real but they evaporate faster than in any other sport.

### 5.1 The Core Live Betting Principle

Your live betting edge comes from one of two situations:
1. **You assessed the game state faster or more accurately than the book** — the line hasn't moved yet to reflect what you see on the pitch
2. **The book overreacted to an event** (goal, red card) and the line has moved too far

You are not playing against a human in live — you are playing against an algorithm. Pinnacle and sharp Asian books have sophisticated live algorithms that update almost instantly. Klashi's live algorithm is less sophisticated. The window where Klashi's line lags reality is your opportunity.

### 5.2 High-Value Live Betting Triggers

These are the events that create the best in-play value. For each, the table shows what the book typically does vs. what the correct probability adjustment is.

#### Red Card

| Scenario | Book's Typical Reaction | Reality | Edge |
|----------|------------------------|---------|------|
| Home team goes to 10 men (1-0 up) | Dramatically increases away win odds, shortens home win odds | 10-man team leads → defensive setup; hold probability is higher than public thinks | Bet home win or home draw |
| Away team goes to 10 men (even) | Shortens home win to near-certainty | 10-man away team often parks the bus; draw probability underestimated | Consider draw or small away HCP |
| Home team goes to 10 men (0-0) | Shortens away win dramatically | 10-man home team has crowd; some of the strongest draws in soccer occur here | Draw often has value |
| Red card in first 20 min | Extreme line reaction | Match is played for 70+ min at 10 v 11; early swing is overdone | Look for the regression to mean |

**Red card rule**: Never react in the first 2 minutes after a red card. Klashi will suspend the market, then reopen it with the algorithmic repricing. Wait for the market to stabilize, then look for overreaction.

#### Opening Goal

| Scenario | Book's Typical Reaction | Correct Analysis | Edge |
|----------|------------------------|-----------------|------|
| Underdog scores first (mins 1–15) | Shortens underdog; lengthens favorite | The goal had ~25–30% probability; now favorite's comeback probability at 75–80 min remaining is still high | Bet favorite ML or AH live |
| Favorite scores first (mins 1–15) | Shortens favorite; lengthens underdog | Probability shift is roughly correct; no obvious edge | Skip |
| Goal in minutes 80–90 | Huge swing on remaining time bets | Small sample of match time remaining; pure gamble territory | Skip — too much variance |
| First goal in a game you expected 2.5 goals | O/U line resets | Whether Over/Under still has value depends on total xG remaining — model this, not the raw line | Requires pre-game model |

**Opening goal rule**: An early goal (minutes 1–25) against the favorite is your best opportunity. The line overreacts to the goal narrative, but match probability at 65+ minutes remaining is still strongly in the favorite's favor. This is your primary live entry trigger.

#### Half-Time Line Shifts

Half-time is a structured break in soccer — Klashi reopens markets for the second half. Half-time offers pre-game-like analysis time (15 minutes) with updated information.

**Half-time betting framework**:

1. Note the score, xG approximation (if you track it), and which team dominated possession/chances
2. Identify the "game state narrative" vs. the actual underlying quality:
   - 0–0 but home team had 4 shots on target vs. 0 → the next goal is likely to the home team
   - 1–0 but the goal was a penalty or own goal, and the away team had more xG → reconsider the away team live
3. Check Klashi's second-half line: if it reflects the score more than the underlying play, you have an edge
4. Apply same unit rules as pre-match (max 1 unit at half-time; 0.5 unit preferred given remaining variance)

**Half-time market opening — sequence**:
- Books suspend live markets at the whistle
- They reopen within 1–3 minutes of the half-time interval
- The first 2–3 minutes of half-time markets are least efficient
- Act early in the half-time window, not late

### 5.3 Markets That Open and Close During Play

| Market | Opens | Suspends | Closes Permanently | Notes |
|--------|-------|----------|-------------------|-------|
| Match Result (1X2) | Pre-kick | Each goal, red card | 90th minute | Most liquid live market |
| Asian HCP | Pre-kick | Each goal, red card | 90th minute | Best live value |
| Next Goal | Pre-kick | Immediately after each goal | 85th minute | High risk, low edge |
| Over/Under Goals | Pre-kick | Each goal | Varies (when mathematically settled) | Closes when not possible |
| BTTS Yes | Pre-kick | First goal or red card | When both teams have scored | Closes when settled |
| BTTS No | Pre-kick | Each goal | When first team not yet scored doesn't matter | Highest value after 60 min, 0-0 |
| Half-time result | Opens at HT whistle | Any half-time goal | HT ends | 15-minute window |
| Corners (total) | Pre-kick | Corner taken | Varies | Book-specific |
| Player cards | Pre-kick | Suspension | 85th minute | Very book-dependent |

**The BTTS No live strategy**: If a match is 0–0 at the 60th minute and you expected 1.5–2 expected goals for each team, the BTTS No price shortens as time runs out. The bet becomes more valuable if one team has a strong defensive record and the match has been tactically cagey. Book for:
- Both teams had under 1.0 xG in the first 60 minutes
- The in-play line on BTTS No is still +EV given the 30 remaining minutes
- Weather or pitch conditions are restricting play

### 5.4 What Not to Do Live

- **Never bet live to "recover" a pre-game bet** — if you bet Over 2.5 and it's 0–0 at 60 min, do not bet Live Next Goal or add live exposure; you are tilting
- **Never bet the Next Goal market for more than 0.25 units** — it is essentially a coin flip with house edge
- **Never bet on a game you are watching emotionally** — neutrality is required; if you are rooting, do not trade
- **Never bet in the last 10 minutes** unless the bet is mathematically near-settled and you have an arbitrage on the exchange

---

## 6. Asian Handicap Deep Dive

Asian Handicap (AH) is the primary betting market for professional soccer bettors worldwide. It eliminates or splits the draw, produces cleaner pricing, carries lower juice at sharp books, and offers more precise expression of probability edges.

### 6.1 All AH Line Types Explained

#### Whole-Ball Lines (Push Scenarios)

Whole-ball Asian handicaps (e.g., -1, -2, +1) create a **push (refund)** if the exact margin equals the handicap.

| Line | Home Team Bet Wins If | Push If | Loses If |
|------|----------------------|---------|---------|
| Home -1 | Home wins by 2+ | Home wins by exactly 1 | Draw or away win |
| Home -2 | Home wins by 3+ | Home wins by exactly 2 | Margin ≤1 or away win |
| Away +1 | Away wins or draws | Away loses by exactly 1 | Away loses by 2+ |
| Away +2 | Away wins, draws, or loses by 1 | Away loses by exactly 2 | Away loses by 3+ |

The push refund makes whole-ball lines equivalent to a "get your money back if it lands exactly on the number" insurance policy. This is different from the American "push" on half-point spreads where the line is designed to avoid a push.

**Practical example**: Home team is -1 Asian HCP at -115. You bet $115.
- Home wins 2-0: Win $100 (bet wins)
- Home wins 1-0: Push — $115 refunded
- Home wins 3-1: Win $100
- Draw 1-1 or 0-0: Lose $115
- Away win: Lose $115

#### Half-Ball Lines (No Push Possible)

Half-ball lines (e.g., -0.5, -1.5, +0.5, +1.5) have no push scenario. Result is always win or lose.

| Line | Home Team Bet Wins If | Loses If |
|------|----------------------|---------|
| Home -0.5 | Home wins by any margin | Draw or away win |
| Home -1.5 | Home wins by 2+ | Win by 1, draw, or away win |
| Away +0.5 | Away wins or draws | Away loses by any margin |
| Away +1.5 | Away wins, draws, or loses by 1 | Away loses by 2+ |

The -0.5 line is the most commonly used line. It is equivalent to the home team moneyline but is typically offered at better juice at Asian-facing books. On Klashi, compare the -0.5 juice to the 1X2 home win price — the AH -0.5 is almost always the better value.

#### Quarter-Ball Lines (Splits)

Quarter-ball lines (e.g., -0.25, -0.75, +0.25, +0.75) are the most sophisticated Asian Handicap lines. Your stake is **split evenly between the adjacent whole-ball and half-ball lines**.

| Line | How It Works |
|------|-------------|
| Home -0.25 | Half stake on Home -0 (draw = push) + Half stake on Home -0.5 |
| Home -0.75 | Half stake on Home -0.5 + Half stake on Home -1 |
| Away +0.25 | Half stake on Away +0 (draw = push) + Half stake on Away +0.5 |
| Away +0.75 | Half stake on Away +0.5 + Half stake on Away +1 |

**Quarter-ball worked example** (Home -0.75, bet $100):

| Result | -0.5 half ($50) | -1 half ($50) | Total |
|--------|-----------------|----------------|-------|
| Home wins by 2+ | Win | Win | Full win |
| Home wins by 1 | Win | Push (refund) | Half win |
| Draw | Lose | Lose | Full loss |
| Away win | Lose | Lose | Full loss |

The quarter-ball creates a "half win / half push" scenario that exists nowhere else in sports betting. It allows you to take a precise position between two adjacent lines.

### 6.2 AH vs. 1X2 — When to Prefer Each

| Situation | Prefer | Reason |
|-----------|--------|--------|
| Clear favorite; draw is plausible | AH -0.5 | Eliminates draw; cleaner pricing |
| Moderate favorite; draw also has value | 1X2 | Can bet two outcomes (home + draw) |
| You want to back a draw explicitly | 1X2 Draw | AH doesn't offer draw |
| You want the underdog to at least not lose badly | AH +1 or +1.5 | Much safer than outright moneyline |
| You expect a high-scoring game and care about margin | AH -1 or -1.5 | Expresses score differential view |
| Book's margin on 1X2 is high | AH | AH at sharp books often has 1–2% margin vs. 5–8% on 1X2 |

**The primary rule**: Unless you are specifically trying to back the draw, Asian Handicap is almost always the superior market due to lower juice and two-outcome clarity.

### 6.3 How AH Affects Breakeven Requirements

| Market | Odds | Break-Even Win % |
|--------|------|-----------------|
| 1X2 Home Win | -130 | 56.5% |
| AH -0.5 Home | -110 | 52.4% |
| AH -0.5 Home | -105 | 51.2% |
| AH -0.75 Home | -115 | 53.5% |
| AH -1 Home | +100 | 50.0% |

A home team at 1X2 -130 (break-even 56.5%) offered at AH -0.5 -110 (break-even 52.4%) represents a 4.1% reduction in break-even threshold for the same underlying outcome (home win). You need to win far fewer bets to be profitable.

### 6.4 AH for In-Play Betting

In-play AH is more efficient than in-play 1X2 because algorithms can cleanly reprice two-outcome markets. However, the live AH line after a goal is often the sharpest priced market on the board — look for the first 30–90 seconds after a goal as the prime window if Klashi's algorithm lags.

---

## 7. Traps to Avoid

### 7.1 The Juice Trap

The juice trap is the single largest source of negative EV for recreational soccer bettors. It occurs when you accept high juice without a corresponding edge.

**Danger zones**:
- 1X2 on clear favorites (teams at -200 to -400) where the juice eats your profit margin completely
- Exotic soccer markets (scorecast, first scorer, exact score) routinely carry 15–25% book margins
- In-play markets on some platforms carry 8–12% margins, double the pre-game margin

**Rule**: If the combined implied probability of all outcomes exceeds 105%, the market has too much juice for a retail bettor to overcome without an exceptional edge. The AH market typically runs at 102–104% at sharp books; use that as your benchmark.

### 7.2 Correlated Parlays in Soccer

Correlated parlays are bets where the outcome of one leg directly influences the probability of another. They look appealing but are mathematically negative EV in most cases.

**Most common soccer correlated parlay traps**:

| Parlay | Correlation | Problem |
|--------|-------------|---------|
| Home win + Over 2.5 goals | Positive | Home win probability is tied to scoring; same events drive both legs |
| BTTS Yes + Over 2.5 goals | Positive | If both teams score, the over often hits — already priced in |
| Home win + Anytime scorer from home team | Positive | Home win requires home team to score; highly correlated |
| Away clean sheet + Away win | Positive | Away win with no away team goals is impossible; trivial correlation |
| Under 2.5 + Home team wins 1-0 | Positive | You're double-betting the same implied scoreline |

**Note**: Same-game parlays on Klashi from the platform's parlay builder should be treated with extreme skepticism. The book knows the correlations and sets the combined juice accordingly. Any "boost" is already factored into the pricing.

**Allowed parlays**: Legs from completely independent matches in different leagues with no shared events. A La Liga pick + a Bundesliga pick + an MLS pick, all independently +EV, is a legitimate parlay.

### 7.3 Chasing After a Red Card Swing

One of the most reliably tilting events in soccer is a red card that swings your pre-game bet from winning to losing. The emotional response is to immediately bet live to compensate.

**The pattern**:
1. You bet Away +0.5 AH at +110 (underdog)
2. Away team goes to 10 men in the 40th minute
3. You are now likely losing pre-game
4. You feel compelled to hedge or add a live bet on the home team
5. You take a poor live price on the home team at inflated odds

**Why this is a trap**: The red card event is already priced into the new live line. You are not betting the post-red card reality — you are buying a line that has already fully repriced the event. If you wouldn't have bet the home team pre-game at the equivalent probability, do not bet them live.

**Protocol**: When a red card negates your pre-game bet, do nothing. Accept the loss and move to the next bet. The live market is not a compensation mechanism.

### 7.4 Overreacting to the Opening Goal

When the underdog scores first, the public and emotional bettor immediately switches to the underdog live. When the favorite scores first, the public assumes the game is over.

Both reactions are usually wrong:
- If you bet the favorite pre-game, their comeback probability with 65+ minutes remaining is still 60–75%
- A 1-0 underdog lead at minute 20 does not mean the underdog is a 50% proposition at that point

**The correct approach**: If you have a live trigger established pre-game (e.g., "if the underdog scores first within 30 minutes, I will bet the favorite ML live at around -140 or better"), follow the trigger and the stake size you planned. Do not improvise a larger bet out of emotion.

### 7.5 Betting on Your National Team (or Favorite Club)

This is addressed in the fundamentals but deserves specific treatment in soccer because it is more prevalent:

- World Cup national team betting is the biggest source of emotional gambling in all of sports
- The public systematically overpays to bet their national team; books know this and shade the line
- Your national team's line is typically 5–10% worse than comparable neutral-country matchups

**Concrete evidence**:
- The United States in World Cup group stage matches regularly opens 10–15% worse than a neutral assessment would price the same matchup (if another pair of nations with equal underlying quality played)
- England and Brazil are consistently overpriced in outright markets; public love inflates their prices to favorites in brackets where they should be modest favorites or co-favorites at best

**Rule**: If you are excited to bet on your team winning, step back 24 hours. If you still see genuine edge on a neutral probability basis, proceed at your minimum unit size (0.5 units). Never bet more on your national team than you would on a neutral contest with identical underlying probabilities.

### 7.6 Betting Mid-Season Fatigue Spots Without Confirmation

In the Premier League, La Liga, and Champions League, the February–April period sees clubs playing twice per week consistently. Managers rotate aggressively and publicly state rotation intentions. However:

- Announced "rotation" lineups often still include 5–7 of the first XI
- Books already price in expected rotation; the line may have already moved on the rotation assumption
- The trap is betting heavily against a rotated "big club" when the market has already priced it in

**Discipline**: Only act on a rotation angle if the confirmed lineup represents a *larger* rotation than the market expected when the line was set. If the line opened at -180 for Manchester City and is now -145, the rotation is already in the price. Look for games where the lineup drops 15 minutes before kickoff and the book hasn't fully adjusted yet.

### 7.7 Long Accumulators (Multi-Leg Soccer Parlays)

The Saturday 10-team Premier League accumulator is the most marketed and worst-EV bet in all of sports betting. Books generate enormous margin from these because:
- Each leg carries 7–10% book margin
- 10 legs compounded at 10% margin each = (0.90)^10 = only 34.9% of fair value returned
- A 10-team parlay requires a near-miraculous run of correct picks and you receive less than half of fair value

**Rule**: Maximum 3 legs in any soccer parlay, and only with independently +EV legs. A 10-team "acca" is a donation to the book.

---

## 8. Record Keeping for Long-Term EV Tracking

Disciplined record keeping is what separates a bettor who thinks they have an edge from one who can prove it. Soccer requires more granular logging than most sports because the three-outcome structure, live trading, and multiple market types all need independent performance tracking.

### 8.1 Required Fields for Every Soccer Bet

Log every bet in `picks/2026/<month>.md` using the standard pick template, plus these soccer-specific additions:

```
## SOCCER | [Date] | [Home Team] vs. [Away Team] | [Competition]

**Pick**: [Market] — [Selection] [Odds]
**Bet Size**: [X] units
**Platform**: Klashi

### Pre-Match Analysis
**Line Origin**: [Where line opened, where it is now at time of bet]
**My estimated probabilities**: Home [X]% / Draw [X]% / Away [X]%
**Implied probabilities (no-vig)**: Home [X]% / Draw [X]% / Away [X]%
**Edge**: +[X]% on [outcome]
**Key inputs**: [xG data source, lineup status, injury notes, motivation tier]
**Competition context**: [League stage, CL/UEL fixture proximity, rotation risk]
**AH or 1X2 rationale**: [Why this market was chosen]

### Stake Calculation
- Market: [AH / 1X2 / O/U / BTTS]
- Estimated win probability: [X]%
- Half-Kelly: [X]% → [X] units
- Actual stake: [X] units (cap reason if applicable)

### Confidence: [Low 0.5u / Standard 1u / High 2u / Max 3u]

### Result
- **Outcome**: [WIN / LOSS / PUSH / HALF-WIN / HALF-LOSS / PENDING]
- **Units**: [+X.X / −X.X]
- **Closing line** (check Pinnacle or Klashi close): [Odds at kickoff]
- **CLV**: [+/−X cents or probability points]
- **xG at end**: [Home xG] — [Away xG] (for calibration)
- **Notes**: [What happened, any lesson, calibration observation]
```

#### The Half-Win and Half-Loss Fields

When you bet quarter-ball Asian Handicap lines, results can be half-wins (full stake back + half profit) or half-losses (half stake lost). Your tracking must record this accurately:

```
Example: Bet 1 unit on Home -0.75 at -110, Home wins 1-0
  -0.5 half: WIN → +0.454 units
  -1 half:   PUSH → 0.00 units
  Total P&L: +0.454 units (half win, not full win)
```

Record this as: **Outcome: HALF-WIN | Units: +0.45**

### 8.2 The Soccer-Specific Metrics to Track

In addition to the standard P&L tracking in `picks/2026/tracking.md`, maintain these soccer-specific performance splits:

| Metric | How to Track | Why It Matters |
|--------|-------------|----------------|
| P&L by Market Type | Separate rows: AH, 1X2, O/U, BTTS | Identifies your strongest market |
| P&L by Competition | PL, UCL, La Liga, WC, etc. | Some competitions may be better modeled |
| P&L by Bet Timing | Early week vs. day-before vs. day-of | Measures timing edge |
| P&L by Live vs. Pre-Game | Separate columns | Live betting may be a drain or a source |
| CLV by Market | Did you beat the close on AH vs. O/U? | Confirms edge in specific markets |
| Draw bet P&L | Track draw bets separately | Draw betting is a distinct skill |
| xG Calibration | Did your pre-match xG estimate match the game? | Calibrates your probability model over time |

### 8.3 Monthly Soccer Performance Review

At the end of each month, before the next month's betting begins, complete this review:

1. **CLV check**: On what percentage of soccer bets did you beat the closing line? Target: >55%
2. **Market review**: Which market (AH / O/U / 1X2 / BTTS) generated the most P&L per bet?
3. **Competition review**: Is your Premier League record better than your La Liga record? Why?
4. **Timing review**: Did early-week bets outperform day-of bets? This indicates your model is ahead of the market
5. **Live review**: If live betting was negative, suspend it for next month and focus on pre-game
6. **Calibration check**: Average your estimated home win probabilities for all bets. Did teams you estimated at 55% win close to 55% of the time? If not, your model needs adjustment

### 8.4 Closing Line Value in Soccer

CLV in soccer requires slight modification from American sports because lines are expressed in three outcomes.

**How to calculate soccer CLV**:

For Asian Handicap bets: Same as other sports — compare the decimal odds you got vs. the closing decimal odds on the same market.

```
You bet: Home -0.5 at -110 (decimal 1.909)
Closed: Home -0.5 at -125 (decimal 1.800)
CLV = 1.909 − 1.800 = +0.109 decimal points → Positive CLV (you got better odds)
```

For 1X2 bets: Track CLV by outcome.

```
You bet: Draw at +280 (decimal 3.80)
Closed: Draw at +260 (decimal 3.60)
CLV = 3.80 − 3.60 = +0.20 decimal points → Positive CLV
```

**Soccer CLV target**: Beating the closing line on 55%+ of bets with an average CLV of +0.05 decimal points or better indicates a genuine edge.

---

## 9. World Cup Specific Considerations

The FIFA World Cup is the highest-profile, highest-liquidity betting event in soccer. It creates unique market dynamics that differ from club play in every dimension — and both the opportunities and the traps are amplified.

### 9.1 How World Cup Liquidity Differs

| Dimension | Club Play (e.g., PL) | World Cup |
|-----------|---------------------|-----------|
| Total global handle per match | $10M–$100M (top matches) | $500M–$2B+ |
| US book liquidity | Secondary market | Primary market |
| Sharp action concentration | Asian books dominate | Global dispersion |
| Line efficiency at kickoff | Very high in PL | Very high in Group Stage |
| Time to closing line efficiency | 5–7 days | 2–3 weeks (early rounds) |
| Public betting volume | Moderate | Extremely high |
| Book margin | 2–5% (sharp books) | 2–4% (competition narrows it) |
| National bias in lines | Minimal | Significant for major nations |

The World Cup is more efficient than most bettors assume — the sharpest professional soccer bettors and syndicates worldwide focus their maximum resources on World Cup markets. Do not assume that because a market is unfamiliar to US bettors, it is inefficient. The sharps are there.

### 9.2 Where World Cup Inefficiency Still Exists

Despite high overall efficiency, specific pockets of inefficiency persist:

#### Outright/Futures Markets (Tournament Winner, Group Winner)

- Open 6–12 months before the tournament; early lines reflect historical reputation and qualification
- Public systematically overvalues: historically dominant nations (Brazil, Germany, Argentina), tournament hosts, nations with the most recognizable individual stars
- Sharp models focus on: current form (last 6 months), squad depth for 7-game tournament, playing style vs. likely bracket opponents, defensive structure
- **Best edge window**: 3–6 months before the tournament when current squad form is known but the public market still reflects historical bias

#### Group Stage (Days 1–15)

- First 3–5 days of group stage have the widest inefficiency — early games for nations with few sharp models tracking them
- Groups containing Asian nations (Japan, South Korea, Australia), CONCACAF nations (Mexico, USA, Canada), African nations (Morocco, Senegal, Nigeria) are less efficiently priced because Asian/European sharp bettors have less data on these leagues
- Group stage underdogs from these regions are statistically undervalued relative to their actual playing quality

**Bracket for 2026 World Cup context**: This is a 48-team tournament for the first time, with a 3-team group stage. The expanded format creates more matches and more pricing events, including a higher share of matches involving nations that are harder to model. This expands the total inefficiency window.

#### Knockout Stage (Rounds of 32, 16, Quarters, Semis, Final)

- As the tournament progresses, lines become more efficient because:
  - More data has accumulated on each team's tournament form
  - The sharp models have had time to update on actual WC performances
  - Handle concentrates on fewer matches, attracting more sharp attention per game
- **Best value**: Early knockout rounds (Round of 32 and 16) for nations that:
  - Overperformed in group stage (public now overprice them)
  - Underperformed in group stage but on underlying xG showed they were better than results (public now underprice them)

### 9.3 National Team Bias — The Systematic Edge

The World Cup creates the single largest national bias event in all of sports. Quantified:

| Nation | Typical Public Betting Bias | Effect on Line |
|--------|-----------------------------|----------------|
| Brazil | Heavy public backing regardless of squad | Shortened by 5–15% vs. neutral assessment |
| England | Strong public backing, especially during tournament | Shortened by 8–12% vs. neutral |
| Argentina | Star-player driven public backing (Messi era ending) | Varies by squad; moderate bias |
| USA | Home nation bias; USA betting market is enormous | USA typically 10–20% overpriced in WC markets |
| Germany | Historical prestige; some bias declining post-2018 | Moderate; watch for line movement direction |
| Morocco | Rising underdog narrative; public fading them | Typically fair-priced or underpriced |
| Japan | Underestimated by Western sharp models | Often underpriced in group stage vs. European competition |

**Fading the public in World Cup Group Stage is historically one of the strongest system edges in soccer betting.** Nations with large diaspora populations in betting markets (Brazil, Argentina, England, Mexico for US books) are consistently overpriced. Their opposition is consistently underpriced.

### 9.4 Line Shopping Strategy Specific to World Cup

The World Cup creates a unique line-shopping opportunity because:
- US books (including Klashi) compete heavily for the large US soccer audience
- Books offer enhanced odds and promotions; compare "boosted" prices vs. actual sharp line
- Asian books (Pinnacle) are the sharpest reference — wider point spread between Pinnacle and US retail books than in regular club play

**World Cup line-shopping protocol**:

1. Open Pinnacle (or Betfair Exchange) as your reference line for every WC match
2. Compare Klashi's line to Pinnacle 48–72 hours before each game
3. If Klashi offers +15 or more cents (American odds) vs. Pinnacle on any outcome, that's a real edge
4. For group stage outrights (Win Group, Advance from Group), compare across 5+ books — variance is largest here
5. Check for promotional "odds boosts" at Klashi around WC matches — if a boost still represents +EV after accounting for the natural line, take it

### 9.5 Asian Handicap in World Cup Matches

World Cup matches are heavily bet on Asian Handicap in Asia, making the AH market exceptionally efficient — possibly more efficient than in club play. The reason: Chinese, Japanese, Korean, and Southeast Asian bettors pour enormous volume into every WC match through Asian-facing books.

Implications:
- The WC AH line is almost certainly the sharpest line you will encounter in soccer
- For major WC matches (Group Stage games involving contenders, all knockout rounds), do not assume you can beat the WC AH market without exceptional information
- If the WC AH is efficient, look instead to the O/U total or the 1X2 draw where public markets may still misprice

### 9.6 Tactical Considerations Unique to World Cup

| Factor | How It Differs from Club Play | Betting Impact |
|--------|-----------------------------|----------------|
| No club-loyalty rotation | NT managers cannot rotate for rest in a WC | Fatigue is real in 7-game run; fade tired teams in semifinals |
| Tactical familiarity | Opponents can scout each other for weeks | More low-scoring tactical battles; lean under in knockout rounds |
| Referee neutrality | Referees are internationally neutral (not domestic) | Fewer home-country refereeing bias effects |
| Altitude and heat | Host nation conditions affect European teams | Research host cities for WC 2026 (USA, Canada, Mexico) — stadiums span sea level to high altitude |
| Squad depth over star power | 7 games in ~30 days requires deep squads | Nations with 15+ quality players outperform pre-tournament star ratings |
| Group stage three-way format (2026) | Each group is 3 teams, 2 qualify | Third-place teams advance; tactical incentives differ significantly |

**2026 World Cup altitude note**: Mexico City's Estadio Azteca is at 2,240m (7,350 ft). European and South American teams not acclimatized to altitude perform measurably worse there, especially in the first 30 minutes. Any team playing at Azteca or other high-altitude venues faces a quantifiable disadvantage worth 0.25–0.5 goals in total expected goals. The market may not fully price this when groups are first drawn.

### 9.7 World Cup Bet Sizing Rules

The elevated handle, emotional environment, and national bias make the World Cup a particularly dangerous context for bet-sizing discipline. Specific rules:

- Apply the same unit system as all other bets (base 1 unit)
- **Do not increase unit sizes** for the World Cup on the basis that "this one matters more"
- **Reduce units by 50%** on any match involving a team you have an emotional rooting interest in
- **Maximum total exposure per World Cup match day**: 5 units across all bets (including parlays) — same daily cap as any other day
- **World Cup parlays**: Maximum 2-leg parlay only; 3-team WC parlays carry severe public bias compounding

---

## Summary Reference — Soccer Betting Quick Card

### Pre-Match Checklist

- [ ] Built own probability estimate before opening Klashi
- [ ] Checked confirmed lineups (if available — 60–75 min before kickoff)
- [ ] Verified no major injuries affecting my probability model
- [ ] Compared Klashi to at least one other book (Pinnacle or Betfair Exchange)
- [ ] Identified the best market for my edge (AH vs. 1X2 vs. O/U vs. BTTS)
- [ ] Calculated Half-Kelly stake and applied unit cap
- [ ] Logged the pick in picks/2026 BEFORE submitting
- [ ] Confirmed the Klashi line on screen matches what I calculated before confirming

### Live Betting Checklist

- [ ] Pre-game triggers defined (which events will I act on?)
- [ ] Unit cap for live bets: max 1 unit per live market
- [ ] Not reacting to a red card or goal within the first 90 seconds
- [ ] Not using live bets to compensate for a pre-game bet that is now losing
- [ ] Have a defined exit: at what game state do I no longer want live exposure?

### Red Flags — Stop and Reconsider

- The line has moved against me by more than 10¢ since I identified the edge
- Lineup news drops that changes my model by more than 5% in any outcome
- I am emotionally excited about this bet (not analytically confident)
- The juice exceeds -130 on a soccer market with no clear structural edge
- I am about to bet a 3-leg parlay with correlated legs
- I am down 3+ units today and considering adding more exposure

### Key Reference Odds for Soccer

| Implied Probability | American Odds | Use Case |
|--------------------|---------------|----------|
| 50.0% | +100 (even) | Coin flip; minimal edge |
| 52.4% | -110 | Break-even for standard -110 bets |
| 55.0% | -122 | Moderate confidence play |
| 60.0% | -150 | Strong favorite; check AH instead |
| 65.0% | -186 | Very heavy favorite; AH -0.5 is better |
| 40.0% | +150 | Underdog with genuine edge |
| 33.3% | +200 | Value underdog; confirm with CLV |
| 27.0% | +270 | Draw bet target price range |
| 25.0% | +300 | Away win underdog |

---

> For related materials, see:
> - `guides/bankroll-management.md` — unit system and Kelly framework
> - `guides/value-betting.md` — BOYL methodology and CLV tracking
> - `sports/soccer/overview.md` — league-by-league efficiency and key soccer angles
> - `picks/template.md` — pick documentation template
> - `picks/2026/tracking.md` — master P&L log
