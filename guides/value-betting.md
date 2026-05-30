# Value Betting — Finding +EV Wagers

## What Is Expected Value (EV)?

Expected value measures what you expect to win (or lose) per dollar wagered over the long run.

```
EV = (Win Probability × Profit) − (Loss Probability × Stake)

Example: You estimate a team has a 55% chance of winning at -110 odds
  Win: 55% × $100 = $55.00
  Loss: 45% × $110 = $49.50
  EV = $55.00 − $49.50 = +$5.50 per $110 wagered → +EV bet
```

Any bet with positive EV is worth taking if properly sized.

## Step-by-Step Value Identification

### Step 1: Build Your Own Line (BOYL)
Before looking at Klashi's line, estimate the true probability of each outcome.

Key inputs:
- Power ratings (your own or from a trusted model)
- Home/away adjustment (typically 2.5–3 points in NFL, 3–4 points in NBA)
- Injury adjustment
- Rest/fatigue adjustment
- Weather adjustment (outdoor sports)

### Step 2: Convert to Implied Odds
Take your estimated win probability and convert to what line it implies.

```
If you estimate Team A wins 56%:
  Implied American Odds = −(56/44 × 100) = −127
  So if Klashi posts Team A at -110, you have value (you're getting +17 cents)
```

### Step 3: Compare to the Posted Line
If your line is significantly better than what Klashi offers, you have an edge.

| Your Line | Klashi Line | Edge |
|-----------|-------------|------|
| -127      | -110        | +17¢ (bet it) |
| -115      | -110        | +5¢  (marginal, small bet) |
| -110      | -115        | −5¢  (pass) |
| -110      | -125        | −15¢ (avoid) |

**Rule of thumb:** Only bet if your edge is at least +5¢ (5 cents better than break-even).

## Value Sources

### Public Bias
The general public overvalues:
- Marquee teams (Cowboys, Lakers, Yankees)
- Teams coming off a big win
- Home favorites on national TV
- High-scoring offenses (inflates totals)
- Hyped, undefeated, or "feared" fighters (MMA)
- KO artists and exciting finishers over methodical grinders (MMA)

And **undervalues**:
- Disliked or controversial fighters — public emotionally suppresses bets on them, inflating their underdog price beyond true probability
- Decision grinders and high-cardio fighters in long fights
- Large underdogs in general (favorite–longshot bias)

Fading the public in these spots provides structural +EV over time.

**Critical rule for MMA**: A fighter's personality, public statements, or "villain" status has zero effect on their true win probability — but it does suppress public betting on them, making their price artificially long. A disliked underdog against a hyped favorite is one of the most reliably mispriced situations in combat sports betting.

When multiple biases stack on the same fight (hype bias + style bias + villain bias all pointing the same direction), the edge on the unpopular side can be 20–30 percentage points above implied probability. This is when the model's output must be followed, even when the narrative says otherwise.

> See `analysis/crowd-bias.md` for the full framework including bias checklist and the Chimaev/Strickland case study.

### Injury Market Inefficiency
When a key player is scratched late, lines don't always move enough.  
Example: An NBA starter averaging 28 PPG sits out. If the line moves only 3 points but his replacement averages 12 PPG, the line is probably still wrong.

### Schedule Spots
Teams play better or worse depending on schedule context. Look for:
- **Letdown spot**: Big emotional win followed by a lesser opponent
- **Look-ahead spot**: Inferior opponent sandwiched between two big games
- **Revenge spot**: Team faces an opponent that beat them badly earlier
- **Short rest**: Teams playing on 0–1 day rest are statistically disadvantaged

### Line Shopping Edge
Getting +3 instead of +2.5 on a spread is a massive long-term edge.  
Always compare Klashi's number to other books. Half-points on key numbers (3, 7 in NFL; 4, 5 in NBA) are worth significant money.

## Key Numbers in Each Sport

### NFL
- **3 and 7** are the most important (field goal and touchdown)
- Paying for -2.5 to -3 or -6.5 to -7 is usually worth it
- Getting +3.5 instead of +3 saves you in a meaningful % of games

### NBA
- Key numbers are less fixed due to higher scoring, but **4, 5, and 6** matter
- Focus more on total efficiency metrics than raw scoring

### MLB
- Run-line (+1.5 / -1.5) creates extra value on dogs — favorites go to extras
- Totals are heavily pitcher-dependent; always confirm confirmed starters

### Soccer
- 0 and 1 are the most important (draw and one-goal wins)
- Asian handicaps eliminate the draw outcome and offer cleaner value
- Double chance (home/draw) reduces risk on underdog markets

## Closing Line Value (CLV)

The single best measure of long-term success is **closing line value** — did your line beat the closing number?

```
You bet: Team A -3 (opened at -3)
Line closes: Team A -5
Your CLV: +2 points → You got the better number
```

Consistently beating the closing line by even 0.5–1 point is the hallmark of a winning bettor. The market is sharpest at close. If you consistently beat it, your picks have long-run value regardless of short-term results.

## Value Bet Checklist

Before placing any bet, confirm:
- [ ] I have estimated a true win probability independently
- [ ] My estimated line is at least +5¢ better than Klashi's posted line
- [ ] I've checked for major injuries or lineup news
- [ ] I've accounted for home/away and rest factors
- [ ] My bet size follows Kelly sizing from `guides/bankroll-management.md`
- [ ] I've logged this pick in the appropriate picks file before the game
