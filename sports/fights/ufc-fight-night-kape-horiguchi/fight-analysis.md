# {{Event}} — Full Card Fight Analysis & Win Predictions

> Methodology: `analysis/mma-fight-prediction.md` (5-step model → win % → edge).
> Source profiles: `sports/ufc/fighters/`. Deep research: `./research/`.
> Last updated: {{Month Year}}

> **Template usage:** Copy to `sports/fights/<event-slug>/fight-analysis.md`. Repeat the Bout block for every fight, then fill the 🏆 Card Summary table. Delete this usage block.

---

## Bout 1 — Main Event | {{Division}} ({{lbs}} lbs) | {{3/5}} Rounds
# {{Fighter A}} vs. {{Fighter B}}

### Fight Context
{{Stakes, layoff, debut, rematch, ranking implications.}}

### Style Matchup
{{Who controls where the fight happens (overview.md Step 2). Skill-area edges from the fighter files.}}

| Skill Area | {{A}} | {{B}} | Edge |
|------------|-------|-------|------|
| Boxing | {{n}} | {{n}} | {{A/B}} |
| Kickboxing / MT | {{n}} | {{n}} | {{A/B}} |
| Wrestling | {{n}} | {{n}} | {{A/B}} |
| Jiu-Jitsu / Subs | {{n}} | {{n}} | {{A/B}} |
| Chin / Durability | {{n}} | {{n}} | {{A/B}} |
| Cardio | {{n}} | {{n}} | {{A/B}} |
| Fight IQ | {{n}} | {{n}} | {{A/B}} |

### Weight Cut Analysis
{{Cut difficulty, history of missing weight, rehydration — see `analysis/injuries-weather.md`.}}

### Injury Report
{{Known injuries, surgeries, layoff/rust.}}

### Performance Prediction
**Most Likely Scenario ({{%}}):** {{...}}
**Alternate Scenario A ({{%}}):** {{...}}
**Alternate Scenario B ({{%}}):** {{...}}

### Betting Analysis
| Fighter | Odds | Implied % | True % (est.) | Edge |
|---------|------|-----------|---------------|------|
| {{A}} | {{}} | {{}} | {{}} | {{+/−}} |
| {{B}} | {{}} | {{}} | {{}} | {{+/−}} |

**Method Props:** {{leans}}
**Totals:** {{over/under lean + reasoning}}

### ✅ Recommended Pick
> **Pick:** {{side + market}}
> **Odds:** {{}}
> **Unit size:** {{u}}
> **Confidence:** {{Low / Medium / High}}
> **Reasoning:** {{1–2 lines}}

---

> Repeat the Bout block for every fight on the card.

## 🏆 Card Summary — Who Wins (All Picks)

| Bout | Predicted Winner | Method | Model Win % | Pick (bet) | Odds | Units | Confidence |
|------|------------------|--------|-------------|------------|------|-------|------------|
| {{A}} vs. {{B}} | **{{winner}}** | {{KO/Sub/Dec + rd}} | {{%}} | {{bet side/market}} | {{}} | {{u}} | {{}} |
| Christian Rodriguez vs. Hyder Amil (FW 145, 3R, main card) | **Christian Rodriguez** | Dec (control); live Sub | 62% | Pass ML (-150/-155 only ~+2% edge); small Rodriguez-by-decision/sub prop if soft | -150/-155 | 0u | Pass (Low lean) |
| Farid Basharat vs. Ethyn Ewing (BW 135, 3R, prelim) | **Farid Basharat** | Decision (control) | 57% | Basharat ML (control-decision; +8.9% edge over +108) | +108 | 1u | Standard |
| Bia Mesquita vs. Melissa Mullins (WBW 135, 3R, prelim) | **Bia Mesquita** | Sub (RNC) R1–R2 | 84% | Pass ML (-600 fully priced); lean Mesquita-by-sub / inside-distance prop if soft | -600 | 0u | Pass |
| André Lima vs. Kevin Borjas (FLW 125, 3R, prelim) | **André Lima** | Dec (or TKO R2–R3) | 83% | Pass ML (-700/-770 no value); lean Lima inside-distance / by-decision prop if soft | -700/-770 | 0u | High (winner) / Pass (bet) |
| Allan Nascimento vs. Mitch Raposo (FLW 125, 3R, prelim) | **Allan Nascimento** | Sub R1–R2 (or grappling-control Dec) | 64% | Pass ML (-205 ≈ 67% implied, ~−3% edge); lean Nascimento-by-submission prop if priced near/above ML | -205 | 0u | Pass (Standard winner lean) |
| Gaston Bolaños vs. Michael Aswell Jr. (FW 145, 3R, prelim) | **Michael Aswell Jr.** | KO/TKO R1–R2 (or volume Dec) | 56% | **Bolaños ML** — live dog in a pure striking fight (no TD threat neutralizes his only hole); model 44% vs ~23% implied = **+20.7% edge** | Bolaños +330 | 1.5u | Standard (value on dog) |
| Jhonata Diniz vs. José Luiz (HW 265, 3R, main card) | **CANCELLED** — Diniz withdrew (undisclosed); José Luiz vs. TBD/off | — | — | No bet — no contest, no line | — | 0u | Pass (cancelled) |

**Total exposure:** {{N}} units
**Best bet on the card:** {{which + why}}

> Note: the predicted **winner** and the **bet** can differ when the line is mispriced (back the value side, not always the likely winner). Carry final action to `final-bets.md`. Log results in `picks/2026/tracking.md`.
