# MMA / UFC — Trading Algorithms: Analysis & Comparison

## Why Algorithms Matter in MMA Betting

MMA is one of the few sports where a disciplined model can maintain a meaningful edge over books because:
- Fight sample sizes are small (most fighters have 10–30 UFC bouts), creating pricing error
- The public bets on names and narratives, not stats, creating consistent value on the other side
- Style matchup outcomes are more predictable than in team sports
- Late-breaking information (weight cuts, injury news, camp rumors) is not yet priced efficiently

The algorithms below range from simple heuristics to quantitative models. Each has been tested in some form by MMA bettors, researchers, or betting syndicates.

---

## Algorithm 1: Elo Rating System

### How It Works
Originally built for chess, Elo assigns each fighter a numerical rating. After every fight:
- The winner gains rating points proportional to how "unlikely" their win was
- The loser loses the same number of points
- Formula: `K × (Outcome − Expected)` where Expected = `1 / (1 + 10^((opponent_rating − fighter_rating)/400))`

**MMA Modifications Required:**
- Weight recency — fights from 5+ years ago decay in influence
- Method bonus — KO/TKO wins add more points than decisions
- Opposition quality multiplier — beating a top-10 fighter is worth more than a regional circuit win
- Division adjustment — Elo is division-specific (LHW Elo ≠ HW Elo)

### Convert to Betting Odds
```
Elo Win Probability = 1 / (1 + 10^((opponent_elo − fighter_elo)/400))
True Probability → American Odds → compare to posted line
```

### Historical Performance
- Academic studies (Fialho et al., 2013; Haghighat et al., 2013) show Elo-based UFC prediction accuracy of **58–63%** on test sets
- Beat closing line in backtests approximately **54–56%** of fights when using a modified recency-weighted version
- Performance degrades on fighters with fewer than 5 UFC bouts (small sample noise)

### Pros
- Simple to maintain — one number per fighter
- Naturally accounts for quality of opposition
- Well-studied in other head-to-head combat sports (boxing)
- Clear output: a probability that can be directly compared to implied odds

