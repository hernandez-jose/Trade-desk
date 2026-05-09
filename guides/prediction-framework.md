# Pick Decision Framework — Who to Bet On

This is the master process to follow every time you are asked "should I bet X?" or "who should I bet on for [game]?". Follow every step in order. Do not skip steps. At the end, issue a clear verdict: **BET / PASS / FADE / WAIT**.

---

## The 9-Step Pick Process

### Step 1: Build the Power Rating Line

Before looking at Klashi's number, generate your own estimated spread.

**Formula:**
```
My Line = (Home Team Rating + Home Field Advantage) − Away Team Rating
```

**Home field advantage by sport:**
| Sport | Home Advantage |
|-------|---------------|
| NFL   | +2.5 points (varies by stadium — Arrowhead, Seattle +3.5) |
| NBA   | +3.0 points  |
| MLB   | +0.3 runs    |
| NHL   | +0.15 goals  |
| Soccer (major leagues) | +0.25 goals |

**Power rating calculation (simplified):**
```
Rating = Avg Points Scored per Game − Avg Points Allowed per Game
Weighting: Last 4 games count 2x vs. season average
Adjust: +1 point for rest advantage, −1 for short rest
```

**NFL Rating Tiers (reference scale):**
| Tier | Rating Range | Example Teams |
|------|-------------|---------------|
| Elite | +6 to +10 | Championship-caliber |
| Above avg | +2 to +5 | Playoff teams |
| Average | −1 to +1 | .500 range |
| Below avg | −2 to −5 | Losing record |
| Bad | −6 or lower | Bottom 5 |

**Line building example:**
```
Chiefs power rating: +7.5 | Raiders: −3.0
Chiefs hosting Raiders → My line: (7.5 + 2.5) − (−3.0) = 13.0
Klashi posts Chiefs −10 → I have +3 edge on Chiefs side → BET
Klashi posts Chiefs −14 → I have −1 edge → no bet, or lean Raiders
```

---

### Step 2: Compare Your Line to the Posted Line

```
Edge = Your Line − Klashi's Posted Line (positive = value on favorite side)
```

| Edge | Action |
|------|--------|
| ≥ +3 pts | Strong bet on favorite side (2 units) |
| +1 to +2.9 pts | Standard bet on favorite side (1–1.5 units) |
| +0.5 to +1 pt | Marginal — 0.5 unit or pass |
| Within 0.5 pts either way | **PASS** — no model edge |
| −1 to −2.9 pts | Standard bet on underdog side |
| ≤ −3 pts | Strong bet on underdog side |

**Convert edge to EV:**
```
EV = (True Win % × Profit) − (True Loss % × Stake)

If true win % = 55%, odds = −110:
  EV = (0.55 × $100) − (0.45 × $110) = $55 − $49.50 = +$5.50 per $110 risked
  → +EV, bet it
```

**Rule of thumb:** Only bet if true win probability exceeds implied probability by at least 2%.

---

### Step 3: Read the Line Movement

**Questions to answer:**
1. Where did this line open?
2. Where is it now?
3. What percentage of bets are on each side?
4. Is there Reverse Line Movement?

**Decision matrix:**

| Line Movement | Public % on Favorite | Signal | Action |
|---------------|----------------------|--------|--------|
| Toward favorite | >60% on favorite | Public-driven | No sharp signal |
| Toward favorite | <50% on favorite | **Sharp on favorite** | Confirm, bet favorite |
| Toward underdog | >60% on favorite | **Sharp on underdog (RLM)** | Bet underdog |
| Toward underdog | <50% on favorite | Public reversal | Neutral |
| No movement | Any | Balanced market | Trust your model |

**Steam move rule:**
- Line moves 1+ point in under 5 minutes with no news = steam move
- A syndicate hit multiple books simultaneously
- Bet the same direction on Klashi immediately — arbs close in 1–15 minutes on major markets

**Optimal bet timing:**
| When | Who Bets | Action |
|------|----------|--------|
| Line release (Mon AM for NFL) | Sharps only | Best time to follow sharp moves |
| Tue–Wed | Mixed | Follow confirmed RLM |
| 2–3 hrs before game | Public floods in | Best time to fade the public |
| 30–60 min before | Heavy public | Fade maximally inflated lines |
| 30 min before tip (NBA) | Late info | Watch for lineup scratches |

---

### Step 4: Injury Impact Assessment

**Impact reference:**

**NFL:**
| Position | Line Adjustment |
|----------|----------------|
| Starting QB | 7–14 points — re-evaluate entirely |
| Left tackle | 2–3 points |
| WR1 / TE1 | 1–2 points |
| Bell-cow RB | 1–2 points |
| CB1 vs. elite WR | 1–2 points |
| Elite pass rusher | 1 point |

