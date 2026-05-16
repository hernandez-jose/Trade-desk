# AI Agent Playbook — Restaurant Back Office

The single biggest advantage an independent restaurant has in 2025–2026 over a poorly managed competitor is a lean AI-augmented back office. California's labor costs make this mandatory, not optional. This playbook covers every domain where an AI agent can replace or substantially reduce headcount.

---

## Philosophy

The goal is not to eliminate humans — it's to redirect human attention to what AI cannot do: hospitality, creativity, relationship-building with regulars, vendor negotiations, and intuitive quality control. Every hour a manager spends on scheduling, invoicing, or posting Instagram content is an hour not spent on the floor improving the guest experience.

**Target state:** One owner-operator can run a ghost kitchen or small fast casual end-to-end with 2–4 part-time employees in the launch phase, using AI for everything else.

---

## Domain 1: Accounting & Bookkeeping

**Traditional cost:** $1,200–$2,500/month for part-time bookkeeper
**AI-augmented cost:** $200–$400/month in software

### Stack
- **QuickBooks Online** ($80–$200/mo) — Core accounting; integrates with POS systems
- **Dext / Hubdoc** ($50/mo) — AI receipt and invoice scanning; photos of receipts auto-categorize into QuickBooks
- **Claude API custom pipeline** — Weekly P&L summaries in plain English; flag anomalies (food cost spike, unusual vendor charges); generate reports for accountants

### What the AI Does
- Categorizes every transaction automatically
- Reconciles bank statements weekly
- Generates weekly food cost reports: actual vs. budgeted
- Emails the owner a plain-English Monday morning summary: "Food cost this week was 34.2% — 2.1% over target. The variance is in your meat purchases. Three vendors increased prices."
- Generates quarterly tax prep files; CPA reviews, doesn't rebuild

### What Still Needs a Human
- Annual tax filing (CPA, ~$2,000–$4,000/year)
- Strategic financial decisions
- Vendor contract negotiation

---

## Domain 2: Scheduling & Labor Management

**Traditional cost:** Manager time (5–8 hrs/week) + overtime mistakes
**AI-augmented cost:** $80–$150/month

### Stack
- **7shifts** ($80–$150/mo for small team) — AI-powered scheduling with sales forecasting
- **Homebase** (free–$100/mo) — Alternative; simpler UI; strong for small teams

### What the AI Does
- Ingests historical sales data and builds next week's schedule automatically
- Accounts for California meal/rest break rules (auto-flags potential violations)
- Sends shift reminders and fills open shifts via text automatically
- Tracks hours in real time; alerts owner when someone is approaching overtime
- Integrates with payroll (Gusto, ADP) to auto-calculate checks

### California-Specific Rules the AI Enforces
- 30-min meal break before 5th hour of work
- 10-min rest break per 4 hours
- Overtime after 8 hrs/day (not just 40 hrs/week — California is daily OT)
- Split shift premium pay
- 3-day advance scheduling notice (not yet state law but monitor local ordinances)

### Claude API Enhancement
Build a simple Claude API call that takes the week's schedule + sales forecast and outputs a daily briefing for the shift manager: "Thursday lunch expects 85 covers based on last 4 Thursdays. Schedule 2 line cooks and 3 front-of-house. Historical overtime risk: low."

---

## Domain 3: Inventory & Food Cost Control

**Traditional cost:** 3–5 hrs/week of manual counting + guesswork
**AI-augmented cost:** $150–$300/month

### Stack
- **MarketMan** ($150–$300/mo) — Integrates with POS; tracks every ingredient used per dish; alerts to variance
- **BlueCart** ($free–$100/mo) — AI-powered ordering; sends purchase orders to vendors automatically when stock hits reorder points
- **Craftybase** (alternative for simpler operations) — Lighter weight, lower cost

### What the AI Does
- Maps every menu item to its ingredient list (recipe costing)
- After each day's sales (from POS), calculates theoretical food usage
- Weekly inventory count takes 20 minutes; AI compares actual vs. theoretical and flags waste/theft
- Automatically generates purchase orders for approved vendors when stock hits par levels
- Tracks vendor price changes and surfaces cheaper alternatives