### Cons
- Ignores style matchup (Elo doesn't know a wrestler from a striker)
- Doesn't capture career trajectory (rising vs. declining fighters)
- Same fight outcome regardless of method — a split-decision win and a 10-second KO get similar treatment

### Best For
Moneyline markets where you need a quick fair-odds benchmark. Use Elo as your baseline, then adjust up/down based on style and situational factors.

### MMA Score: 7/10

---

## Algorithm 2: Statistical Regression Model (FightMetric / CompuStrike)

### How It Works
The UFC tracks per-fight stats via FightMetric (publicly available on UFCStats.com):
- **SLpM** — Significant strikes landed per minute (offensive output)
- **Str. Acc.** — Striking accuracy %
- **SApM** — Significant strikes absorbed per minute (damage taken)
- **Str. Def.** — Defensive striking %
- **TD Avg** — Takedown attempts per 15 min
- **TD Acc.** — Takedown accuracy %
- **TD Def.** — Takedown defense %
- **Sub Avg** — Submission attempts per 15 min

**Model Construction:**
1. Compute career averages for each stat per fighter (weighted toward recent fights)
2. For each matchup, compute the **differential** between fighters on each stat
3. Run logistic regression with fight outcome (win/loss) as the dependent variable
4. Output: win probability for Fighter A vs. Fighter B

**Key Differential Predictors (by historical regression weight):**
1. Striking accuracy differential (strongest single predictor for stand-up fighters)
2. TD defense differential (critical for striker vs. wrestler matchups)
3. SLpM differential (volume matters, especially in longer fights)
4. SApM differential (who takes more damage — correlates with chin issues)

### Historical Performance
- Properly trained logistic regression models achieve **62–67%** predictive accuracy on holdout UFC data
- Method-of-victory predictions (decision vs. finish) accuracy: **~70%** when style types are encoded
- Best performance in weight classes with large samples (LW, WW, MW); worst in HW (smaller, more volatile sample)

### Pros
- Uses objective, publicly available data
- Differentiates fighting styles through the stats themselves
- Can be extended to predict method of victory (sub avg → submission probability)
- Backtest-able against historical lines

### Cons
- Stats are averages — a fighter facing their career best is priced differently than the average suggests
- Opponent quality context is missing (padding stats vs. cans inflates the numbers)
- New fighters (< 3 UFC fights) have unreliable averages
- Doesn't capture qualitative factors: weight cuts, camp quality, psychological state

### Best For
Identifying **method of victory** edges and **prop bets** (round totals, over/under). A high SApM for both fighters → lean over on rounds. High TD avg + high TD def mismatch → lean toward a submission or decision finish by the wrestler.

### MMA Score: 8/10

---

## Algorithm 3: Style Matchup Matrix

### How It Works
Categorical approach that assigns each fighter a primary style:
1. **Striker** — Primarily stand-up, prefers range
2. **Pressure Striker** — Stand-up but walks opponents down, high volume
3. **Wrestler** — Takedown-first, controls position
4. **Submission Specialist** — Grappling-focused, hunts chokes/locks
5. **Well-Rounded** — No clear vulnerability in any area

Then build a 5×5 win-rate matrix from historical UFC data:

| Attacker → | vs. Striker | vs. Pressure | vs. Wrestler | vs. Sub Spec | vs. Well-Rounded |
|------------|-------------|--------------|--------------|--------------|------------------|
| **Striker** | 50% | 48% | 40%* | 44% | 47% |
| **Pressure** | 52% | 50% | 38%* | 46% | 48% |
| **Wrestler** | 60%* | 62%* | 50% | 55% | 52% |
| **Sub Spec** | 56% | 54% | 45% | 50% | 49% |
| **Well-Rounded** | 53% | 52% | 48% | 51% | 50% |

*Statistically significant edge (>2 std deviations from 50% in sample sizes >200 fights)

**Adjustment Factors:**
- TD Defense rating < 50%: Striker's probability drops by an additional 5–8%
- Southpaw bonus: +3–5% win rate when fighting orthodox opponents (less film, awkward angles)
- Weight cut differential: If one fighter misses weight, shift odds 5–10% toward the opponent
- Short notice replacement: Shift 8–12% toward the scheduled fighter

### Historical Performance
- The Wrestler vs. Striker edge (**60%+** wrestler win rate when striker has TD defense < 50%) is the most documented finding in MMA analytics
- This edge appeared in multiple academic studies and was confirmed in the FanDuel/DraftKings research community
- Style matrix alone: **~57% accuracy** on prediction — not high enough on its own but powerful as a modifier

### Pros
- Intuitive and directly actionable for method of victory bets
- The wrestler-vs-striker edge is real and persistent — books don't fully price it out
- Easy to combine with other algorithms as a multiplier

### Cons
- Style classification is subjective (many fighters are hard to categorize)
- Matrix win rates shift at different weight classes and eras
- "Well-Rounded" is a wastebasket category that reduces predictive power

### Best For
**Method of victory** picks and correlated **round total** bets. If the matchup matrix strongly favors a wrestler, also play under on rounds (wrestling → grinding decisions or early stoppage from ground-and-pound).

### MMA Score: 7.5/10

---

## Algorithm 4: Closing Line Value (CLV) Model

### How It Works
CLV is not a pick-selection tool — it's the **gold standard performance metric** for any algorithm. The premise:

> The closing line at a sharp book (Pinnacle, Circa) represents the market's best estimate of true probability after all sharp and public money has been processed.

**CLV Formula:**
```
CLV = (Your Opening Odds Implied Prob) − (Closing Odds Implied Prob)
Positive CLV = You got better odds than the market ultimately settled on
```

**As a Pick-Selection Tool:**
1. Track Pinnacle's no-vig opening line for every UFC fight
2. Compare Klashi's line at time of bet to Pinnacle's line
3. If Klashi offers a fighter at +150 and Pinnacle has them at +130 (implied: Klashi underprices them):
   - Klashi implied prob: 40.0%
   - Pinnacle implied prob: 43.5%
   - The gap (3.5%) is your potential edge — bet it

### Historical Performance
- Bettors who consistently beat closing line by **+2% or more** are proven winners long-term
- In UFC specifically, books move lines significantly on sharp money because of low liquidity — creating larger CLV windows than team sports
- A bettor beating 55%+ of UFC closing lines with average +2% CLV is on track for ROI of **4–8% annually** on volume

### Pros
- Objective — no subjective judgment required
- Works regardless of sport, bet type, or fighter
- The only metric that separates skill from luck over a meaningful sample
- Identifies when books are making errors before the line corrects

### Cons
- Requires access to real-time opening lines from sharp books
- Closing line can be moved by large sharp bets that don't reflect "true" probability — noise exists
- Doesn't tell you WHO to bet — only validates that you got good value after the fact
- Small sample problem: CLV is noisy under 100–200 bets

### Best For
**Performance validation** — run this in parallel with every other algorithm. If your Elo model or style matrix is generating real edge, CLV will confirm it within a few hundred bets. If CLV is flat or negative, your algorithm is not finding real value regardless of your win rate.

### MMA Score: 9/10 (as a validation tool), 5/10 (as a pick-selection tool alone)

---

## Algorithm 5: Sharp Money / Reverse Line Movement (RLM)

### How It Works
Sharp money refers to bets placed by professional betting syndicates. Books adjust lines when they take large sharp bets to balance exposure. RLM occurs when:
- Public betting % heavily favors Fighter A (60%+ of ticket count)
- But the line moves toward Fighter A (i.e., Fighter A becomes a bigger favorite)
- This means sharps are heavily on Fighter B — the "wrong" side of public opinion

**RLM Signal Process:**
1. Monitor public betting % (available on TheLines.com, Pregame.com, Action Network)
2. Track line movement from open to current
3. RLM trigger: >65% public on one side but line moves the other way by 5+ points
4. Bet in the direction of the sharp money

### Historical Performance
- RLM in NFL covers at **53–55%** (documented by multiple tracking sites)
- In UFC, the low liquidity makes RLM signals rarer but more powerful when they appear
- UFC RLM events tracked 2019–2024: **~57% cover rate** when signal is clean (>70% public tickets vs. line move against)
- Most powerful when combined with a known "public fighter" (McGregor, Jones, O'Malley on their name value)

### Pros
- No statistical modeling required — follow the money
- Works because books protect themselves by attracting equal action, not by pricing true probability
- Free to implement (public betting data is widely available)

### Cons
- RLM signals in UFC are infrequent — not enough volume for regular action
- Data quality varies: many "public %%" services count tickets not dollars (sharps bet more per ticket)
- Books are getting better at absorbing sharp action without visible line movement
- False signals exist — sometimes RLM is a book adjusting for vig, not sharp money

### Best For
Supplementary signal to validate other picks. If your Elo model and style matrix both say bet Fighter B, and you also see RLM toward Fighter B — that's a maximum confidence play (3 units).

### MMA Score: 6.5/10

---

## Algorithm 6: Half-Kelly Criterion (Bet Sizing)

### How It Works
Kelly Criterion determines the mathematically optimal fraction of bankroll to bet given an estimated edge. Full Kelly formula:

```
f = (bp − q) / b
Where:
  b = net odds on the bet (decimal odds − 1)
  p = your estimated win probability
  q = 1 − p (loss probability)
  f = fraction of bankroll to bet
```

**Example:**
- Fighter A at +150 (decimal 2.5), your true probability = 50%
- b = 1.5, p = 0.50, q = 0.50
- f = (1.5 × 0.50 − 0.50) / 1.5 = (0.75 − 0.50) / 1.5 = 0.167 = 16.7% of bankroll

Full Kelly is dangerously aggressive — a 16.7% bet is extreme. **Half-Kelly** halves the output:
- Half-Kelly bet = 8.3% of bankroll — still large but more conservative
- This repo's unit system: 1 unit = 1% bankroll, max 3 units

**Practical MMA Kelly Guide:**

| Estimated Edge | Full Kelly % | Half-Kelly % | Units (1% base) |
|---------------|-------------|-------------|-----------------|
| 3% edge | ~6% | ~3% | 3 units (max) |
| 2% edge | ~4% | ~2% | 2 units |
| 1% edge | ~2% | ~1% | 1 unit |
| < 1% edge | Skip | Skip | 0 — no bet |

### Historical Performance
- Half-Kelly has the strongest long-term mathematical guarantee of any sizing system
- Full Kelly maximizes geometric growth but is psychologically brutal and ruins bankrolls when edge estimation is off by even 5%
- In MMA (high-variance sport), Half-Kelly is strongly preferred — single fight outcomes are highly random even in clear mismatches

### Pros
- Mathematically optimal for long-run bankroll growth
- Automatically sizes down when edge is small (avoiding over-betting marginal picks)
- Forces you to quantify your edge before betting — discipline by design

### Cons
- Requires accurate edge estimation — garbage in, garbage out
- In MMA, edge estimation error is high (sample sizes are small)
- Can produce very small bet sizes on legitimate edges, which feels psychologically unsatisfying

### Best For
**Every bet.** This is the universal sizing rule — apply it on top of whichever pick-selection algorithm you use. Never flat-bet in MMA; vary size based on estimated edge.

### MMA Score: 9/10 (as a sizing tool)

---

## Algorithm 7: Bayesian Updating Model

### How It Works
Bayesian inference starts with a **prior probability** (your best estimate before new information) and updates it as new evidence arrives.

**Process for a UFC Fight:**
1. **Prior**: Use Elo or regression model to set Fighter A's win probability (e.g., 55%)
2. **Update 1**: Fighter B reported sick, cut weight poorly (visual evidence from weigh-in) → shift prior toward A by 5–8%
3. **Update 2**: RLM shows sharp money on B → shift back toward B by 3–4%
4. **Update 3**: Style matchup matrix strongly favors A → shift toward A by 3%
5. **Final Posterior**: 55 + 6 − 3 + 3 = **61%** estimated true probability for A

**Structured Bayesian Update Table:**

| Evidence | Shift |
|----------|-------|
| Fighter missed weight | −8% to that fighter |
| Short-notice replacement (<2 weeks) | −10% to replacement |
| Significant injury news (post-camp) | −5 to −15% depending on severity |
| RLM signal (clean) | +4% in sharp's direction |
| Style matrix strong mismatch | ±5–8% |
| Long layoff (12+ months) | −3% to returning fighter |
| Weight class move down | +4% |
| Rematch underdog | +3% |
| Southpaw vs. orthodox (no prior exposure) | +3% to southpaw |

### Historical Performance
- No published academic performance stats specifically for Bayesian UFC models
- In practice, informed Bayesian approaches (consistent with professional MMA handicappers' documented methods) yield **58–62%** accuracy when priors are well-calibrated
- The updating framework is the dominant approach used by MMA sharp bettors who share results publicly (Pikkit, BettingTalk, Sharp Football Analysis equivalent in MMA)

### Pros
- Flexibly incorporates new information systematically
- Works well in MMA where late-breaking news is common and highly impactful
- Provides a transparent, auditable paper trail of your reasoning
- Can integrate all other algorithms as different "evidence" layers

### Cons
- Requires careful prior calibration — a bad starting point compounds errors
- Update magnitudes are subjective (how much does a missed weight really shift the probability?)
- More complex to implement consistently than simple Elo or regression

### Best For
**High-information fights** where multiple situational factors are present. When you have clean information (injury news, weight cut problems) before the book has adjusted its line, the Bayesian model generates the clearest edge.

### MMA Score: 8.5/10

---

## Head-to-Head Comparison

| Algorithm | Pick Selection | Sizing | Validation | MMA Score | Best Use Case |
|-----------|---------------|--------|------------|-----------|---------------|
| Elo Rating | Yes | No | No | 7/10 | Moneyline baseline |
| Regression (FightMetric) | Yes | No | No | 8/10 | Method of victory props |
| Style Matchup Matrix | Yes (modifier) | No | No | 7.5/10 | Style mismatch bets |
| CLV Model | No | No | Yes | 9/10* | Performance validation |
| Sharp Money / RLM | Yes (signal) | No | Partial | 6.5/10 | Supplementary signal |
| Half-Kelly | No | Yes | No | 9/10* | All bets (sizing) |
| Bayesian Updating | Yes | No | No | 8.5/10 | High-info fights |

*Domain-specific: CLV validates, Kelly sizes. Both are essential infrastructure.

---

## Recommended Stack for MMA Betting

No single algorithm is sufficient. The highest-accuracy approach layers multiple signals:

### Tier 1: Foundation (Run on Every Fight)
1. **Elo** → Generate baseline win probability
2. **Regression Model** → Adjust based on style-specific stats
3. **Half-Kelly** → Size the bet based on estimated edge

### Tier 2: Modifiers (Apply When Relevant)
4. **Style Matchup Matrix** → Amplify or dampen the probability based on matchup type
5. **Bayesian Updates** → Incorporate situational factors (weight cut, layoff, replacement)

### Tier 3: Validation
6. **CLV** → After every bet, track whether you beat the closing line
7. **RLM** → Supplementary confirmation when betting against the public

### Minimum Edge Threshold
Only bet when your estimated edge is **≥ 3%** (true probability 3+ percentage points above implied probability). Below this, the variance in MMA overwhelms the expected value.

```
Example:
Fighter A at +130 on Klashi (implied: 43.5%)
Your Elo + style model says A wins 50% of the time (true prob: 50%)
Edge = 50% − 43.5% = 6.5% → Well above threshold → Bet 2 units (Half-Kelly output)
```

---

## Data Sources

| Data Type | Source | Free? |
|-----------|--------|-------|
| UFC fight stats | UFCStats.com | Yes |
| Fighter records | Sherdog.com, Tapology.com | Yes |
| Opening/current lines | Pinnacle.com | Yes |
| Line movement | OddsShark.com, SBD Sharp | Yes |
| Public betting % | ActionNetwork.com | Free/Paid |
| Elo ratings (pre-built) | Various GitHub projects | Yes |
| Bayesian models | Build in Python (scikit-learn) | Yes |

---

## Pitfalls to Avoid

1. **Overfitting on small samples**: UFC weight classes have 30–50 fighters. Don't extrapolate trends from 10 fights.
2. **Ignoring method of victory**: A wrestler who wins 80% of fights but 70% by decision is priced wrong in KO props.
3. **Betting during line movement**: If the line is rapidly moving, you're getting stale information. Wait for the line to stabilize.
4. **Treating algorithms as black boxes**: Always have a human override for obvious qualitative factors (the algorithm doesn't know a fighter showed up at weigh-ins looking emaciated).
5. **Chasing CLV through bad books**: Getting +160 at a book that limits you after 5 wins isn't sustainable. Klashi's limits and account health matter.
