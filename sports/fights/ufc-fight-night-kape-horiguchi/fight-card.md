# {{Event}} — Main Card Fighter Index

> **Event:** {{matchup name}} ({{Event number}})
> **Date:** {{Month Day, Year}} | **Venue:** {{arena, city, state/country}}
> **Broadcast:** {{network / PPV}} | **Main Card Start:** {{time ET}}
> **Combat Sport:** Mixed Martial Arts
> **Last updated:** {{Month Year}}

> **Template usage:** Copy this whole `_TEMPLATE/` folder to `sports/fights/<event-slug>/` (e.g. `ufc-329/`). This file is the bout index — it links each fighter to their evergreen profile in `sports/ufc/fighters/`. Delete this usage block in the real file.

---

## Main Card Bouts

### Bout 1 — Main Event | {{Division}} ({{lbs}} lbs) | {{3/5}} Rounds

| | Fighter | Record | Ranking | Profile |
|---|---------|--------|---------|---------|
| 🔴 | **{{Fighter A}}** | {{W–L}} | {{rank}} | [View](../../ufc/fighters/{{a-slug}}.md) |
| 🔵 | **{{Fighter B}}** | {{W–L}} | {{rank}} | [View](../../ufc/fighters/{{b-slug}}.md) |

**Stakes:** {{title implications, layoff, debut, rematch, etc.}}

---

### Bout 2 — Co-Main Event | {{Division}} | {{3/5}} Rounds

| | Fighter | Record | Ranking | Profile |
|---|---------|--------|---------|---------|
| 🔴 | **{{Fighter A}}** | {{W–L}} | {{rank}} | [View](../../ufc/fighters/{{a-slug}}.md) |
| 🔵 | **{{Fighter B}}** | {{W–L}} | {{rank}} | [View](../../ufc/fighters/{{b-slug}}.md) |

**Stakes:** {{...}}

---

> Repeat a Bout block for every fight on the card (main card + notable prelims).

## Card Map

| Slot | Bout | Division | Rounds | Deep research |
|------|------|----------|--------|---------------|
| Main Event | {{A}} vs. {{B}} | {{div}} | 5 | [research](research/{{a-slug}}.md) · [research](research/{{b-slug}}.md) |
| Co-Main | {{A}} vs. {{B}} | {{div}} | 3 | … |

> Next steps: deep research per fighter → `fight-analysis.md` (predictions + 🏆 who-wins table) → `final-bets.md` (action sheet). See `sports/ufc/RESEARCH-WORKFLOW.md`.
