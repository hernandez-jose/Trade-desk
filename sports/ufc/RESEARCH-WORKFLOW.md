# UFC / Fight Research — Workflow / Runbook

**Trigger:** when the user says *"research a fight"* or names a card (e.g. *"research UFC 329"* / *"research UFC Freedom 250"*), follow these steps. The deliverable is a per-event folder under `sports/fights/<event-slug>/` containing a card index, deep per-fighter research, a full-card analysis with a **🏆 who-wins prediction table**, and a final bets action sheet.

> Two distinct fighter docs — don't confuse them:
> - **Evergreen profile** → `sports/ufc/fighters/<name>.md` (career-long; updated after each fight). Template: `sports/ufc/fighters/_TEMPLATE.md`.
> - **Matchup-specific deep research** → `sports/fights/<event>/research/<name>.md` (one fight only). Template: `sports/fights/_TEMPLATE/research/_FIGHTER.md`.

---

## Step 0 — Confirm the card
Identify the event: name, date, venue, broadcast, and every announced bout with division + round count (championship/main-event = 5 rounds, else 3). If the card is unannounced or ambiguous, ask before proceeding.

> Live data (records, stats, odds) requires this environment's network policy to allow web access. If blocked, scaffold from the templates with `—`/placeholders and flag what to fill.

## Step 1 — Scaffold the event folder
Copy `sports/fights/_TEMPLATE/` to `sports/fights/<event-slug>/` (e.g. `ufc-329/`). You now have `fight-card.md`, `fight-analysis.md`, `final-bets.md`, and `research/`.

## Step 2 — Fill the card index
Complete `fight-card.md`: list every bout, records, rankings, stakes, and link each fighter to their `sports/ufc/fighters/<name>.md` profile.

## Step 3 — Fighter profiles (evergreen)
For every fighter, create or refresh `sports/ufc/fighters/<name>.md` from `sports/ufc/fighters/_TEMPLATE.md`. Always complete the **Skill Ratings** and **Situational Flags** — the prediction model uses them.

## Step 4 — Deep per-fighter research
For each fighter, fill `sports/fights/<event>/research/<name>.md` from `research/_FIGHTER.md` (the 13-section matchup breakdown: striking, grappling, cardio, psychology, camp, market, paths to victory, confidence).

## Step 5 — Predict every bout
Run `analysis/mma-fight-prediction.md` (5-step model) per bout: score 7 skill areas → weight by where the fight happens → composite → base win % → situational modifiers → edge vs. market. Project method + round window. Fill each Bout block in `fight-analysis.md`, then the **🏆 Card Summary — Who Wins** table.

## Step 6 — Final bets
Distill `fight-analysis.md` into `final-bets.md`: odds snapshot, per-bout verdicts, action sheet (sized per `guides/bankroll-management.md`), the "Who Wins" clean summary, and prediction-market vs. sportsbook divergence. Flag only bets clearing the `guides/value-betting.md` edge threshold. The predicted winner and the bet may differ when the line is mispriced.

## Step 7 — Log & review
Log placed bets in `picks/2026/<month>.md` (template: `picks/template.md`, tag UFC) and results in `picks/2026/tracking.md`. After the card, fill results back into `final-bets.md`. Records are the only truth — log misses honestly (`CLAUDE.md` Golden Rules).

---

## Output checklist
- [ ] `sports/fights/<event>/fight-card.md` — every bout, linked to profiles
- [ ] `sports/ufc/fighters/<name>.md` per fighter (skill ratings + flags complete)
- [ ] `sports/fights/<event>/research/<name>.md` per fighter (13 sections)
- [ ] `fight-analysis.md` with filled 🏆 Card Summary prediction table (Model Win % shown)
- [ ] `final-bets.md` action sheet — only +EV plays, bankroll-sized
- [ ] Sources cited; post-event review left ready

## File map
```
sports/
├── ufc/
│   ├── overview.md                     # bet types, angles, style hierarchies
│   ├── RESEARCH-WORKFLOW.md            # this file
│   └── fighters/
│       ├── _TEMPLATE.md                # evergreen fighter-profile template
│       └── <name>.md                   # one persistent profile per fighter
└── fights/
    ├── _TEMPLATE/                      # copy this to start a new card
    │   ├── fight-card.md
    │   ├── fight-analysis.md           # holds the 🏆 who-wins table
    │   ├── final-bets.md
    │   └── research/_FIGHTER.md        # deep matchup-research template
    └── <event-slug>/                   # e.g. ufc-329/
        ├── fight-card.md
        ├── fight-analysis.md
        ├── final-bets.md
        └── research/<name>.md
analysis/
├── mma-fight-prediction.md             # the 5-step prediction model
├── crowd-bias.md                       # public-sentiment distortion
├── line-movement.md
└── injuries-weather.md
```