**NBA:**
| Position | Line Adjustment |
|----------|----------------|
| Star (25+ PPG) | 8–12 points |
| Star (18–24 PPG) | 4–6 points |
| Starting PG | 2–4 points |
| Starting C (anchor) | 2–3 points |
| Key rotation player | 1–2 points |

**MLB:**
| Factor | Impact |
|--------|--------|
| Starting pitcher change | Entire bet — recalculate from scratch |
| Closer unavailable | Affects save situation and totals |
| Cleanup hitter out | Moderate — affects run scoring |

**Soccer:**
| Player | Impact |
|--------|--------|
| Starting GK change | High — clean sheet probability drops sharply |
| Main striker out | Reduces scoring probability 15–20% |
| Creative midfielder | Reduces chance creation significantly |

**Timing edge — act here:**
```
Injury announced → Klashi not yet adjusted → BET immediately
Klashi partially adjusted → Small edge remains
Klashi fully adjusted → No injury edge, ignore it
```

**Checklist before any bet:**
- [ ] Starting pitcher confirmed (MLB)?
- [ ] QB confirmed healthy (NFL)?
- [ ] Star players active (NBA, Soccer)?
- [ ] Any game-time decisions that would flip the pick?
- [ ] Does Klashi's line reflect the known injury already?

---

### Step 5: Situational Angle Check

Each confirmed angle stacks onto your edge. Count how many apply.

**NFL:**
| Spot | Angle | ATS Edge |
|------|-------|----------|
| Off bye week | Bet the rested team | +2–3% |
| Short rest (Thu after Mon) | Fade the tired road team | +2% |
| Look-ahead game | Fade team with bigger game next week | +1.5% |
| Letdown after emotional upset | Fade the team | +1.5% |
| Revenge game (lost by 14+ to this opp earlier) | Lean revenge team | +1% |
| Division underdog at home | Cover historically | +2% |
| West coast team, 1pm ET kickoff | Fade the traveler | +1% |
| Divisional underdog short-week road | Fade the dog | +1% |

**NBA:**
| Spot | Angle | Value |
|------|-------|-------|
| 4th game in 5 nights | Under lean, fade the team | High |
| Star on load management (b2b) | Fade the team hard | High |
| Back-to-back road game | Bet home team | Moderate |
| Team resting stars publicly | Public still bets them — fade | High |

**MLB:**
| Spot | Angle | Value |
|------|-------|-------|
| Ace facing cold lineup (late season) | Lean under | Moderate |
| Bullpen game vs. true ace | Over lean in mid-innings | Moderate |
| 7+ games straight, offensive team | Over lean | Low |
| West coast team at 4pm ET start | Lean home dog | Moderate |

**Angle stacking rule:**
- 1 angle confirmed: +1% to true win probability estimate
- 2 angles on same team: +2–3% cumulative
- 3+ angles stacking: Strong signal, bet the max for that edge level

---

### Step 6: Weather Impact (Outdoor Sports Only)

**NFL — Total adjustment table:**
| Wind Speed | Total Adjustment |
|------------|-----------------|
| 0–10 mph | 0 |
| 11–15 mph | −0.5 |
| 16–20 mph | −1.5 |
| 21–25 mph | −2.5 |
| 26–30 mph | −3.5 |
| 30+ mph | −5.0+ |

| Temperature | Total Adjustment |
|-------------|-----------------|
| 50°F–70°F | 0 |
| 35°F–49°F | −0.5 |
| 25°F–34°F | −1.5 |
| Below 25°F | −2.5+ |

| Precipitation | Total Adjustment |
|---------------|-----------------|
| Light rain | −0.5 |
| Heavy rain | −1.5 to −2.0 |
| Light snow | −1.0 |
| Heavy snow | −2.0 to −3.0 |

**Stack all applicable modifiers.** If combined weather drops total by 4+ points and Klashi only moved 1.5 → strong under.

