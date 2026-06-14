# UFC / Fight Research — Workflow / Runbook

**Trigger:** when the user says *"research a fight"* or names a card (e.g. *"research UFC 329"* / *"research UFC Freedom 250"*), follow these steps. The deliverable is a per-event folder under `sports/fights/<event-slug>/` containing a card index, deep per-fighter research, a full-card analysis with a **🏆 who-wins prediction table**, and a final bets action sheet.

> Two distinct fighter docs — don't confuse them:
> - **Evergreen profile** → `sports/ufc/fighters/<name>.md` (career-long; updated after each fight). Template: `sports/ufc/fighters/_TEMPLATE.md`.
> - **Matchup-specific deep research** → `sports/fights/<event>/research/<name>.md` (one fight only). Template: `sports/fights/_TEMPLATE/research/_FIGHTER.md`.

---

## Trigger Prompts

Copy-paste one of these. The bracketed bits are the only things to change.

**Sequential (main card only):**
> `Research [EVENT NAME].`
> e.g. *"Research UFC Freedom 250."*

**Parallel — full card, all bouts (recommended for big cards):**
> `Research the full [EVENT NAME] card — every bout, main card + prelims — fan out subagents to research each fight in parallel.`
> e.g. *"Research the full UFC Freedom 250 card — every bout, main card + prelims — fan out subagents to research each fight in parallel."*

**Reusable template (fill the blanks):**
> `Research [EVENT + DATE]. Cover [main card only | full card incl. prelims]. [Use subagents, one per bout, in parallel | run sequentially]. Output the who-wins table and final bets.`

The phrases that flip on **parallel mode**: *"full card" / "every bout" / "incl. prelims"* **and** *"subagents" / "in parallel"*. Omit them and I run the main card sequentially.

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

## Parallel Mode (Subagents)

For a full card (often 12–15 bouts), fan the research out instead of doing it serially.

**Orchestration (what the lead does):**
1. Do **Step 0–2** first — confirm the card and fill `fight-card.md` so every bout + fighter slug is locked before delegating.
2. Launch **one subagent per bout**, all in a **single batch** so they run concurrently (per-bout keeps each matchup coherent; ~1 agent/fight vs ~2 for per-fighter).
3. Wait for all subagents, then do **Step 5 (table) + Step 6 (final bets) + Step 7 (logging)** as the lead — these need the whole card in view.

**Each subagent's brief (one bout):**
- Build/refresh both fighters' evergreen profiles in `sports/ufc/fighters/` (template: `_TEMPLATE.md`).
- Write both deep-research files in `sports/fights/<event>/research/` (template: `research/_FIGHTER.md`).
- Run `analysis/mma-fight-prediction.md` (5-step model) for the bout.
- **Return** to the lead: predicted winner, method + round, Model Win %, market odds + implied %, edge, and a one-line suggested bet. (Files written; only the summary comes back.)

**Lead assembly:** collate the returned summaries into the 🏆 Card Summary table in `fight-analysis.md`, then `final-bets.md` (action sheet, who-wins clean summary, market divergence). Apply bankroll sizing and the `guides/value-betting.md` edge threshold across the whole card last.

> Granularity options: **per-bout** (default — coherent matchup) vs **per-fighter** (deeper isolation, but the prediction must be stitched after). Use per-fighter only when a single fighter needs unusually deep digging.

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
