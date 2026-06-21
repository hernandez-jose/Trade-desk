# Soccer Match Prediction Model — 5-Step Framework

> This is the canonical prediction engine for soccer match analysis. Reference from `sports/soccer/RESEARCH-WORKFLOW.md` Step 5 and `sports/soccer/matches/_TEMPLATE/match-analysis.md`.
> Parallel document for MMA: `analysis/mma-fight-prediction.md`.

---

## Overview

The model converts team research into a structured win/draw/loss probability estimate, which is then compared to the market's implied probability to identify edge.

**Inputs:** Tactical Ratings from both team profiles (`sports/soccer/teams/<team>.md`)  
**Output:** True Win % / Draw % / Loss % per team → Edge vs. market odds

---

## Step 1 — Score Six Skill Areas (Rate Each Team 1–10)

Pull ratings from the team's evergreen profile. If a profile doesn't exist yet, estimate from available form/stats and flag as provisional.

| Skill Area | Weight | Notes |
|------------|--------|-------|
| Attacking Quality (build-up, chance creation, xG) | **20%** | Use xG/game as cross-check on rating |
| Defensive Solidity (structure, press resistance, xGA) | **20%** | Use xGA/game as cross-check |
| Set Pieces (offense + defense combined) | **15%** | ~30–35% of goals come from set pieces; market underprices |
| Midfield Control (possession, transitions, PPDA) | **15%** | PPDA < 8 = high-press dominance |
| Individual Quality / Star Players | **15%** | Adjust if key player is absent (see Step 2) |
| Physical / Fitness / Squad Depth | **15%** | Apply fatigue modifier for short rest |

**Weights sum to 100%.** Rate on your best available data; note data quality (5+ games = reliable, <5 = provisional).

---

## Step 2 — Apply Contextual Weights

Adjust ratings before computing the composite. Do not skip this step — a paper rating means nothing without context.

| Contextual Factor | Adjustment |
|-------------------|-----------|
| Neutral venue (World Cup, neutral site) | No home advantage modifier |
| Home venue | +0.5 to Composite Score for the home team |
| Knockout / must-win pressure | Raise pressure modifier: reduce mental-strength estimate for low-pressure-history sides |
| Short rest (< 3 days since last match) | −1 to Physical rating for fatigued team |
| Altitude ≥ 1,500m (Denver, Mexico City, Guadalajara, Monterrey) | −1 to Physical rating for teams not altitude-acclimatized |
| Key attacking player absent (starter-level) | −1 to Attacking Quality and Individual Quality for that team |
| Key goalkeeper or CB absent | −1 to Defensive Solidity |
| Goalkeeper on yellow card alert | Minor — note only |

Apply each adjustment to the raw rating before calculating the composite.

---

## Step 3 — Calculate Composite Score

```
Composite = (Attacking × 0.20) + (Defensive × 0.20) + (Set Pieces × 0.15)
          + (Midfield × 0.15) + (Individual × 0.15) + (Physical × 0.15)
```

The composite is on a **0–10 scale** (ratings are 1–10, weights sum to 1.0).

```
Differential = Team A Composite − Team B Composite
```

A positive differential means Team A is rated stronger. Maximum realistic differential in a competitive match: ~3.0. Differentials above 2.5 are dominant mismatches.

**Cross-check with xG data:** If the composite differential and the recent xG differential (xG per game minus xGA per game, last 5–8 matches) point in opposite directions, flag it. Lower confidence until you reconcile the disagreement.

---

## Step 4 — Base Win / Draw / Loss Probability

Look up the composite differential in the table to get base probabilities. "Strong Team" = the team with the higher composite score.

| Composite Differential | Strong Team Win % | Draw % | Weak Team Win % |
|------------------------|-------------------|--------|-----------------|
| 0.0–0.5 (even match) | 38% | 28% | 34% |
| 0.6–1.0 | 42% | 27% | 31% |
| 1.1–1.5 | 50% | 26% | 24% |
| 1.6–2.0 | 58% | 23% | 19% |
| 2.1+ | 65%+ | 20% | 15% |

> Note: At differential 0.0–0.5 the "Weak Team Win %" is lower than "Strong Team Win %" because even a slight rating edge produces an asymmetry in a competitive match. Draw probability stays above 27% even in moderately mismatched games because weaker teams can defend and absorb pressure.

---

## Step 5 — Situational Modifiers and Edge

Apply to the base probabilities from Step 4. Then **renormalize**.

### Modifiers

