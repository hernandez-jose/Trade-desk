# MMA Fight Prediction — Methodology

This is the engine behind every UFC pick. It turns research into a **win probability**, then compares that to the market to find an edge. Use it for every bout on a card analyzed via `sports/ufc/RESEARCH-WORKFLOW.md`.

The model's win % feeds the 🏆 Card Summary table in each event's `sports/fights/<event>/fight-analysis.md`.

Companion docs:
- `sports/ufc/overview.md` — bet types, style hierarchies, situational angles
- `analysis/crowd-bias.md` — how public sentiment distorts lines (the edge source)
- `analysis/line-movement.md` — reading steam and reverse line movement
- `analysis/injuries-weather.md` — weight cut / short-notice impact
- `guides/value-betting.md` — the edge threshold required to bet
- `guides/bankroll-management.md` — unit sizing

---

## The 5-Step Model

### Step 1 — Score the seven skill areas
Pull each fighter's 1–10 ratings from their profile (`sports/ufc/fighters/<slug>.md`). If a fighter file has no ratings yet, build them from the UFC stats and tape first.

| Skill Area | What it captures | Primary stat tell |
|------------|------------------|-------------------|
| Boxing | Hands, combinations, head movement | SLpM, striking accuracy |
| Kickboxing / Muay Thai | Kicks, clinch, elbows, distance | Sig. strike variety, leg-kick volume |
| Wrestling | Takedown offense **and** defense | TD avg, TD accuracy, TD defense |
| Jiu-Jitsu / Submissions | Guard, subs, scrambles, position | Sub avg, sub attempts |
| Chin / Durability | Has he been hurt or stopped? | KO losses, knockdowns absorbed |
| Cardio / Endurance | Late-round output | Avg fight time, R3+ output |
| Fight IQ / Adaptability | Game-planning, in-fight adjustments | Rematch results, comeback wins |

### Step 2 — Weight by where the fight happens
A skill only matters if the fight is fought there. Decide who controls the engagement (`overview.md` Step 2), then weight the skill areas:

| Likely fight location | Weighting emphasis |
|-----------------------|--------------------|
| Stays standing | Boxing + Kickboxing + Chin (60%), Cardio + IQ (25%), grappling (15%) |
| Grappling-heavy | Wrestling + JJ (55%), Cardio + IQ (25%), striking + chin (20%) |
| Genuinely mixed | Even split, then let Cardio + Fight IQ break ties |

> The decisive question: **who gets to fight the fight they want?** A 9-rated striker fighting a 9-rated wrestler who controls range loses on tape even though the raw scores tie.

### Step 3 — Compute a composite and convert to a base probability
1. For each skill area, take the **weighted** rating gap (Fighter A − Fighter B).
2. Sum the gaps into a composite score `S` (positive favors A).
3. Map `S` to a base win probability for A using the conversion table:

| Composite gap `S` | Base Win % (favorite) | Read |
|-------------------|----------------------|------|
| 0 | 50% | Pick'em |
| ±1 | ~55% | Slight edge |
| ±2 | ~60% | Clear edge |
| ±3 | ~66% | Strong edge |
| ±4 | ~72% | Large edge |
| ±5 | ~78% | Dominant matchup |
| ±6+ | 82%+ | Mismatch — cap at ~88% (MMA variance is real) |

> **Never exceed ~88%.** Four-ounce gloves mean any fighter can be finished. Hard cap your confidence.

### Step 4 — Apply situational modifiers
Adjust the base probability with multipliers from `overview.md` Step 4 and `injuries-weather.md`. These are the late-breaking edges books are slow to price.

| Factor | Adjustment to the affected fighter |
|--------|-----------------------------------|
| Short-notice replacement (<2 weeks) | −8 to −12% |
| Missed weight | −5 to −10% |
| Long layoff (12+ months) | −3 to −6% (early rounds) |
| Moving up in weight | −4 to −8% |
| Moving down in weight (clean cut) | +2 to +4% |
| UFC debut vs. seasoned UFC opponent | −5 to −8% to the debutant |
| 5-round fight, superior cardio/grappler | +3 to +6% to the high-gas-tank fighter |
| Rematch — underdog from fight 1 | +3 to +5% to that underdog (see overview.md) |

Re-normalize so the two fighters' probabilities sum to 100%.

### Step 5 — Compare to the market and find the edge
1. Convert the market odds to implied probability (`overview.md` has the formula; American odds).
2. **Edge = Model Win % − Implied %.**
3. Bet only if the edge clears the threshold in `guides/value-betting.md` (rule of thumb: **+5% or more** for a moneyline play; demand more on props).
4. Size the bet with `guides/bankroll-management.md` (base unit 1%, max 3u, parlay legs ≤ 0.5u).

---

## Method-of-Victory & Totals

After the winner probability, project **how** it ends — this is where MMA props are mispriced.

| Signal | Method lean | Totals lean |
|--------|-------------|-------------|
| Big chin gap + power puncher | KO/TKO for the puncher | Under |
| Elite grappler vs. weak TD defense | Submission or decision (control) | Under if early sub threat, else Over |
| Two high-volume strikers, good chins | Decision | Over |
| High-cardio pressure fighter, 5 rounds | Decision (late) | Over 3.5 |
| Finisher vs. durable, well-rounded foe | Decision | Over |

State the projected method **and round window** in the prediction table (e.g. "KO R2", "Sub R1", "Dec").

---

## Confidence Labels

Map the final edge + model certainty to a label used in the prediction table and `picks/template.md`:

| Label | Criteria | Typical sizing |
|-------|----------|----------------|
| **Low** | Edge 5–7%, or noisy data (debut, 1-fight sample) | 0.5–1u |
| **Standard** | Edge 7–12%, solid data, clear style read | 1–2u |
| **High** | Edge 12%+, clean style mismatch, healthy camps | 2–3u |
| **Pass** | Edge < 5% or contradictory signals | 0u — no bet |

---

## Worked Mini-Example

> Striker A (Boxing 8, Chin 7, Cardio 6) vs. Wrestler B (Wrestling 9, TD def 8, Cardio 8), B controls where it happens.

1. Fight location: grappling-heavy → weight wrestling/JJ at 55%.
2. B's wrestling edge dominates the weighted composite → `S ≈ −2.5` (favors B).
3. Base: B ≈ 63%.
4. Situational: 3-round fight, no flags → no change. A is **not** short-notice. B stays ~63%.
5. Market has B at −150 (implied 60%). Edge = 63% − 60% = **+3%** → below the 5% threshold → **Pass** (or a small method play if B-by-decision is priced soft).

The discipline is in Step 5: a correct winner pick is **not** a bet unless the price is wrong.