**MLB Wind:**
| Condition | Lean |
|-----------|------|
| Wind blowing OUT to CF/alleys, >12 mph | Over |
| Wind blowing IN from CF, >12 mph | Under |
| Coors Field + wind out | Very strong over (+2–3 runs) |
| Wrigley Field — always check | Can flip entire total |
| Temp <50°F | Under (ball doesn't carry) |
| Temp >90°F + humidity | Slight over |

---

### Step 7: Calculate Final Edge Score

```
Edge Score (%) =
  Model edge from Step 2 (in probability %)
  + 2% if confirmed RLM or steam move (Step 3)
  + injury bonus if line not adjusted (Step 4, use impact table)
  + 1% per confirmed situational angle (Step 5)
  + weather bonus if books underadjusted (Step 6)
```

| Total Edge Score | Action | Bet Size |
|-----------------|--------|----------|
| < 1% | Pass | 0 |
| 1–2% | Marginal | 0.5 units |
| 2–4% | Standard | 1 unit |
| 4–7% | High confidence | 2 units |
| 7%+ | Max confidence | 3 units |

---

### Step 8: Kelly Criterion Sizing

```
Kelly % = (b × p − q) / b

b = net payout odds (−110 → b = 100/110 = 0.909)
p = your estimated true win probability
q = 1 − p

Use Half-Kelly to reduce variance.
```

**Quick table:**
| True Win % | Odds | Half-Kelly % | Units |
|-----------|------|-------------|-------|
| 53% | −110 | ~0.5% | 0.5 |
| 55% | −110 | ~2.75% | 1–1.5 |
| 57% | −110 | ~5% | 2 |
| 60% | −110 | ~9% (cap) | 3 (max) |
| 55% | +110 | ~7.25% (cap) | 3 (max) |
| 54% | +120 | ~5% | 2 |

**Hard limits:**
- Max single bet: 3 units
- Max simultaneous open bets: 5
- Stop for the day: −5 units
- Parlays: 0.5 units max exposure

---

### Step 9: Issue the Verdict

Use this format for every pick recommendation:

```
═══════════════════════════════════════
PICK: [Team] [Spread/ML/Total] @ [Odds]
UNITS: [X] | PLATFORM: Klashi
CONFIDENCE: [Low / Standard / High / Max]
═══════════════════════════════════════

MODEL EDGE:
  My line: [X] | Klashi: [Y] | Edge: [Z] pts

LINE SIGNAL:
  Opened: [X] | Current: [Y]
  Public %: [X]% on [team]
  Movement: [Sharp/Public/RLM/Steam]

INJURIES: [Clear / Key concern: name, position, impact]

SITUATIONAL: [Spots confirmed — list each]

WEATHER: [N/A or adjustment applied]

FINAL EDGE: ~[X]% → [X] units

CLV TARGET: Expect line to close at [X] — get in before then

VOID IF: [Condition that cancels pick — e.g., "if [player] ruled out"]
═══════════════════════════════════════
```

---

## Quick-Reference Signal Cheat Sheet

### Bet (Green Lights)
- Model line is 2+ points better than posted line
- Confirmed RLM — line moves opposite to heavy public %
- Steam move — 1+ point in <5 minutes, no news
- Key opponent injury, Klashi line not yet adjusted
- 2+ situational angles stacking on same side
- Odds boost on a pick you already like

### Pass (No Bet)
- Model line within 0.5 pts of Klashi's line
- Public hammering a team, line following — no sharp counter
- Injury already fully priced in by Klashi
- Juice is −130 or worse with no overwhelming edge
- More than 2 legs in a parlay without independent +EV on each
- Already down 5 units today

### Fade (Bet the Other Side)
- 60%+ of public on one side AND line doesn't follow (RLM) → bet the other side
- Star load management game — public on the name, line inflated → fade
- Emotional favorite after a big win → letdown spot → fade
- Look-ahead trap — big game next week, inferior opponent this week → fade

### Wait (Gather More Info First)
- Game-time injury decision not yet resolved
- Starting pitcher not confirmed (MLB)
- Line moving rapidly — wait for it to settle before committing
- Weather forecast update expected closer to game time

---

## Decision Tree (Visual)

```
START: Game I'm considering
│
├─ Step 1: Build my line
│    └─ Compare to Klashi's posted line
│         ├─ Edge < 0.5 pts → PASS
│         └─ Edge ≥ 0.5 pts → Continue
│
├─ Step 2: Check injuries
│    └─ Key player out, line unadjusted?
│         ├─ YES → Bet adjusted side immediately
│         └─ NO → Continue
│
├─ Step 3: Check line movement
│    └─ RLM or steam confirmed?
│         ├─ YES → Confirms edge or creates edge → Continue
│         └─ NO → Check situational angles
│
├─ Step 4: Count situational angles
│    └─ 2+ stacking on same side?
│         ├─ YES → Strong signal → Continue
│         └─ NO → Marginal, reduce size
│
├─ Step 5: Weather (outdoor only)
│    └─ Weather under-adjusted by Klashi?
│         ├─ YES → Add weather edge → Continue
│         └─ NO → Continue
│
├─ Step 6: Calculate Edge Score
│    └─ Edge ≥ 2%? → BET (Kelly sized)
│         Edge 1–2%? → 0.5 units only
│         Edge < 1%? → PASS
│
└─ FINAL: Issue verdict using Step 9 template
```
