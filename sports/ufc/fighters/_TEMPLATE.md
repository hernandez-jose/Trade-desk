# {{Fighter Name}} — Fighter Profile

> Nickname: "{{nickname}}"
> Last updated: {{Month Day, Year}} — update after each fight

> **Template usage:** Copy this file to `sports/ufc/fighters/<first-last>.md` (kebab-case, e.g. `dom-mar-fan.md`). Fill every `{{placeholder}}`. Leave a stat as `—` when unknown and note where to source it. Delete this usage block in the real file.

---

## Identity

| Attribute | Detail |
|-----------|--------|
| Full name | {{full name}} |
| Nickname | {{nickname}} |
| DOB | {{Month Day, Year}} |
| Age | {{age}} |
| Nationality | {{nationality}} |
| Hometown | {{hometown}} |
| Fighting out of | {{city}} |
| Team / Gym | {{gym}} |
| Coach | {{coach}} |
| Weight class | {{division}} ({{lbs}} lbs) |
| Height | {{ft'in"}} ({{cm}} cm) |
| Reach | {{in}}" ({{cm}} cm) |
| Stance | {{Orthodox / Southpaw / Switch}} |

---

## Record

**{{W–L–D}}** ({{UFC record}} UFC)

| # | Result | Opponent | Method | Event | Date | Rd | Time |
|---|--------|----------|--------|-------|------|----|------|
| {{n}} | **{{Win/Loss}}** | {{opponent}} | {{method}} | {{event}} | {{date}} | {{rd}} | {{time}} |

> Fill gaps from [Sherdog]({{url}}), [Tapology]({{url}}), or [UFCStats]({{url}}).

---

## Finish Rate Breakdown ({{N}} wins)

| Method | Count | % |
|--------|-------|---|
| KO / TKO | {{n}} | {{%}} |
| Submission | {{n}} | {{%}} |
| Decision | {{n}} | {{%}} |

---

## UFC Career Statistics

> Pull live numbers from [UFCStats]({{url}}). Note sample size if small.

| Stat | Value | Notes |
|------|-------|-------|
| Significant Strikes Landed per Min (SLpM) | {{x.xx}} | |
| Striking Accuracy | {{%}} | |
| Significant Strikes Absorbed per Min (SApM) | {{x.xx}} | |
| Striking Defense | {{%}} | |
| Takedown Average (per 15 min) | {{x.xx}} | |
| Takedown Accuracy | {{%}} | |
| Takedown Defense | {{%}} | |
| Submission Average (per 15 min) | {{x.xx}} | |
| Average Fight Time | {{mm:ss}} | |

---

## Fighting Style

**{{one-line archetype, e.g. "Wrestling-based pressure fighter"}}**

{{2–4 sentences on how this fighter wins and the fight they want.}}

### Grappling
- {{notes}}

### Striking
- {{notes}}

### Cardio
- {{notes}}

---

## Strengths

| Strength | Rating (1–10) | Notes |
|----------|--------------|-------|
| {{skill}} | **{{n}}** | {{notes}} |

---

## Weaknesses

| Weakness | Risk Level | Notes |
|----------|-----------|-------|
| {{weakness}} | **{{Low/Med/High}}** | {{notes}} |

---

## Skill Ratings (for the prediction model)

> These feed `analysis/mma-fight-prediction.md`. Rate 1–10.

| Skill Area | Rating |
|------------|--------|
| Boxing | {{n}} |
| Kickboxing / Muay Thai | {{n}} |
| Wrestling (offense + defense) | {{n}} |
| Jiu-Jitsu / Submissions | {{n}} |
| Chin / Durability | {{n}} |
| Cardio / Endurance | {{n}} |
| Fight IQ / Adaptability | {{n}} |

---

## Situational Flags

> Check `sports/ufc/overview.md` (Step 4) for impact. Tick any that apply to the next bout.

- [ ] Short-notice replacement (<2 weeks)
- [ ] Missed weight / hard cut history
- [ ] Long layoff (12+ months)
- [ ] Moving up a weight class
- [ ] Moving down a weight class
- [ ] UFC debut
- [ ] On a 2+ fight losing streak
- [ ] Coming off a war / hard KO loss

---

## Betting Profile

### When to back

| Scenario | Lean |
|----------|------|
| {{scenario}} | **{{Back / Strong back}}** |

### When to fade

| Scenario | Lean |
|----------|------|
| {{scenario}} | **{{Fade / Neutral}}** |

### Method of Victory Markets
- **Submission**: {{note}}
- **KO/TKO**: {{note}}
- **Decision**: {{note}}

---

## Power Rating

| Category | Score (1–10) |
|----------|-------------|
| Overall | **{{n}}** |
| vs. Wrestlers | **{{n}}** |
| vs. Strikers | **{{n}}** |
| vs. Grapplers | **{{n}}** |
| 3-round fights | **{{n}}** |
| 5-round fights | **{{n}}** |
| As underdog | **{{n}}** |
| As favorite | **{{n}}** |

---

## Sources
- [UFC Athlete Page]({{url}})
- [UFCStats]({{url}})
- [Sherdog]({{url}})
- [Tapology]({{url}})
- [ESPN]({{url}})
