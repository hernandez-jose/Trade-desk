# Restaurant Launch Playbook — San Jose, CA

A full-stack research guide for opening a restaurant in San Jose, California, bootstrapped heavily with AI agents for back-office operations.

---

## Why San Jose?

San Jose sits at the heart of Silicon Valley — high disposable income, a fiercely tech-savvy customer base, and a deeply diverse population hungry for authentic and innovative food experiences. The same factors that make it expensive also make it forgiving: average check sizes are higher, corporate catering opportunities are massive, and delivery culture is embedded.

**Best-fit concepts for San Jose:**
- Fast-casual with premium positioning (tech workers, quick lunch)
- Ghost kitchen / virtual brand (low overhead entry point)
- Corporate catering arm attached to a small brick-and-mortar
- Authentic ethnic cuisine (Vietnamese, Indian, Mexican, Ethiopian — large diaspora communities)
- Health-forward / plant-based (strong demand in tech demographic)

---

## The 10 Stages at a Glance

| # | Stage | Timeline | Detail File |
|---|-------|----------|-------------|
| 1 | Concept & Market Research | Months 1–2 | [stages/01-concept-planning.md](stages/01-concept-planning.md) |
| 2 | Business Plan & Funding | Months 2–3 | [stages/02-business-plan-funding.md](stages/02-business-plan-funding.md) |
| 3 | Location & Lease | Months 3–5 | [stages/03-location-lease.md](stages/03-location-lease.md) |
| 4 | Permits & Licenses | Months 4–7 | [stages/04-permits-licenses.md](stages/04-permits-licenses.md) |
| 5 | Design & Build-Out | Months 5–9 | [stages/05-design-buildout.md](stages/05-design-buildout.md) |
| 6 | Equipment & Suppliers | Months 7–9 | [stages/06-equipment-suppliers.md](stages/06-equipment-suppliers.md) |
| 7 | Staffing & HR | Months 8–10 | [stages/07-staffing-hr.md](stages/07-staffing-hr.md) |
| 8 | Menu Development | Months 6–9 | [stages/08-menu-development.md](stages/08-menu-development.md) |
| 9 | Marketing & Brand | Months 7–11 | [stages/09-marketing-brand.md](stages/09-marketing-brand.md) |
| 10 | Soft Open → Scale | Months 10–12+ | [stages/10-launch-operations.md](stages/10-launch-operations.md) |

---

## Budget Summary (San Jose, CA)

Full detail in [budget-san-jose.md](budget-san-jose.md).

| Concept Type | Startup Range | Monthly Burn |
|---|---|---|
| Ghost Kitchen / Virtual Brand | $40K – $120K | $8K – $18K |
| Fast Casual (800–1,200 sqft) | $180K – $450K | $25K – $55K |
| Full-Service (1,500–2,500 sqft) | $450K – $1.2M | $60K – $130K |

> **Recommended entry path:** Ghost kitchen or fast-casual with a strong corporate catering arm. Reach profitability faster, validate the concept, then expand to a full-service location.

---

## AI Agent Stack (Back Office)

Heavy bootstrapping with AI keeps overhead lean, especially critical in California where labor costs are the #1 killer. See [ai-playbook.md](ai-playbook.md) for the full stack.

| Domain | Tool / Agent | Replaces |
|---|---|---|
| Accounting & Bookkeeping | Claude API + QuickBooks | Part-time bookkeeper |
| Scheduling | 7shifts AI | Scheduling manager |
| Inventory & Ordering | MarketMan + AI forecasting | Inventory clerk |
| Marketing Content | Claude API pipelines | Marketing agency |
| Customer Service | AI chatbot (reservations, FAQs) | Host labor hours |
| Menu Engineering | Sales data analysis via Claude | Consultant |
| Social Media | AI-generated content + human review | Social media manager |

---

## Critical Numbers to Keep Front of Mind

- **Food Cost %:** Target 28–32% of revenue
- **Labor Cost %:** Target 28–35% (California labor laws push this higher)
- **Occupancy Cost %:** Target under 10% of revenue
- **Prime Cost (Food + Labor):** Must stay under 65% to be profitable
- **Break-even:** Typically 18–24 months in the Bay Area; ghost kitchen can hit 6–12 months

---

## File Structure

```
/
├── README.md                    ← You are here (overview)
├── budget-san-jose.md           ← Full budget breakdown
├── ai-playbook.md               ← AI agent stack details
└── stages/
    ├── 01-concept-planning.md
    ├── 02-business-plan-funding.md
    ├── 03-location-lease.md
    ├── 04-permits-licenses.md
    ├── 05-design-buildout.md
    ├── 06-equipment-suppliers.md
    ├── 07-staffing-hr.md
    ├── 08-menu-development.md
    ├── 09-marketing-brand.md
    └── 10-launch-operations.md
```
