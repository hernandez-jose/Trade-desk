# Soccer / World Cup Research — Workflow / Runbook

**Trigger:** when the user says *"research a match"* or names a fixture (e.g. *"research Argentina vs Brazil"* / *"research USA vs England WC2026"*), follow these steps. The deliverable is a per-match folder under `sports/soccer/matches/<match-slug>/` containing a match card, deep per-team research, a full match analysis with a **🏆 predicted outcome table**, and a final bets action sheet.

> Two distinct team docs — don't confuse them:
> - **Evergreen profile** → `sports/soccer/teams/<team-slug>.md` (tournament-long; updated after each match). Template: `sports/soccer/teams/_TEMPLATE.md`.
> - **Matchup-specific deep research** → `sports/soccer/matches/<match-slug>/research/<team-slug>.md` (one match only). Template: `sports/soccer/matches/_TEMPLATE/research/_TEAM.md`.

---

## Trigger Prompts

**Single match:**
> `Research [TEAM A] vs [TEAM B] — [competition + round].`
> e.g. *"Research Argentina vs Brazil — World Cup 2026 Group C."*

**Multiple matches in parallel (recommended for full matchday):**
> `Research the full [MATCHDAY / GROUP] — fan out subagents to research each match in parallel.`
> e.g. *"Research all Group A World Cup 2026 matches — fan out subagents in parallel."*

**Reusable template:**
> `Research [TEAM A] vs [TEAM B] — [competition, round, date, venue]. [Use subagents in parallel | run sequentially]. Output the predicted outcome and final bets.`

Parallel mode triggers: *"full matchday" / "all groups" / "every match"* **and** *"subagents" / "in parallel"*.

---

## Step 0 — Confirm the fixture
Identify: teams, competition, round/stage, date, venue, kickoff time. Note group standings if applicable. Confirm the match is announced before proceeding.

> Live data (squad news, odds, form) requires network access. If blocked, scaffold from templates with `—` placeholders and flag what to fill.

## Step 1 — Scaffold the match folder
Copy `sports/soccer/matches/_TEMPLATE/` to `sports/soccer/matches/<match-slug>/` (e.g. `wc2026-usa-vs-england/`). You now have `match-card.md`, `match-analysis.md`, `final-bets.md`, and `research/`.

## Step 2 — Fill the match card
Complete `match-card.md`: competition, round, venue, kickoff, referee, group/bracket context, and link each team to their evergreen profile in `sports/soccer/teams/`.

## Step 3 — Team profiles (evergreen)
For both teams, create or refresh `sports/soccer/teams/<team-slug>.md` from `sports/soccer/teams/_TEMPLATE.md`. Always complete the **Tactical Ratings** and **Situational Flags** — the prediction model uses them.

## Step 4 — Deep per-team research (matchup-specific)
For each team, fill `sports/soccer/matches/<match-slug>/research/<team-slug>.md` from `research/_TEAM.md`. Cover: current form, squad availability, tactical setup vs. this specific opponent, key players, set-piece threat, and market positioning.

## Step 5 — Predict the match
Run `analysis/soccer-match-prediction.md` (5-step model) per match: score 6 tactical areas → apply contextual weights → composite differential → base win/draw/loss % → situational modifiers → renormalize → edge vs. market. Fill each section in `match-analysis.md`, then the **🏆 Outcome Prediction table**.

The full model with worked example lives in `analysis/soccer-match-prediction.md`. Summary of the 5 steps:

### 5-Step Soccer Prediction Model (Summary)

**Step 1 — Skill Area Scoring (rate each team 1–10)**

| Skill Area | Weight |
|------------|--------|
| Attacking Quality (build-up, chance creation) | 20% |
| Defensive Solidity (structure, press resistance) | 20% |
| Set Pieces (offense + defense combined) | 15% |
| Midfield Control (possession, transitions) | 15% |
| Individual Quality / Star Players | 15% |
| Physical / Fitness / Squad Depth | 15% |

**Step 2 — Contextual Weights**
- Neutral venue: reduce home advantage to 0
- Tournament knockout: raise pressure modifier (form collapses for low-mental-strength sides)
- Short rest (<3 days): −1 to Physical rating for fatigued team
- Injury to key player: −1 to relevant Skill Area

**Step 3 — Composite Score**
`Composite = Σ (Rating × Weight)` for each team. The result is on a **0–10 scale** (each rating is 1–10, weights sum to 100%). Calculate the differential: Team A composite − Team B composite. A positive differential favors Team A. Maximum possible differential is 9.0 (impossible in practice — real matches cluster between 0 and 3.0).

**Step 4 — Base Win/Draw/Loss Probability**
Convert composite differential to implied probabilities using the table:

| Composite Differential (0–10 scale) | Strong Team Win % | Draw % | Weak Team Win % |
|--------------------------------------|-------------------|--------|-----------------|
| 0.0–0.5 (even match) | 38% | 28% | 34% |
| 0.6–1.0 | 42% | 27% | 31% |
| 1.1–1.5 | 50% | 26% | 24% |
| 1.6–2.0 | 58% | 23% | 19% |
| 2.1+ | 65%+ | 20% | 15% |