### The Food Cost Loop
```
POS sale data → AI calculates theoretical usage
Physical count → AI calculates actual usage
Variance → AI flags: waste, theft, or portion drift
Purchase orders → AI auto-sends to vendors at par levels
Vendor invoices → AI reconciles against orders
```

### Claude API Enhancement
Weekly food cost briefing: "Your burger yield variance is 8% — above the 3% threshold. Either portion size has drifted or you're seeing prep waste. Recommend a line check this week." These insights would cost $500+/month from a food cost consultant.

---

## Domain 4: Customer Service & Reservations

**Traditional cost:** Phone answering, reservation management, FAQ responses
**AI-augmented cost:** $50–$200/month

### Stack
- **OpenTable / Resy** ($250–$600/mo) — Reservation management with AI-optimized table turns
- **Yelp Reservations** (lower cost alternative) — ~$200/mo
- **Custom AI chatbot** (built on Claude API) — Handles FAQs, catering inquiries, hours, menus via website chat and SMS
- **Google Business Profile auto-responses** — AI drafts responses to all reviews within 24 hours (owner approves before posting)

### What the AI Does
- Answers "Are you open on Memorial Day?", "Do you have vegan options?", "What's your catering minimum?" automatically 24/7
- Qualifies catering leads: collects event date, guest count, budget, and delivers a PDF quote
- Responds to 1–3 star Yelp/Google reviews with empathetic, brand-consistent language (draft for owner approval)
- Sends automated reservation reminders + day-of SMS confirmations
- Post-visit: sends review request SMS 2 hours after reservation

### Claude API Catering Quote Pipeline
1. Customer fills out catering form on website
2. Claude API processes: generates itemized quote, estimates food cost, checks calendar for conflicts
3. Sends professional PDF quote within 5 minutes, 24/7
4. Follow-up email at 48 hours if no response

This alone can close more catering revenue than a human could, especially after business hours.

---

## Domain 5: Marketing & Content

**Traditional cost:** $1,500–$3,000/month for marketing agency or social media manager
**AI-augmented cost:** $200–$500/month in tools + 3–4 hrs/week owner time

### Stack
- **Claude API** — Content generation engine
- **Buffer / Later** ($18–$80/mo) — Social media scheduling
- **Canva** ($13–$55/mo) — AI-assisted graphic design; brand templates
- **ElevenLabs** ($5–$44/mo) — AI voiceover for short video ads
- **CapCut** (free) — AI video editing for Reels/TikTok

### Weekly AI Content Pipeline
**Monday (15 min):**
- Owner photographs 3–5 dishes / behind-the-scenes moments during the week

**Tuesday (30 min with AI):**
- Feed photos + weekly specials to Claude API
- Claude generates: 3 Instagram captions, 2 TikTok scripts, 1 email newsletter draft, 2 Google post updates, 5 Story text overlays
- Owner edits for voice (10 min)
- Upload to Buffer for scheduled posting

**Monthly (1 hour):**
- Claude analyzes which posts drove the most engagement (feed in analytics data)
- Generates next month's content calendar with topics prioritized by what worked

### Email Marketing
- **Klaviyo or Mailchimp** ($0–$100/mo) — Segmented email lists
- AI generates: weekly specials email, monthly newsletter, re-engagement for lapsed customers, post-visit thank you
- Automated flows: welcome series, birthday offer, 60-day lapse winback

### Ad Creative (Meta / Google)
- Claude API generates 10 ad copy variations per campaign
- A/B test; pause underperformers weekly
- Budget: $500–$1,500/month on paid social in launch phase; scale what works

---

## Domain 6: Menu Engineering

**Traditional cost:** $500–$2,000 for a menu consultant
**AI-augmented cost:** Free (part of POS + QuickBooks data you already have)

### The Menu Engineering Matrix
Every dish falls into one of four quadrants:

| | High Profit Margin | Low Profit Margin |
|---|---|---|
| **High Popularity** | Stars ⭐ — Feature prominently | Plowhorses 🐴 — Reprice or reformulate |
| **Low Popularity** | Puzzles 🧩 — Reposition or promote | Dogs 🐕 — Remove |

### Claude API Menu Analysis Pipeline
Monthly, feed into Claude:
- Sales volume by item (from POS)
- Food cost by item (from MarketMan)
- Contribution margin by item

