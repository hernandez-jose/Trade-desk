# {{Country / Club Name}} — Team Profile

> Last updated: {{Month Day, Year}} — update after each match
> Competition: {{FIFA World Cup 2026 / UEFA Champions League / etc.}}

> **Template usage:** Copy this file to `sports/soccer/teams/<team-slug>.md` (kebab-case, e.g. `argentina.md`, `manchester-city.md`). Fill every `{{placeholder}}`. Leave a stat as `—` when unknown. Delete this usage block in the real file.

---

## Identity

| Attribute | Detail |
|-----------|--------|
| Full name | {{full official name}} |
| Nickname | {{nickname}} |
| Country / League | {{country or league}} |
| Head Coach | {{coach name}} |
| Formation (default) | {{e.g. 4-3-3}} |
| FIFA Ranking | {{rank}} |
| Confederation | {{UEFA / CONMEBOL / CONCACAF / CAF / AFC / OFC}} |
| Home Venue | {{stadium, city}} |
| Kit Colors | {{primary / secondary}} |

---

## Current Form (Last 10 Matches)

| # | Date | Opponent | Comp | Result | Score | Notes |
|---|------|----------|------|--------|-------|-------|
| 1 | {{date}} | {{opponent}} | {{comp}} | {{W/D/L}} | {{x–x}} | {{notes}} |

**Record (last 10):** {{W}}W – {{D}}D – {{L}}L  
**Goals scored (last 10):** {{n}}  
**Goals conceded (last 10):** {{n}}  
**Clean sheets (last 10):** {{n}}

---

## World Cup / Tournament Record

| Stage | Opponent | Result | Score |
|-------|----------|--------|-------|
| {{Group A — MD1}} | {{opponent}} | {{W/D/L}} | {{x–x}} |

**Current standing:** {{position in group / round reached}}

---

## Key Players

| Player | Position | Role | Status | Notes |
|--------|----------|------|--------|-------|
| {{name}} | {{GK/CB/LB/RB/CDM/CM/CAM/LW/RW/ST}} | {{e.g. captain, set-piece taker}} | {{Available / Doubtful / Out}} | {{notes}} |

---

## Tactical Profile

**Default System:** {{e.g. 4-3-3 with high press}}

**How they attack:**
{{2–4 sentences on buildup, key movements, pressing triggers, set-piece threats.}}

**How they defend:**
{{2–4 sentences on defensive shape, press, transitions, set-piece defense.}}

**Pressing Intensity:** {{High / Medium / Low}}  
**Possession Style:** {{Dominant / Balanced / Counter-attack}}  
**Set-Piece Threat (offense):** {{High / Medium / Low}}  
**Set-Piece Vulnerability (defense):** {{High / Medium / Low}}

---

## Tactical Ratings (for the prediction model)

> These feed `RESEARCH-WORKFLOW.md` Step 5. Rate 1–10.

| Skill Area | Rating |
|------------|--------|
| Attacking Quality (build-up, chance creation) | {{n}} |
| Defensive Solidity (structure, press resistance) | {{n}} |
| Set Pieces (offense + defense combined) | {{n}} |
| Midfield Control (possession, transitions) | {{n}} |
| Individual Quality / Star Players | {{n}} |
| Physical / Fitness / Squad Depth | {{n}} |

**Composite Score (baseline — neutral venue, full squad):** {{n}} / 10 — recalculated per matchup in `match-analysis.md` with contextual weights applied

---

## Strengths

| Strength | Rating (1–10) | Notes |
|----------|--------------|-------|
| {{e.g. Counter-attack speed}} | **{{n}}** | {{notes}} |

---

## Weaknesses

| Weakness | Risk Level | Notes |
|----------|-----------|-------|
| {{e.g. Aerial defending}} | **{{Low/Med/High}}** | {{notes}} |

---

## Situational Flags

> Tick any that apply to the next match.

- [ ] Key player suspended (1-match ban)
- [ ] Key player injured / doubtful
- [ ] Short rest (<3 days since last match)
- [ ] Must-win / elimination match
- [ ] Coming off a heavy defeat (morale hit)
- [ ] Playing at altitude / extreme heat
- [ ] Historically poor record vs. this opponent
- [ ] Heavy public favorite (square money — consider fading)
- [ ] Manager under pressure / reported dressing room issues
- [ ] Players on yellow card accumulation alert (1 card from suspension)
- [ ] Dead rubber / mutual advancement scenario (both teams content with a draw)

---

## Betting Profile

### When to back

| Scenario | Lean |
|----------|------|
| {{e.g. vs. low-block teams}} | **{{Back / Strong back}}** |

### When to fade

| Scenario | Lean |
|----------|------|
| {{e.g. Slow starts — lay first half}} | **{{Fade / Neutral}}** |

### Market Tendencies
- **1X2:** {{note — e.g. "Covers as favorite 68% ATS"}}
- **O/U 2.5 Goals:** {{note — e.g. "Overs in 6 of last 10"}}
- **BTTS:** {{note}}
- **Asian Handicap:** {{note}}

---

## Head-to-Head vs. Key Opponents

| Opponent | Last 5 H2H | W–D–L | Avg Goals | Notes |
|----------|-----------|-------|-----------|-------|
| {{opponent}} | {{dates}} | {{W–D–L}} | {{x.x}} | {{notes}} |

---

## Power Rating

| Category | Score (1–10) |
|----------|-------------|
| Overall | **{{n}}** |
| vs. High-Press Teams | **{{n}}** |
| vs. Low-Block Teams | **{{n}}** |
| vs. Counter-Attack Teams | **{{n}}** |
| Knockout / Must-Win Games | **{{n}}** |
| Neutral Venue | **{{n}}** |
| As favorite (−150 or shorter) | **{{n}}** |
| As underdog (+120 or longer) | **{{n}}** |

---

## Sources
- [FIFA Team Page]({{url}})
- [Transfermarkt]({{url}})
- [FBref / StatsBomb]({{url}})
- [Understat]({{url}})
- [SofaScore]({{url}})
