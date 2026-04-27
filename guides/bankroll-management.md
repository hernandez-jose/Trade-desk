# Bankroll Management

## The Foundation

Bankroll management is the single most important skill in sports betting. A +EV bettor with poor bankroll management goes broke. A disciplined bettor with mediocre picks survives to find better edges.

**Your bankroll is your business capital. Protect it.**

## Unit System

A **unit** is a fixed percentage of your total bankroll. This keeps bet sizes proportional as your bankroll grows or shrinks.

```
Base unit = 1% of starting bankroll
Example: $1,000 bankroll → 1 unit = $10
```

Recalibrate your unit size at the start of each month based on the current bankroll.

## Bet Sizing Scale

| Confidence Level | Unit Size | When to Use |
|-----------------|-----------|-------------|
| Low (edge <3%) | 0.5 units | Marginal spot, situational angle only |
| Standard (edge 3–6%) | 1 unit | Typical +EV wager |
| High (edge 6–10%) | 2 units | Strong model + sharp agreement |
| Max (edge >10%) | 3 units | Rare — requires overwhelming edge |

**Never exceed 3 units on a single bet, regardless of confidence.**

## Kelly Criterion

The Kelly formula determines mathematically optimal bet sizing to maximize long-term growth.

```
Kelly % = (bp − q) / b

Where:
  b = net odds (decimal odds − 1)
  p = estimated win probability
  q = estimated loss probability (1 − p)

Example:
  Bet: -110 odds on a team you estimate wins 55%
  b = (100/110) = 0.909
  p = 0.55
  q = 0.45
  Kelly = (0.909 × 0.55 − 0.45) / 0.909 = (0.500 − 0.45) / 0.909 = 5.5%
```

**Use Half-Kelly in practice** — full Kelly is volatile and assumes perfect probability estimates.  
Half-Kelly on the above = 2.75% of bankroll.

### Kelly Quick Reference

| Win Prob | Odds | Full Kelly | Half Kelly (Use This) |
|----------|------|-----------|----------------------|
| 53%      | -110 | 1.1%      | 0.55% (~0.5 units)   |
| 55%      | -110 | 5.5%      | 2.75% (~1.5 units)   |
| 57%      | -110 | 9.9%      | 4.95% (~2 units)     |
| 60%      | -110 | 18.2%     | 9.1% (cap at 3 units)|
| 55%      | +110 | 14.5%     | 7.25% (cap at 3 units)|

## Daily and Weekly Limits

| Limit | Rule |
|-------|------|
| Daily loss cap | Stop for the day at −5 units |
| Weekly loss cap | Stop new action at −10 units for the week |
| Single-game max | 3 units |
| Parlay exposure | 0.5 units total, regardless of legs |
| Max open bets | 5 simultaneous bets |

## Parlay Policy

Parlays are generally bad EV due to compounding juice. However, they have a place:

- **Allowed**: 2-leg parlays where both legs are independently +EV
- **Allowed**: Round-robin parlays of 3 teams (3 separate 2-team parlays)
- **Avoid**: 3+ leg singles parlays — variance destroys bankroll
- **Never**: Same-game parlays — book controls all correlation

Max parlay exposure per event: **0.5 units**.

## Withdrawal Strategy

- At month-end, withdraw **50% of net profits** above your starting bankroll
- Reinvest the other 50% to grow your unit size
- Keep 2–3 months of base bankroll in reserve outside the betting account
- Never dip into reserve capital

## Tilt Management

**Tilt** is emotional betting — the number one bankroll killer.

Signs you are on tilt:
- Betting on sports or games you haven't researched
- Increasing bet size after a loss to "get it back"
- Feeling angry at a team or a bad beat
- Making 8+ bets in a single day

**Tilt protocol:**
1. Stop betting immediately
2. Log off Klashi
3. Walk away for at least 2 hours
4. Review your `tracking.md` to ground yourself in the long-term record
5. Only return when you can objectively evaluate the next pick

## Variance Reality Check

Even a 55% bettor at -110 will experience significant losing streaks.

| Streak | Probability Over 500 Bets |
|--------|--------------------------|
| 5-game losing streak | ~28% |
| 8-game losing streak | ~6% |
| 10-game losing streak | ~1.5% |

Losing streaks are not evidence of a broken system — they are math. Trust the process and unit sizing.