Claude outputs:
- Full quadrant classification of every menu item
- Specific recommendations: "Your truffle fries are a Star — add a photo to menu and feature in social. Your salmon dish is a Dog — food cost is 42%, it sold 8 times in 30 days. Remove or reprice by $4."
- Seasonal swap suggestions based on commodity price trends

### Pricing Strategy
- CA menu pricing is typically 15–25% above national averages — price to San Jose, not to the country
- Use psychological pricing ($18.95 feels less than $19; menus without $ signs increase spend by ~8%)
- AI can draft seasonal price adjustment memos when commodity costs spike

---

## Domain 7: Compliance & HR

**Traditional cost:** HR consultant or errors that become PAGA lawsuits
**AI-augmented cost:** $50–$200/month

### Stack
- **Gusto** ($80–$200/mo) — Payroll + HR compliance automation; built for California
- **Trainual** ($50–$150/mo) — AI-powered employee training documentation
- **Poster Elite** ($30/mo) — Ensures all required posting compliance

### What the AI Does
- Gusto auto-calculates California daily OT, split shift premiums, paid sick leave accrual
- Generates offer letters, I-9 workflows, onboarding checklists
- Trainual: build your SOPs once (with Claude's help), employees train on-demand on their phones
- Sends reminders for food handler card renewals, alcohol training (RBS) renewals

### SOP Generation with Claude
Use Claude to write your standard operating procedures from a bullet-point brain dump:
- Opening checklist
- Closing checklist
- Food safety protocols (HACCP)
- Customer complaint handling
- Cash handling
- Line cook station setup

This documentation protects you in PAGA litigation and reduces training time from days to hours.

---

## Domain 8: Analytics & Reporting

**Traditional cost:** Manual spreadsheets, guesswork
**AI-augmented cost:** Already covered in stacks above

### Daily Dashboard (automated)
Built from POS + QuickBooks integrations:
- Yesterday's revenue vs. same day last week/last year
- Running food cost %
- Labor cost % for the week
- Top 5 selling items
- Delivery platform performance breakdown

### Weekly Report (Claude API generates, owner reads Monday morning)
- "Revenue was $18,400, up 12% vs. last week. Food cost held at 29.8%. Labor spiked to 38% Tuesday due to a slow dinner; consider cutting one FOH position on Tuesday nights. Your DoorDash orders are growing but at 28% commission they're your lowest-margin channel — consider pushing customers to your direct ordering link."

### Monthly Strategic Report
- Menu engineering analysis
- Cohort analysis of new vs. returning customers
- Catering pipeline and conversion rate
- Comparison to break-even targets

---

## Full AI Stack Cost Summary

| Tool | Monthly Cost |
|---|---|
| QuickBooks Online | $90 |
| Dext (receipt scanning) | $50 |
| 7shifts (scheduling) | $100 |
| MarketMan (inventory) | $200 |
| BlueCart (ordering) | $50 |
| OpenTable / Resy | $300 |
| Claude API (custom pipelines) | $50–$150 |
| Buffer (social scheduling) | $30 |
| Canva Pro | $20 |
| Gusto (payroll/HR) | $120 |
| Trainual | $75 |
| Mailchimp / Klaviyo | $50 |
| **TOTAL** | **$1,135–$1,235/month** |

**What this replaces:** $6,000–$10,000/month in traditional back-office staffing.

---

## Implementation Roadmap

### Before Opening (Months 1–3)
- [ ] Set up QuickBooks + Dext
- [ ] Set up Gusto; load all California compliance settings
- [ ] Choose and configure POS (Toast recommended; deep integrations)
- [ ] Build Claude API account; start with weekly food cost summary script
- [ ] Write SOPs using Claude; load into Trainual

### At Opening (Month 1)
- [ ] Connect POS → QuickBooks → MarketMan
- [ ] Launch social media AI content pipeline
- [ ] Deploy catering quote chatbot on website
- [ ] Set up Google/Yelp auto-response drafts

### 90 Days Post-Open
- [ ] First menu engineering analysis with 90 days of real data
- [ ] Refine scheduling model with actual traffic patterns
- [ ] Optimize delivery platform mix based on margin data
- [ ] Launch email marketing to collected customer list