**Step 5 — Situational Modifiers & Edge**
Apply to base probabilities:
- Must-win situation: +5% to attacking team win probability
- Coming off a loss (tournament): +3% motivation boost (revenge/elimination fear)
- Heavy public square side: check if line has moved >0.5 AH — consider fading
- Altitude ≥ 1,500m (Denver, Mexico City, Guadalajara, Monterrey): −1 to Physical rating for teams not acclimatized; reduces effective composite by ~0.15
- **Mutual advancement / dead rubber**: Both teams advance with a draw → −12% to BTTS Yes; apply Under lean; suppress goal-line by 0.3
- Referee tendency (knockout stages): note home/away card rate if historical data available; generally minor at neutral WC venues

> **Renormalize after all modifiers:** Win % + Draw % + Loss % must equal 100%. After applying modifiers, sum the three raw values and divide each by the total: `True % = raw % ÷ (raw Win + raw Draw + raw Loss)`. Skipping this step will produce incorrect edge calculations.

Calculate edge: `Edge = True % − Implied %`. Flag bets with edge ≥ **+5%** (consistent with `guides/value-betting.md`).

## Step 6 — Final bets
Distill `match-analysis.md` into `final-bets.md`: odds snapshot, per-market verdicts, action sheet (sized per `guides/bankroll-management.md`), clean outcome summary, and prediction-market vs. sportsbook divergence. Flag only bets clearing the `guides/value-betting.md` edge threshold.

## Step 7 — Log & review
Log placed bets in `picks/2026/<month>.md` (template: `picks/template.md`, tag SOCCER/WC2026) and results in `picks/2026/tracking.md`. After the match, fill results back into `final-bets.md`.

---

## Parallel Mode (Subagents)

For a full matchday or group stage (often 4–8 matches at once), fan research out instead of running serially.

**Orchestration:**
1. Do **Step 0–2** first — confirm all fixtures so match slugs are locked before delegating.
2. Launch **one subagent per match**, all in a **single batch**.
3. Wait for all subagents, then do **Step 5 (table) + Step 6 (final bets) + Step 7 (logging)** as the lead.

**Each subagent's brief (one match):**
- Build/refresh both teams' evergreen profiles in `sports/soccer/teams/`.
- Write both deep-research files in `sports/soccer/matches/<match-slug>/research/`.
- Run the 5-step soccer prediction model.
- **Return** to the lead: predicted outcome, model probabilities, market odds + implied %, edge, and a one-line suggested bet.

---

## Key Soccer Betting Markets (priority order)

| Market | Notes |
|--------|-------|
| Asian Handicap (half-ball: −0.5, +0.5) | Best juice; eliminates draw variable; most common line |
| Asian Handicap (quarter-ball: −0.25, −0.75, +0.25, +0.75) | Stake splits between two adjacent lines; half-win/half-push possible; use for close matches |
| Asian Handicap (whole-ball: −1, +1) | Push (refund) if margin equals handicap exactly; use when dominant win expected |
| Over/Under 2.5 Goals | Most liquid; use 1.5/3.5 when justified |
| 1X2 (Match Result) | Only when draw has clear value or backing an underdog |
| Draw No Bet (DNB) | Effectively AH 0; returns stake on draw; often better juice than 1X2 for slight favorites |
| Both Teams to Score | Good in open knockout games; very sensitive to striker availability |
| First Half AH / O-U | Strong coaching-matchup edges; less efficient market |
| Double Chance | Use when backing underdog but draw is possible |

> Avoid: exact score, first scorer, scorecasts — juice is prohibitive. **Exception:** 0-0 or 1-0 correct scores may offer value when both teams have incentive to protect a narrow result — check implied % vs. True % from the goal total model.

**Asian Handicap Quick Reference:**
- Quarter-ball lines (−0.25, +0.25, −0.75, +0.75) are the most common WC lines. Your stake is split 50/50 between the two adjacent lines. A "half-win" returns full stake + half profit. A "half-loss" loses only half the stake.
- Prefer AH −0.5 over −1 unless the model differential exceeds 1.5 and the weaker team shows clear vulnerability. AH −1.5+ requires high confidence.
- In mismatched WC group matches, AH is exceptionally sharp due to Asian betting volume — pivot to O/U or Draw if no AH edge exists.

---

## Output Checklist
- [ ] `sports/soccer/matches/<match-slug>/match-card.md` — fixture info, linked profiles
- [ ] `sports/soccer/teams/<team-slug>.md` per team (tactical ratings + flags complete)
- [ ] `sports/soccer/matches/<match-slug>/research/<team-slug>.md` per team
- [ ] `match-analysis.md` with **🏆 Outcome Prediction table** (model probabilities shown)
- [ ] `final-bets.md` action sheet — only +EV plays, bankroll-sized
- [ ] Results logged in `picks/2026/tracking.md` post-match

## File Map
```
sports/
└── soccer/
    ├── overview.md                       # bet types, angles, league efficiency
    ├── RESEARCH-WORKFLOW.md              # this file
    ├── teams/
    │   ├── _TEMPLATE.md                  # evergreen team-profile template
    │   └── <team-slug>.md                # one persistent profile per team
    └── matches/
        ├── _TEMPLATE/                    # copy this to start a new match
        │   ├── match-card.md
        │   ├── match-analysis.md         # holds the 🏆 outcome prediction table
        │   ├── final-bets.md
        │   └── research/_TEAM.md         # deep matchup-research template
        └── <match-slug>/                 # e.g. wc2026-usa-vs-england/
            ├── match-card.md
            ├── match-analysis.md
            ├── final-bets.md
            └── research/<team-slug>.md
analysis/
├── line-movement.md                      # steam, CLV, reverse line movement
├── crowd-bias.md                         # public-sentiment distortion
└── injuries-weather.md                   # situational impact guide
```