| Situation | Effect |
|-----------|--------|
| Must-win (elimination) for Team A | +5% to Team A Win %; redistribute from Draw and Team B Win |
| Coming off a loss (tournament) — Team A | +3% to Team A Win % (motivation/bounce) |
| Mutual advancement / dead rubber (draw suits both) | −12% to BTTS Yes; suppress goal total by 0.3; draw probability +5% |
| Heavy public side (Team A >70% of bets; line moved against them) | Consider fading — shift +3–5% toward Draw or Team B |
| Team A scored early in most recent match (fast start history) | Minor — note in analysis |

### Renormalization (Required)

After applying all modifiers, the three probabilities will likely no longer sum to 100%. Renormalize:

```
Sum = (Raw Win %) + (Raw Draw %) + (Raw Loss %)

True Win %  = Raw Win %  ÷ Sum
True Draw % = Raw Draw % ÷ Sum
True Loss % = Raw Loss % ÷ Sum
```

This ensures the numbers remain a valid probability distribution before calculating edge.

### Edge Calculation

```
Edge = True % − Implied %

Where Implied % = 1 / Decimal Odds
Or for American odds:
  Negative: Implied % = |odds| / (|odds| + 100)
  Positive: Implied % = 100 / (odds + 100)
```

**Flag for action: Edge ≥ +5%** (consistent with `guides/value-betting.md`)

---

## Worked Example

**Match:** Team A vs. Team B — WC Group Stage, neutral venue

**Raw Ratings:**

| Skill Area | Weight | Team A | Team B |
|------------|--------|--------|--------|
| Attacking Quality | 20% | 7.5 | 6.0 |
| Defensive Solidity | 20% | 6.5 | 7.0 |
| Set Pieces | 15% | 6.0 | 5.5 |
| Midfield Control | 15% | 7.0 | 6.5 |
| Individual Quality | 15% | 8.0 | 6.0 |
| Physical / Depth | 15% | 6.5 | 7.0 |

**Contextual adjustments:** Team A key striker doubtful → −1 to Attacking Quality and Individual Quality for Team A.

**Adjusted Ratings:** Team A Attacking = 6.5, Individual = 7.0.

**Composite Scores:**
```
Team A: (6.5×0.20) + (6.5×0.20) + (6.0×0.15) + (7.0×0.15) + (7.0×0.15) + (6.5×0.15)
      = 1.30 + 1.30 + 0.90 + 1.05 + 1.05 + 0.975 = 6.575

Team B: (6.0×0.20) + (7.0×0.20) + (5.5×0.15) + (6.5×0.15) + (6.0×0.15) + (7.0×0.15)
      = 1.20 + 1.40 + 0.825 + 0.975 + 0.90 + 1.05 = 6.35
```

**Differential:** 6.575 − 6.35 = **0.225** → Row 1 (0.0–0.5)

**Base probabilities:** Team A Win 38% / Draw 28% / Team B Win 34%

**Modifier:** Team B must win (must-win situation) → +5% to Team B Win %

**Post-modifier (before renormalization):** Team A 38% / Draw 28% / Team B 39% = 105%

**Renormalized:** Team A 36.2% / Draw 26.7% / Team B 37.1% (sums to 100%)

**Market:** Team A −120 (implied 54.5%), Draw +280 (implied 26.3%), Team B +200 (implied 33.3%)

**Edge:**
- Team A: 36.2% − 54.5% = −18.3% → **Pass (no edge)**
- Draw: 26.7% − 26.3% = +0.4% → **Pass (below threshold)**
- Team B: 37.1% − 33.3% = +3.8% → **Pass (below +5% threshold)**

→ No bet. The situation is interesting but the market correctly priced Team B's must-win pressure.

---

## Integration with Research Files

| File | Role |
|------|------|
| `sports/soccer/teams/<team>.md` | Source of Tactical Ratings (Step 1 input) |
| `sports/soccer/matches/<event>/research/<team>.md` | Contextual adjustments (Step 2 inputs) |
| `sports/soccer/matches/<event>/match-analysis.md` | Where you fill the model output + Edge table |
| `sports/soccer/matches/<event>/final-bets.md` | Carries through only bets that clear ≥ +5% edge |
| `picks/2026/<month>.md` | Logs placed bets |
| `picks/2026/tracking.md` | Long-term P&L and CLV tracking |

---

## Quick Reference

**The two things that matter most in the model:**

1. **Set Pieces are underrated.** 30–35% of goals come from corners and free kicks, but standard ratings weight them implicitly. Rate this skill area honestly — it is the single biggest market inefficiency in soccer.

2. **Renormalize always.** Forgetting this step produces fictional edge numbers. One extra line of arithmetic; never skip it.
