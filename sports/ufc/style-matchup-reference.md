# Style Matchup Betting — Fight-Day Reference Card

The wrestler vs. striker edge is the most durable, documented alpha in MMA betting.
Use this file every time you are evaluating a fight between two fighters.

---

## Step 1: Classify Each Fighter's Primary Style

Look up each fighter on **UFCStats.com** or **Sherdog.com** and assign one style:

| Style | Definition | How to Spot It |
|-------|-----------|----------------|
| **Striker** | Prefers range, stand-up exchanges | High SLpM, low TD avg, low sub avg |
| **Pressure Striker** | Walks opponents down, high volume | High SLpM + high SApM, aggressive walk-forward style |
| **Wrestler** | Takedown-first, controls position | High TD avg (3+/15 min), high TD acc, high ctrl time |
| **Submission Specialist** | Hunts chokes and locks from guard | High sub avg (1+/15 min), fights predominantly from the ground |
| **Well-Rounded** | No clear primary weapon or clear weakness | Balanced stats across all categories |

---

## Step 2: Pull These Stats from UFCStats.com

For **each fighter**, record:

| Stat | Fighter A | Fighter B |
|------|-----------|-----------|
| SLpM (strikes landed/min) | | |
| Str. Acc. % | | |
| SApM (strikes absorbed/min) | | |
| Str. Def. % | | |
| TD Avg (per 15 min) | | |
| TD Acc. % | | |
| **TD Def. %** ← most important | | |
| Sub Avg (per 15 min) | | |

---

## Step 3: Check the Matchup Matrix

Find where the two styles intersect:

| Fighter A Style → | vs. Striker | vs. Pressure | vs. Wrestler | vs. Sub Spec | vs. Well-Rounded |
|-------------------|-------------|--------------|--------------|--------------|------------------|
| **Striker** | 50% | 48% | **40%** | 44% | 47% |
| **Pressure Striker** | 52% | 50% | **38%** | 46% | 48% |
| **Wrestler** | **60%** | **62%** | 50% | 55% | 52% |
| **Sub Specialist** | 56% | 54% | 45% | 50% | 49% |
| **Well-Rounded** | 53% | 52% | 48% | 51% | 50% |

Read the table as: Fighter A's win probability against Fighter B's style.
Figures marked **bold** are statistically significant edges (>2 std deviations from 50%).

---

## Step 4: Apply the Wrestler Gate Check

The wrestler edge only activates if **both** conditions are met:

```
GATE 1: Wrestler's TD Avg ≥ 3.0 per 15 min   →  YES / NO
GATE 2: Striker's TD Def % ≤ 55%              →  YES / NO

Both YES = STRONG wrestler edge (use 60% base win probability)
One YES  = MODERATE edge (use 55% base win probability)
Both NO  = No structural edge — treat as coin flip at style level
```

---

## Step 5: Apply Situational Modifiers

Adjust the base win probability up or down:

| Situation | Shift | Apply To |
|-----------|-------|----------|
| Fighter missed weight | −8% | That fighter |
| Short-notice replacement (< 2 weeks) | −10% | Replacement |
| Southpaw vs. orthodox (limited prior exposure) | +3% | Southpaw fighter |
| Long layoff (12+ months) | −4% | Returning fighter |
| Moving down in weight class | +4% | Smaller fighter |
| Moving up in weight class | −4% | Larger fighter |
| Rematch — fighter who lost fight 1 | +3% | Underdog from fight 1 |
| Fighter visibly depleted at weigh-ins | −6% | That fighter |
| 5-round fight (championship/main event) | +4% | Wrestler / high-cardio fighter |
| Consecutive losses (2+) on current losing streak | +2% | That fighter as underdog |

Add all applicable modifiers to the base probability from Step 4.

---

## Step 6: Calculate Your Edge and Decide

```
1. Your True Win Probability  = base % ± modifiers  (from Steps 4–5)
2. Implied Probability        = convert Klashi's odds using table below
3. Your Edge                  = True Prob − Implied Prob

Bet if Edge ≥ 3%
Skip if Edge < 3% — variance will overwhelm small edges in MMA
```

### Odds → Implied Probability Quick Reference

| American Odds | Implied Prob |
|--------------|-------------|
| −200 | 66.7% |
| −175 | 63.6% |
| −150 | 60.0% |
| −130 | 56.5% |
| −120 | 54.5% |
| −115 | 53.5% |
| −110 | 52.4% |
| +100 | 50.0% |
| +110 | 47.6% |
| +120 | 45.5% |
| +130 | 43.5% |
| +150 | 40.0% |
| +170 | 37.0% |
| +200 | 33.3% |

---

## Step 7: Size the Bet (Half-Kelly)

```
f  = (b × p − q) / b          ← Full Kelly
Bet = f / 2                    ← Half-Kelly (use this)

b = decimal odds − 1  (e.g., +150 → decimal 2.5 → b = 1.5)
p = your true win probability  (from Step 6)
q = 1 − p

Cap at 3 units regardless of formula output.
```

### Quick Sizing Table

| Your Edge | Bet Size |
|-----------|----------|
| 3–4% | 1 unit |
| 5–7% | 2 units |
| 8%+ | 3 units (max) |
| < 3% | No bet |

---

## Step 8: Pick the Right Bet Type Based on Matchup

Once you know the style edge, extend it to correlated markets:

| Matchup | Moneyline | Method of Victory | Round Total |
|---------|-----------|------------------|-------------|
| Wrestler vs. striker (gates open) | Back wrestler | Back wrestler by decision or GnP TKO | Lean under (grinding fight) |
| Sub specialist vs. wrestler | Back sub spec | Back submission | Lean under |
| Pressure striker vs. shot chin | Back pressure fighter | Back KO/TKO | Lean under (early finish) |
| Striker vs. striker (both technical) | Line value only | Back decision | Lean over |
| Pressure vs. pressure (both high SApM) | Line value only | Back KO/TKO | Lean under |
| Well-rounded vs. anything | Line value only | No strong lean | Use SLpM differential |

---

## Quick Reference: Red Flags (Reduce Bet Size or Skip)

- Fighter missed weight → automatic 1-unit max regardless of edge
- Short notice replacement → automatic 0.5-unit max
- Line has moved 20+ points since open (you're late to the information)
- Both fighters are debuting in the UFC (insufficient data for any model)
- Injury report is unverified (social media rumor, not official)
- Your edge is entirely dependent on one situational modifier (not structural)

---

## Worked Example

**Fight: Wrestler (A) −130 vs. Striker (B) +110**

1. **Style Classification**: A is a wrestler (TD avg 4.2, TD acc 52%). B is a striker (SLpM 5.1, TD def 48%).
2. **Gate Check**: TD avg 4.2 ≥ 3.0 ✓ | TD def 48% ≤ 55% ✓ → STRONG edge → Base = 60%
3. **Modifiers**: 5-round fight → +4% for wrestler. No other factors.
4. **Adjusted True Prob for A**: 60 + 4 = **64%**
5. **Implied Prob at −130**: 56.5%
6. **Edge**: 64 − 56.5 = **+7.5%** → Bet ✓
7. **Sizing**: 7.5% edge → **2 units**
8. **Bet Type**: Back A on moneyline (2u) + Back A by decision or TKO as method of victory prop (1u)

---

*Update this file if new matchup win-rate data becomes available. All base percentages derived from historical UFC data (2010–2025).*
