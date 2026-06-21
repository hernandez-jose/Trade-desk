# Soccer Research Methods — Complete Analytical Framework for Betting

*A quantitative analyst's guide to researching soccer matches, identifying value, and building durable edges across all major markets.*

---

## Table of Contents

1. [Key Metrics to Track](#1-key-metrics-to-track)
2. [Data Sources](#2-data-sources)
3. [Form Analysis](#3-form-analysis)
4. [Squad Analysis](#4-squad-analysis)
5. [Tactical Analysis for Betting](#5-tactical-analysis-for-betting)
6. [Set Piece Analysis](#6-set-piece-analysis)
7. [Referee Analysis](#7-referee-analysis)
8. [Weather and Venue Factors](#8-weather-and-venue-factors)
9. [Tournament-Specific Research](#9-tournament-specific-research-world-cup--major-tournaments)
10. [Pre-Match Research Checklist](#10-pre-match-research-checklist)

---

## 1. Key Metrics to Track

Soccer advanced metrics exist to separate underlying performance from noisy scoreline results. The core insight: **goals are a high-variance, low-frequency event**. Two or three matches of scorelines tell you almost nothing reliable. The underlying process — how a team creates and concedes shots, and where those shots come from — converges to truth much faster.

### 1.1 Expected Goals (xG)

**What it is**: xG assigns a probability (0.0 to 1.0) to every shot attempt based on historical data: shot location, shot type (foot vs. head), assist type (through-ball vs. cross vs. open play), and game state. A penalty = ~0.76 xG. A header from 18 yards on a cross = ~0.09 xG. An open-play tap-in from 3 yards = ~0.85 xG.

**Why it predicts outcomes**: Teams that consistently outperform their xG (i.e., score significantly more goals than their shot quality predicts) are typically getting lucky on finishing or benefiting from an elite finisher. Teams that consistently underperform are either unlucky or shooting poorly in execution. Over a season, xG is significantly more predictive of next-season goal-scoring than actual goals.

**Betting translation**:
- A team with a 1.8 xG vs. 0.6 xGA per game but a 4-4-4 scoreline record is likely to start winning; their underlying process is elite. Bet on the regression.
- A team with 0.7 xG vs. 1.5 xGA but 8-2-2 scorelines is living on luck; bet against them before the correction.
- Season-long xGD (differential) correlates ~0.72 with final league position, versus ~0.61 for goal differential.

**Critical caveats**:
- xG models differ slightly by provider (Opta, StatsBomb, Understat). Understat's model is strong for open play but slightly weaker on set pieces. StatsBomb's model (available to clubs/researchers) adds pressure variables.
- Penalties inflate xG totals without reflecting open-play quality. **Always note a team's penalty count** when reviewing xG.
- A team with a prolific world-class finisher (Lewandowski, Mbappe) legitimately outperforms xG because their finishing skill is real — don't blindly assume regression.

### 1.2 Expected Goals Against (xGA)

**What it is**: The xG of all shots the opposition has taken against a team. Reflects defensive shape quality and goalkeeper positioning (how well the defense restricts shot quality), rather than just preventing shots from happening.

**Why it matters**: Low shot volume doesn't always mean good defense. A team may give up few shots but allow many from central dangerous areas. xGA catches this. Conversely, a team may face many shots but concede from poor locations only.

**Betting translation**:
- Teams with low xGA (elite defensive structures) are significantly better bets in under 2.5 markets and clean sheet props.
- A team conceding 1.4 xGA/game but only 0.8 goals/game has a goalkeeper massively outperforming — regress goalkeeper performance, not the defense.

### 1.3 xG Differential (xGD)

**Formula**: `xGD = xG − xGA` per match, or season total.

**What it is**: The single best "power rating" number in soccer. A team with a +1.0 xGD per game creates a full expected goal more than they concede per match — elite dominance. A team at −0.3 xGD is a net weak team over time regardless of their current form or points table position.

**Betting translation**:
- xGD is the backbone of any home/away power rating. To estimate a match result, compare both teams' home/away xGD over the last 8–12 matches.
- xGD-based power ratings are more stable than Elo ratings based on results, especially mid-season.
- Corrected xGD (removing penalties and own goals) is even more stable — use it when building models.

**Quick power rating example**:

| Team | Home xGD/game | Away xGD/game |
|------|--------------|--------------|
| Team A (home) | +0.85 | +0.40 |
| Team B (away) | +0.60 | +0.20 |
| Expected match xGD | +0.85 − 0.20 = +0.65 in favor of Home | Lean home |

### 1.4 PPDA (Passes Allowed Per Defensive Action)

**What it is**: PPDA = opposition passes in the defensive half / defensive actions (tackles, interceptions, fouls) in the same area. It is the premier metric for quantifying pressing intensity.

- **Low PPDA (4–7)**: Team presses aggressively, allows very few passes per defensive action — high-energy pressing teams like Liverpool, Bayer Leverkusen, Atalanta.
- **High PPDA (10–15+)**: Team sits deep, allows many opposition passes, defends in a low block — Atletico Madrid, most defensive-leaning lower-table sides.

**Betting translation**:
- A high-press team (low PPDA) playing a team that struggles with build-up under pressure will win the positional battle. Lean on the pressing team to generate more xG.
- When a high-press team is running 4 games in 12 days: their PPDA will rise (they press less aggressively), and their xG creation typically drops 10–18%. This is exploitable in total markets.
- Tactical mismatch: a team with very strong press resistance (high "build-up under pressure" completion rates) vs. a pressing team is a neutralizer — neither side dominates, lean under.

### 1.5 Deep Completions

**What it is**: Passes completed into the opposition's box area (roughly the final third attacking zone, within 18 yards of goal). Also called "box entries" in some models.

**Why it matters**: Deep completions are a leading indicator of shot creation. Teams that consistently thread passes into dangerous areas generate higher-quality shots. The metric captures incisive combination play that doesn't always result in a shot but is part of the attack's structure.

**Betting translation**:
- Teams with high deep completions but middling xG are typically unlucky with their final ball or shot selection — they're creating structure without converting it to shots yet. This often corrects.
- Track deep completion differential (yours vs. theirs) as a companion to xGD for a fuller picture of attacking vs. defensive dominance.

### 1.6 Progressive Passes and Progressive Carries

**What they are**:
- **Progressive pass**: A completed pass that moves the ball 10+ yards closer to the opposition goal (in the opposition half) or into the final third.
- **Progressive carry**: A ball carry that moves 5+ yards into the final third, or 10+ yards toward goal from anywhere.

Both measure how a team advances the ball toward goal — whether through passing combinations or dribbling.

**Betting translation**:
- High progressive passing teams control territory and tempo; they dictate time of possession in the attacking half. This correlates with winning the xGD battle.
- Teams with elite progressive carriers (dribble-heavy wide players) that are marked out by a disciplined defensive low block can struggle — assess whether the opposition's defensive shape neutralizes the weapon.

### 1.7 Press Resistance

**What it is**: How successfully a team passes and carries out of its own defensive third under pressure. Measured by pass completion rate when pressed, successful dribbles in own half, and goalkeeper distribution under pressure.

**Why it matters**: A team with poor press resistance will routinely give the ball away in dangerous areas when pressed. Against a high-press opponent, they may give up 5–8 short-distance xGA chances per game purely from poor build-up.

**Betting translation**:
- Poor press resistance + high-press opponent = higher match xGA for the poor-pressing team. Lean on the pressing team in 1X2 and Asian handicap markets.
- Particularly important for goalkeeper evaluation: Does the GK distribute confidently under pressure? Goalkeepers forced into long balls by poor press resistance increase their team's xGA in transition.

### 1.8 Shot Quality vs. Shot Quantity

**The distinction**: Raw shot volume tells you which team controlled play. Shot xG per shot (average shot value) tells you whether the shots were from dangerous positions.

| Team Profile | Shots/Game | xG/Shot | Total xG |
|---|---|---|---|
| High-volume, low quality | 18 | 0.06 | 1.08 |
| Low-volume, high quality | 9 | 0.13 | 1.17 |

Both teams generate similar xG, but the public will see "18 shots vs. 9 shots" and overrate the first team.

**Betting translation**:
- Teams that allow many shots from the perimeter (long-range, low xG/shot) look defensively porous in raw stats but are actually well-organized — their xGA is low.
- Teams that allow few shots from central dangerous areas (high xG/shot) have a structural problem regardless of whether goals have been conceded yet.

### 1.9 Save Percentage vs. Post-Shot xG (PSxG)

**The distinction**:
- **Save%**: Raw saves / shots on target. Simple but noisy — depends on shot quality faced.
- **Post-Shot xG (PSxG)**: xG calculated after the shot is struck, accounting for shot placement within the goal frame. A shot aimed into the top corner from 15 yards = high PSxG even if stopped.

**Why PSxG matters**: PSxG-conceded vs. goals-conceded tells you whether a goalkeeper is adding or subtracting value.

- `GK value = PSxG conceded − Goals actually conceded`
- If PSxG faced = 1.4 per game but Goals conceded = 0.9 per game: the GK is adding +0.5 goals/game of value — elite, like an Alisson or De Gea in prime form.
- If PSxG faced = 1.0 per game but Goals conceded = 1.4 per game: the GK is subtracting value — get out of clean sheet props immediately.

**Betting translation**:
- When a GK is overperforming PSxG heavily over 15+ matches, treat it as partial skill but expect partial regression. Fade clean sheet props on teams with mediocre defense propped up by a hot GK.
- PSxG overperformance that's sustained across 2+ seasons is often real (Alisson has done this historically). One-season overperformance is typically 60% luck.

### 1.10 Conversion Rate and Finishing Quality

**Non-penalty goals vs. non-penalty xG**: The ratio tells you whether a team's finishers are better or worse than average.

- Elite finisher impact: A striker consistently at 150%+ of npxG (scores 50% more goals than their shot quality suggests) is a real finishing talent — Lewandowski historically.
- Team-level conversion: Teams finishing 130%+ of npxG are typically either lucky, or have a world-class finisher. Regress toward expected without the finisher.

**Betting translation**:
- When a team's star striker is injured, their expected goal conversion drops back toward 100% of xG. This can be worth 0.3–0.5 goals/game — significant for totals markets.

---

## 2. Data Sources

### 2.1 FBref (fbref.com)

**Cost**: Free  
**Best for**: Deep per-player and per-team statistics across all top leagues; historical data back to 2017+; StatsBomb-powered underlying metrics (xG, progressive passes, pressures, PPDA)

**What's available**:
- Team stats: xG, xGA, progressive passes, shots, press stats, PPDA
- Player stats: xG, xA (expected assists), shot-creating actions, progressive carries, defensive actions
- Match logs for every game — useful for home vs. away splits
- Squad age profiles, minutes distribution

**How to use for betting**:
1. Go to the league table on FBref → click "Squad Stats" → select "Shooting" for xG data
2. Click team name → "Match Logs" → filter home/away → build your own rolling average
3. Compare xGD over last 8 games (not season total) for recency-weighted power ratings
4. Player page → "Match Logs" shows per-game xG + xA to calculate key player dependency

**Limitations**:
- Does not show live in-play data
- StatsBomb coverage includes top 5 leagues + select others; lower leagues may lack deep metrics
- UI requires practice; not beginner-friendly for building custom tables

### 2.2 Understat (understat.com)

**Cost**: Free  
**Best for**: Quick xG data per match, team season-level xG/xGA, rolling form visualization

**What's available**:
- Season-long xG and xGA for all teams in EPL, La Liga, Bundesliga, Serie A, Ligue 1, RFPL (Russian)
- Match-by-match xG timeline
- Situation breakdown: open play xG vs. set piece xG vs. counter-attack xG vs. penalty xG
- Shot map: every shot plotted on a pitch with xG value visible

**How to use for betting**:
1. Team page → scroll down to "xG Progress" chart — this shows cumulative xG vs. actual goals over the season. Divergence = regression candidate.
2. Match report → shot map: see if the team's shots are clustered in central areas (high quality) or from the perimeter (lower quality).
3. Situation tab: if a team creates 60% of xG from set pieces, they're highly set-piece dependent — significant if the opposing defender is excellent in the air.

**Limitations**:
- Limited to 6 leagues (no Champions League, no English Championship, no Portuguese/Dutch leagues on free tier)
- xG model differs slightly from FBref/StatsBomb — use for cross-referencing, not as single source of truth
- No player-level detail beyond goal/shot contributions

### 2.3 SofaScore (sofascore.com)

**Cost**: Free (app); some advanced features behind paywall  
**Best for**: Live scores, injury updates, head-to-head records, referee stats, immediate lineup notifications, real-time xG during matches

**What's available**:
- Live match tracker with event timeline, key stats, and in-play xG (basic)
- Team form tables: last 5/10 results with home/away filters
- Player ratings per match (crowd-sourced but directionally useful)
- Head-to-head records: last 10+ meetings, with venue filter
- **Referee profiles**: Fouls called/game, yellow cards/game, red cards rate, penalty rate — critical for cards and corners markets
- Standings with xG displayed for some leagues

**How to use for betting**:
1. Match preview → click "Referee" name → see that official's stats: avg cards/game, fouls/game, penalties/season
2. Team page → "Matches" tab → filter home/away → manually note last 6 results with scorelines
3. Player → "Season stats" → check injury history and availability trend

**Limitations**:
- xG model is proprietary and less sophisticated than FBref/StatsBomb — treat as a rough guide only
- Player ratings are crowd-sourced (fan-driven), not statistical — don't use for analytical purposes
- Injury info lags behind beat reporters on Twitter/X by hours

### 2.4 WhoScored (whoscored.com)

**Cost**: Free (with Opta data)  
**Best for**: Opta-powered match stats, player ratings based on statistical performance, league averages for benchmark comparison, detailed match statistics

**What's available**:
- Opta-based player ratings (statistically generated, more reliable than SofaScore)
- Match statistics: possession, shots on/off target, corners, fouls, cards, offsides
- Team tactical formations and average position maps
- League averages for all key stats — useful for benchmarking whether a metric is truly above/below average

**How to use for betting**:
1. Team page → "Detailed Stats" → compare to league averages for possession, shots on target, dribbles, aerial duels won
2. Match center → "Formation" tab → see average position of players (tells you how high the defensive line plays, how wide the fullbacks push)
3. League page → sort by clean sheet %, corners per game, fouls per game — find outlier teams for specific markets

**Limitations**:
- Full Opta data (deep metrics like PPDA, progressive passes) not available on the free site
- Slightly dated UI; navigation is cumbersome
- Less real-time than SofaScore for live data

### 2.5 Transfermarkt (transfermarkt.com)

**Cost**: Free  
**Best for**: Squad composition, player market values, age/experience profiles, contract situations, transfer news and window activity

**What's available**:
- Full squad roster with age, contract expiry, market value, nationality
- Transfer history: when players arrived, what was paid
- Injury history per player: how many games missed in prior seasons, injury type patterns
- Head coach history
- Squad comparison tool: compare average age, squad value, experience

**How to use for betting**:
1. Before major tournaments: check squad ages — very young squads tire in late knockout stages.
2. Check contract situations: a manager in final months of contract, or players in final year, can affect motivation (positively or negatively).
3. After a transfer window: use squad value change to identify teams that upgraded/downgraded significantly vs. how the market has re-priced them.

**Limitations**:
- Market values are crowd-sourced approximations, not actual transfer fees
- No performance metrics — it is a roster/value database, not an analytics tool
- Injury history is only broadly coded; doesn't indicate severity or return timeline

### 2.6 StatsBomb (statsbomb.com)

**Cost**: Paid (commercial platform); some free open-data releases via GitHub  
**Best for**: The gold standard in soccer analytics. Professional-grade data used by Premier League clubs, the FA, and national federations.

**What's available (commercial)**:
- 360 data: every player's position on the pitch at the moment of every action — not just the ball carrier
- Pressure-adjusted metrics: pass completion under high vs. low pressure; pressing efficiency
- Advanced goalkeeper metrics including sweeper-keeper actions and distribution quality
- Off-ball run data: how often players make runs without the ball, and into what spaces
- All of the above across 40+ leagues and competitions

**Free data (GitHub)**:
- StatsBomb Open Data repository contains event-level data for select competitions (FA Women's Super League, La Liga from 2004–2019, Euro matches, some World Cup data)
- Good for building your own models if you code in Python or R

**How to use for betting**:
- StatsBomb IQ (paid tool): Build custom dashboards comparing team profiles across tactical dimensions — ideal for identifying matchup edges before a Champions League fixture.
- The free open data via Python's `mplsoccer` library: Build shot maps, pressing intensity heatmaps, passing networks for historical research.

**Limitations**:
- Expensive (tens of thousands per year for full commercial access)
- For individual bettors, the free GitHub data is useful but covers limited competitions and may be outdated

### 2.7 Opta / Stats Perform (statsperform.com)

**Cost**: Paid (commercial; accessed via platforms like WhoScored, SofaScore, ESPN, BBC Sport)  
**Best for**: The underlying data engine powering most of the internet's soccer statistics. The numbers you see on major media sites are Opta numbers.

**What's available (via free consumer sites)**:
- Touch-by-touch event data for all major leagues
- Pass success rates, dribbles, aerial duels, tackles, interceptions, shots
- Goals and assists attribution
- All metrics accessed indirectly through WhoScored, SofaScore, ESPN Stats, BBC Sport

**How to use for betting (indirect access)**:
- When two sources (WhoScored and FBref) agree on a stat, that stat is highly reliable — both pull from Opta or StatsBomb respectively, but directional agreement confirms the signal.
- ESPN FC's match reports use Opta data — the possession and pass completion numbers shown on the broadcast are Opta.

**Direct paid access**: Used by betting syndicates and professional sports analytics operations. For individual bettors, the free-tier platforms are sufficient.

---

## 3. Form Analysis

### 3.1 How Many Matches of Form to Use

The question of sample size is the most important and most ignored aspect of soccer form analysis.

**The core problem**: Soccer is a low-scoring game. A team can win 3 games 1-0 while completely outplayed in all three (getting outshot 15-4, facing 1.8 xGA vs. 0.6 xG per game). Their "form" in raw terms is perfect. Their underlying trajectory is alarming.

**Minimum sample for reliability**:

| Metric | Minimum matches | Confidence threshold |
|--------|----------------|---------------------|
| Goals for/against | 15+ | High noise below this |
| xG / xGA | 8+ | Directional signal from 5 |
| PPDA (press intensity) | 5+ | Tactical pattern stabilizes quickly |
| Defensive shape (xGA/shot) | 10+ | Structure takes time to show |
| Set piece xG | 15+ | Set piece goals are very low frequency |
| Home vs. Away splits | 10+ home/away each | Small home samples mislead |

**Practical approach**: Use a **10-match rolling window** as your primary analysis period. Check the season total as context. For a team mid-season with 25+ games played, the last 10 games weighted 2x and the prior 15 games weighted 1x gives you a reasonable recency-weighted estimate.

### 3.2 Recency Weighting

Not all matches in your sample carry equal weight. Apply decay weighting:

```
Recency weight model (10-game window):

Game N (most recent):      weight = 1.0
Game N-1:                  weight = 0.95
Game N-2:                  weight = 0.90
Game N-3:                  weight = 0.85
...
Game N-9:                  weight = 0.55
```

Simplified: the most recent 3 games = ~30% of the signal; the prior 7 games = ~70%. Don't overcorrect — a team that won 7 of their last 10 and lost the last 3 is not suddenly bad. They are having a rough patch within a strong foundation.

### 3.3 Weighting Competition Quality

Not all wins are created equal. A 3-0 win against a lower-table Premier League side counts more than a 3-0 win against a League Cup third-round opponent.

**Competition quality weighting**:

| Competition | Quality multiplier | Notes |
|---|---|---|
| Champions League group/knockout | 1.3 | Elite opposition quality |
| Premier League / La Liga / Bundesliga | 1.0 | Baseline |
| Serie A / Ligue 1 | 0.95 | Slight quality discount vs. top 3 leagues |
| Europa League / Conference League | 0.75 | Mixed quality opponents |
| Domestic Cup (vs top-flight opponent) | 0.85 | Same quality, different motivation |
| Domestic Cup (vs lower-league opponent) | 0.40 | Major quality discount |
| International friendly / pre-season | 0.20 | Discard for power ratings |

**In practice**: When a team has 3 UCL wins in 10 recent games, treat their 10-game xGD as stronger than the raw number suggests.

### 3.4 Identifying "Peaking Form" in Data

A team in genuine peak form shows all of the following simultaneously:
- **xGD improving trend**: Not just a positive xGD, but the 5-game rolling xGD is higher than the 10-game rolling xGD — they're getting better.
- **PPDA decreasing**: They're pressing harder and winning the ball higher up the pitch.
- **Deep completions increasing**: More entries into dangerous areas per game.
- **Clean sheet rate elevated**: Defense compact and organized, not just goalkeeper heroics.
- **xG overperformance narrowing**: Actual goals converging toward xG suggests the hot streak is becoming a real trend, not just luck.

**Warning signals even in good form**:
- Win streak with xGD that's negative or flat: living on a hot GK and/or shooting above xG — regression imminent.
- PPDA rising over the last 5 games: pressing less aggressively, possibly due to fatigue or tactical shift — check schedule density.
- High individual xG concentrated in one player: key-player dependency risk.

### 3.5 Contextualizing a Form Run

Before acting on a form reading, verify:
1. **Who did they play?** A 4-1-5-form run against relegation-threatened opposition is different from the same run against top-half clubs.
2. **Were they at home?** Home dominance can mask away vulnerability.
3. **Were there tactical reasons for variance?** A team coming off a two-legged UCL tie may have played conservatively in one leg, suppressing their usual metrics.
4. **Injuries during the run?** A team playing their best 11 for the last 8 games after injuries resolved is a different entity from the struggling mid-season version.

---

## 4. Squad Analysis

### 4.1 Assessing Squad Depth

Depth is the risk management variable for betting on big clubs over a full season. Teams without depth become vulnerable during:
- Fixture congestion (3 games in 7 days)
- Injury crises (3+ first-team regulars out simultaneously)
- Late-season fatigue (March through May in domestic leagues)

**Depth assessment framework**:

For each starting position, answer: "If the starter is out, what does the backup offer?"

| Position | Quality gap risk | Backup quality impact |
|---|---|---|
| Goalkeeper | Low (most backups are competent) | Usually 0.1–0.2 goals/game worse for backup GK |
| Centre-back partnership | High | Loss of pairing disrupts chemistry even with quality individuals |
| Defensive midfielder | High | DM provides defensive structure; backup often inferior positionally |
| Central playmaker / #10 | Very high | Chance creation drops sharply without elite creator |
| Striker / #9 | Very high | 15–25% xG reduction without key finisher |
| Wide forward | Moderate | More coverage options typically |
| Full-backs | Moderate | Less tactical variation but less catastrophic |

**Where to find it**: FBref squad page shows minutes distribution. A team with one player playing 3,200+ minutes in a 38-game season (3,420 min theoretical max) is extremely dependent on that player's availability.

### 4.2 Rotation Risk Assessment

**What triggers rotation**:
- Fixture within 3 days of previous match (especially if previous was high-intensity)
- Manager's stated pre-match comments about "managing minutes"
- Cup competition following a difficult league fixture
- Team already qualified for/eliminated from competition (no motivation)

**How to quantify rotation risk**:
1. Count days since last match: <3 days = high rotation risk; 3–5 days = moderate; 6+ days = likely first choice.
2. Check if the last game was 120 minutes (extra time) — extreme fatigue signal.
3. For Champions League clubs: league game between UCL legs is the prime rotation spot. Book often fails to fully adjust.

**The betting angle**: When a +EV side on paper is likely to rotate, recalculate their expected xG at 75% of full-strength output. If the edge disappears, don't bet.

### 4.3 Youth Integration Impact

Young players (U21) entering rotations affect team performance in measurable ways:
- **Positive**: High energy, no fatigue accumulation, press harder (PPDA often improves with youth infusion)
- **Negative**: Decision-making errors, higher card rate, less positioning discipline

**Impact by position**:

| Position | Youth impact risk |
|---|---|
| Goalkeeper | High negative — decision-making is critical |
| Centre-back | High negative — reading of the game most important |
| Wide forward / winger | Low negative / positive — athleticism matters more |
| Striker | Moderate — finishing ability often present in youth |
| Defensive midfielder | High negative — positional demands are complex |

**Data to look for**: FBref age distribution for the starting lineup. A starting 11 averaging under 23.5 years old will underperform their underlying quality metric in high-pressure environments.

### 4.4 Key Player Dependency: xG Without the Striker

The most exploitable squad analysis finding for betting: teams where one player drives a disproportionate share of xG.

**How to measure it**:
1. FBref → Team → Player stats → filter to forwards
2. Note: what % of the team's total non-penalty xG comes from one player?

| Dependency level | Top player's share | Vulnerability |
|---|---|---|
| Low dependency | <25% | Minimal injury impact |
| Moderate dependency | 25–35% | Noticeable but manageable |
| High dependency | 35–50% | Significant goal threat reduction without them |
| Critical dependency | >50% | Team fundamentally changes without this player |

**Betting application**: If a team's star striker (>40% of xG) is confirmed out, their xG per game typically drops by:
- 0.3–0.5 xG/game (from average 1.4 to 0.9–1.1)
- This equates to approximately 0.2–0.4 expected goals reduction in the actual match
- For a total market set at 2.5, this alone may flip the over/under lean

**Also track playmaker dependency**: How much does xA (expected assists) concentrate in one midfielder? Teams where one midfielder generates 40%+ of xA are similarly vulnerable to that player's absence — their attack loses its creativity engine.

---

## 5. Tactical Analysis for Betting

### 5.1 Reading a Team's Style from Statistics

You don't need to watch every match to understand how a team plays. The statistics tell the story:

**High-press teams**:
- PPDA: 4–8 (presses aggressively, allows few passes before winning it back)
- High tackles + interceptions in the middle and attacking thirds (not just defensive third)
- Possession: often 45–55% (not dominant possessors; they win it back and attack quickly)
- Fast counter-attack goals as a frequent event type

**Possession-dominant teams**:
- Possession: 60–70%
- High progressive passes per game (55+)
- Low PPDA (don't need to press — they hold the ball)
- Slow build-up; goals from sustained pressure rather than transitions

**Low-block / defensive teams**:
- PPDA: 12–18 (let opponents have the ball)
- Very low xG for (0.7–0.9/game) — limited attacking investment
- Very low xGA (0.6–0.8/game if elite, 0.9–1.1 if mediocre)
- High clearance rate; aerial duels concentrated in their own box
- Goals: frequently from set pieces, counter-attacks, or individual moments

**Direct/long ball teams**:
- Low pass completion (70–76%) — playing long passes deliberately
- High aerial duels won per game
- Few progressive passes in midfield (bypassing midfield entirely)
- High aerial win % in final third — their striker wins headers as the primary attacking method

### 5.2 Identifying Tactical Mismatches

| Matchup | Analysis |
|---|---|
| High press vs. poor press resistance | Pressing team creates high xG from turnovers; lean on them in AH |
| Possession team vs. press-and-counter | Possession team creates slowly; counter team profits from transition — lean under total, but over on counter team winning |
| Low block vs. direct ball team | Direct team bypasses the midfield but the aerial contest in the box may favor whoever wins headers — assess aerial duel stats |
| Set piece specialist vs. poor aerial defense | Significant corner/free kick edge; bet set piece-reliant markets |
| Two possession teams meeting | Neither team transitions quickly; game becomes structured and slow — lean under |
| Two high-press teams | High-intensity, high-turnover game; tends to produce more shots from both sides — lean over |

### 5.3 Predicting Tactical Adjustments

**When and why managers adjust**:
1. **Going behind by 2 goals**: Even the most defensive manager goes more expansive. xG increases for the trailing team in the second half.
2. **Protecting a lead against a stronger opponent**: Possession teams may drop into a 5-4-1 when 1-0 up away from home — their PPDA effectively becomes defensive.
3. **Playing the second leg of a knockout tie**: Strategy dictates whether they press or conserve — study the first-leg context.
4. **Depleted lineup**: Rotation forces the manager's hand tactically.

**Betting exploitation**:
- A possession team playing 0-0 at half against a low-block team will often open up after 60 minutes when the low-block team's legs tire and the possession team tries to force it. Lean over in second-half total markets.
- A team with a first-leg lead at home in the second leg of a tie will often sit deeper — lean under and lean away team to cover AH (the team needing to score is more motivated and takes risks).

### 5.4 Style vs. Context Matrix

Before assigning a style label to a team, confirm it's the right context:

| Context | Likely tactical shift |
|---|---|
| Team is strong favorite | May play conservatively, risk-manage — PPDA rises, xG drops |
| Team is a significant underdog | May drop into low block — xG drops significantly |
| Team needs a draw to qualify | Ultra-defensive; lean heavy under |
| Team needs to score 2+ to advance | Forced to attack; lean over |
| Dead rubber (nothing at stake) | Wildcards — may rest players or play with freedom |

---

## 6. Set Piece Analysis

### 6.1 Why Set Pieces Are an Inefficient Market

Set pieces account for approximately 30–35% of all goals in top European leagues. Despite this, most casual bettors and many books treat set pieces as secondary to open-play quality. The result: **systematic mispricing in corners, card, and total markets** when one team has a clear set piece dominance edge.

Key inefficiency: xG models that don't adequately separate set piece quality from open-play quality. A team that generates 1.4 xG/game with 0.5 of it from set pieces has very different risk from a team generating 1.4 xG/game entirely from open play.

### 6.2 Corner Frequency Analysis

**Metrics to track**:
- Corners won per game (attacking corners): average across last 10 games
- Corners conceded per game (defensive corners): how many corners does their style of defending force?
- Corner conversion rate: what % of corners result in shots? In goals?
- Corner type: inswinger vs. outswinger; short corner vs. cross; zonal vs. man-marking defense

**Where to find it**: WhoScored (corners per game), FBref (corner kick data in "Pass Types" column), SofaScore (match stats).

**Betting angle — Total Corners markets**:
- Books are less sophisticated on corner totals in smaller leagues (Championship, Ligue 1, Eredivisie) than they are on goal totals in the Premier League.
- A matchup between two teams averaging 6+ corners/game each suggests 10+ total corners is a solid lean if the total is set at 9.5.
- Historically: teams that win more possession force more corners (the defending team clears to the corner under pressure). Track possession dominance as a leading indicator for corners.

### 6.3 Delivery Type and Aerial Threat Ranking

Corners vary wildly in danger based on:
1. **Delivery quality**: A team whose corner taker hits whipped, inswinging deliveries to the six-yard box is far more dangerous than a team that plays short corners.
2. **Aerial threat in the box**: Headers require tall, strong players who time their runs. If a team has multiple aerial threats (a 6'2" CB + a 6'1" striker both in the box), their set piece xG is significantly elevated.
3. **Movement patterns**: Teams with structured set piece routines (blocking runs, off-ball movements creating space) generate more clear headed chances.

**How to evaluate**:
- Understat: Match report → "Situation" tab → "Set piece" xG per game (team level)
- FBref: Shooting table → filter to set pieces
- Watch 2-3 match clips specifically watching corner routines (Youtube, clubs' highlight channels)

### 6.4 Set Piece Goals Scored and Conceded

**Key ratios**:

| Metric | Source | Betting use |
|---|---|---|
| Set piece goals scored / total goals | FBref, Understat | High % = set piece dependent; significant when key set piece taker is injured |
| Set piece xG / total xG | Understat situation tab | Isolate open-play quality |
| Aerial duel win % in own box | FBref defensive stats | Low % = vulnerable to crosses and corners |
| Aerial duel win % in opposition box | FBref attacking stats | High % = strong aerial set piece attack |

**Free kick zones**: Teams with a world-class direct free kick taker (Trent Alexander-Arnold, Bruno Fernandes) inflate their set piece xG dramatically. When that player is absent, their set piece xG drops 0.1–0.2 per game — significant.

---

## 7. Referee Analysis

### 7.1 Why Referee Tendencies Matter

The specific official assigned to a match is one of the most underused pre-match variables in soccer betting. Every referee has documented statistical tendencies that are consistent across seasons. These tendencies directly affect:
- Cards per game (critical for player card props and total cards markets)
- Fouls per game (affects game flow and total goal market indirectly)
- Penalty frequency (affects 1X2 and specific markets)
- Home-team bias (affects 1X2 and Asian handicap)
- Extra time given (affects last-minute outcome markets)

### 7.2 Card Frequency by Official

**Data to build or find**:
- SofaScore: Match page → click referee name → career stats tab → yellows/game, reds/game
- FBref: Match logs note the referee; build your own log from match histories
- WhoScored: Referee section in match details

**Key thresholds**:

| Cards per game (yellows) | Category |
|---|---|
| <3.0 cards/game | Lenient official — lean under card totals |
| 3.0–4.2 cards/game | Average official — line should reflect this |
| 4.3–5.5 cards/game | Strict official — lean over card totals |
| 5.5+ cards/game | Very strict — significant over lean in cards markets |

**Compounding factors**: A strict official + two physically confrontational teams (see PPDA, tackle rate, foul rate) = very high card expectation. A lenient official + two technical, possession-dominant teams = very low card expectation.

### 7.3 Penalty Rate

Some officials call penalties at 3–5x the rate of others. This is partially because they work different competitions (more top-flight games = more penalty-worthy contact), but there is genuine individual variation beyond competition level.

**How to use it**:
- If the match features a pressing team that fouls frequently inside the box against an attacking team that runs at defenders, and the referee has a high penalty rate: BTTS probability increases slightly, and specific team to score probability increases.
- High penalty rate officials + teams with a prolific penalty earner (players who draw contact in the box) = small but real edge on total goals over markets.

### 7.4 Home-Team Bias

Research consistently shows that across European football:
- Home teams receive 15–25% fewer yellow cards than away teams per foul committed
- Home teams win more 50/50 decisions (ball out of play, fouls on the edge of the area)
- Certain referees exhibit stronger home bias than others

**Betting translation**:
- In very close 1X2 markets, a referee with documented strong home bias adds ~1–2% to the home win implied probability.
- For card markets: away team cards typically the better bet for "first card" props under most officials.

### 7.5 Stoppage Time Tendencies

Some officials consistently give 5–8 minutes of stoppage time in close games; others give 2–3 minutes regardless. This matters for:
- Late goal markets
- Whether a team protecting a lead needs to defend another 3 minutes or 7 minutes
- Live in-play betting: knowing a particular official always gives 6+ minutes in close games provides a live edge when a team is pressing for a goal

**Tracking method**: Build your own log of referees you see frequently. After each major-league match you research, note the official and the stoppage time given in both halves. Within one season you'll have usable data on the regulars.

---

## 8. Weather and Venue Factors

### 8.1 Altitude

**Impact**: At altitude above 2,000 meters, aerobic capacity is reduced by 6–10% per 1,000 meters elevation. Soccer is a high-aerobic sport; this significantly affects teams not acclimatized.

**Key high-altitude venues**:

| City | Altitude (m) | Key teams |
|---|---|---|
| Quito, Ecuador | 2,850 | LDU Quito |
| Bogota, Colombia | 2,600 | Millonarios, Santa Fe |
| Mexico City, Mexico | 2,240 | Club America, Cruz Azul |
| La Paz, Bolivia | 3,640 | The Strongest, Bolívar |
| Addis Ababa, Ethiopia | 2,355 | Ethiopian national team |
| Denver, USA | 1,600 | Colorado Rapids (moderate) |

**Betting rule**:
- Sea-level teams playing their first game at 2,500+ meters altitude should have their expected xG reduced by 10–15% in the second half (fatigue accelerates).
- Teams acclimatized (playing their home games there) have a structural advantage — lean home heavily at extreme altitude.
- In South American Copa Libertadores and World Cup qualifiers, altitude is the single biggest venue factor; books often underprice it.

### 8.2 Heat and Humidity

**Impact**: Games in extreme heat (30°C+, 85°F+) produce slower play in the second half. Both teams tire faster, pressing intensity drops, and the game opens up in the final 20 minutes.

| Condition | Betting lean |
|---|---|
| 30–35°C, high humidity | Under 2.5 first half; over second half as tired defenses make errors |
| 35°C+, high humidity | Significant second-half slowdown; lean under second-half total |
| Early-afternoon kickoff in summer | Maximum fatigue scenario; lean under |

**World Cup specific**: Qatar 2022 was air-conditioned. Brazil 2014 had extreme heat in interior cities — under-2.5 hit at a significantly elevated rate vs. European-based expectation.

### 8.3 Wet Pitch and Rain

**Impact on soccer** (unlike NFL where rain dramatically affects outcomes, soccer effects are more nuanced):

| Condition | Effect | Betting lean |
|---|---|---|
| Heavy rain, waterlogged pitch | Ball slows, aerial game disrupted, more slippery footing | Slight over (more errors, chaotic play) |
| Light consistent rain | Ball moves faster on wet grass — quicker transitions | Neutral; slightly over in possession-dominant games |
| Sudden downpour mid-game | Can disrupt momentum mid-match — particularly affects pressing teams | No pre-match adjustment possible |
| Recently heavily rained then dry | Fast, true surface | No adjustment |

**Key note**: Waterlogged pitches in England (November–February, particularly at Championship level or smaller grounds) reduce ball-speed significantly and favor more physical, direct teams over technical possession teams.

### 8.4 Artificial Turf (Astroturf / 3G Pitch)

**Key impact areas**:
- The ball moves faster and truer on 3G than on wet grass — transition attacks are faster.
- Players from grass-based leagues often struggle with the pace of the ball in early minutes.
- Injury risk increases on 3G (knee and ankle injuries are more common on hard surface).
- Teams that train and play on 3G regularly (many lower leagues, Scandinavian leagues in winter, MLS) have significant home advantages.

**Betting implications**:
- Home advantage is substantially amplified on 3G pitches for teams accustomed to them.
- Visiting teams from grass-dominant leagues at 3G surfaces: lean against them slightly, especially in first 20 minutes.
- Lower leagues where 3G is common: books adjust less efficiently — check if home team regularly plays on 3G vs. visiting team's typical surface.

### 8.5 Crowd Size and Atmosphere

**Impact**: Home advantage in soccer is the strongest of any major North American or European sport (~60% home win rate vs. ~57% in other team sports). Crowd effects are real and documented:

| Venue context | Estimated HW probability adjustment |
|---|---|
| Full capacity (50,000+), hostile atmosphere | Full +5–7% home win probability |
| Neutral venue (cup final, tournament) | Remove home advantage entirely |
| Empty stadium / COVID protocol | Home win rate drops to ~53–54% — significant lean toward away |
| Partial capacity (<30% full) | Roughly half the crowd effect |

**COVID-era data** (2020–2021): With empty stadiums, the home win rate dropped from historical ~46% to ~41–42% in most European leagues. Away teams and draws were underpriced. This effect is well documented and confirms the psychological/referee impact of crowd noise.

---

## 9. Tournament-Specific Research (World Cup & Major Tournaments)

### 9.1 Fatigue Accumulation Across Group Stage

At a 7-game World Cup (group stage + 4 knockout rounds), physical fatigue accumulates in ways that have no equivalent in club football. Key patterns:

**Physical load by round**:

| Round | Average minutes per player (squad avg) | Fatigue impact |
|---|---|---|
| Group Game 1 | 45–55 min (squad avg with subs) | Fresh; performance close to ceiling |
| Group Game 2 | 90–120 min cumulative | Manageable; some fatigue in 80+ min |
| Group Game 3 | 135–180 min cumulative | First real fatigue signals |
| Round of 16 | 225–270 min cumulative | Noticeable drop in pressing intensity |
| Quarter-final | 315–360 min cumulative | Significant fatigue; more errors |
| Semi-final | 405–450 min cumulative | Only the deepest squads maintain quality |
| Final | 495–540 min cumulative | Both teams operating below peak; coin-flip territory |

**Betting implication**:
- Teams with thin squads (relying on 11–12 players) fatigue faster than teams who can genuinely rotate 16 quality players.
- By the quarter-final stage, PPDA tends to rise 15–25% for even elite pressing teams vs. their group stage levels.
- Late-tournament matches feature fewer first-half goals and more second-half goals as legs tire — lean first-half under, second-half over as a structural pattern.

### 9.2 Knockout Pressure Performance

Tournament pressure affects teams differently. Some managers' systems are built for high-stakes, low-possession, low-risk management (Mourinho's ultra-defensive shells, Simeone's Atletico). Others perform below their club form in tournament pressure.

**Key historical patterns**:
- Dominant group-stage teams often drop performance in the round of 16 as opponents shift to purely defensive play.
- First knockout game: the cautious draw at 0-0 is the most likely outcome (historically ~28% of Round of 16 fixtures finish 0-0 at 90 min, well above normal ~8% league game rate).
- Teams with a "big game" manager who thrives in tactical defensive setups outperform their underlying metrics in tournament knockout rounds.

**Research checklist for knockout games**:
1. How does each manager historically perform in must-win knockout scenarios?
2. What is the defensive record in the current tournament (xGA trend vs. group stage)?
3. Are there any yellow card suspension risks for key defensive players?
4. Is there a penalty shootout history for either team? (GKs with known shootout performance differences)

### 9.3 National Team vs. Club Team Data Reliability

National teams present the most analytically challenging research environment because:
1. **Small sample sizes**: A national team plays 6–10 qualifying games and 3–5 friendlies before a tournament. That's insufficient for most metric stabilization.
2. **Tactical inconsistency**: Club managers use set rosters and train daily; national managers have 10-day windows 4–6 times per year. Tactical cohesion is lower.
3. **Player quality context switching**: A player who generates 0.4 xG/game at a Premier League club functions very differently when surrounded by differently-skilled national team teammates.
4. **Qualification opponent quality varies enormously**: CONCACAF qualification is not comparable to UEFA qualification — xGD in qualification is nearly meaningless for tournament power ratings.

**Best approach for national team analysis**:
- Prioritize recent tournament performance (last 2–3 tournaments) over qualification stats.
- Weight club form of individual players heavily when national stats are unreliable.
- Use FIFA/Elo-based power ratings as your baseline, then adjust for injury, suspension, and form.
- **Elo ratings** (eloratings.net, club-elo.com) are the gold standard for national team power ratings — better than FIFA rankings for predictive accuracy.

### 9.4 Manager Tendencies in Must-Win Games

A team that must win (or needs a specific result to advance) plays differently. Research the manager's historical tendencies:

| Manager style | Must-win approach | Betting adjustment |
|---|---|---|
| Pragmatic / defensive (Mancini, Simeone, Mourinho) | Wait for opponent to open up; strike on transition | Lean under first half; over second half if they're trailing |
| Attack-first (Nagelsmann, Guardiola, Klopp era) | Press from the start; force the game | Over total, lean pressing team |
| Reactive rotator | Adjust at half time based on first-half read | Second half often better indicator of result direction |

---

## 10. Pre-Match Research Checklist

A 15-point checklist to complete before placing any soccer bet. This should take 25–45 minutes for a well-researched wager.

---

### Before You Start: Confirm the Basics

**Point 1 — Identify the exact market you're targeting**
- What are you betting? 1X2, Asian Handicap, Over/Under total goals, BTTS, first-half total, corners total, player props?
- The research emphasis changes by market: total goals requires knowing xG and defensive structure; cards requires knowing referee and team foul rates; corners requires knowing set piece and possession tendencies.

**Point 2 — Check the current line and find the opening line**
- What was the opening line? What is the current line?
- Direction of movement: toward which team? By how much? (Line movement analysis — see `analysis/line-movement.md`)
- If sharp money moved the line, it's moving toward the correct side.

---

### Team Research

**Point 3 — Pull xGD for both teams (last 10 matches)**
- Use FBref or Understat.
- Calculate home/away xGD separately if it's a home/away fixture.
- Note: are they improving or declining over the last 5 games vs. the prior 5?

**Point 4 — Check PPDA and style categorization**
- FBref squad stats → "Misc" → find PPDA equivalent in defensive pressure section.
- Label each team: high-press, possession, low-block, direct.
- Identify the key tactical mismatch if one exists.

**Point 5 — Identify and verify the expected lineups**
- Source: official pre-match press conference (48 hours out), team X/Twitter accounts, Fabrizio Romano or reliable beat reporters.
- SofaScore / FBref for injury confirmed absences.
- Key question: Is anyone responsible for more than 30% of the team's xG or xA unavailable?

**Point 6 — Assess rotation risk**
- When did each team last play? How many days between matches?
- Is either team playing in a competition that prompts rotation (mid-table in league, already qualified/eliminated)?
- Is the manager known to rotate ahead of a more important fixture?

**Point 7 — Review squad depth and injuries**
- Check Transfermarkt injury section for each team.
- Note any CB pairing disruptions, goalkeeper changes, or DM absences.
- Quantify the impact: use the key player dependency framework (Section 4.4) to estimate xG impact of each absence.

---

### Statistical Deep Dive

**Point 8 — Set piece edge assessment**
- Which team is stronger at set pieces (aerial threat in the box, corner delivery quality)?
- What % of each team's xG comes from set pieces vs. open play? (Understat situation tab)
- If there's a clear set piece edge: check if the market for corners or BTTS reflects this.

**Point 9 — Goalkeeper quality check**
- PSxG-conceded vs. actual goals conceded for each GK (FBref goalkeeper stats).
- Is either goalkeeper significantly over- or under-performing their PSxG?
- Is one team's GK recently introduced (injury to starter)? Quality gap?

**Point 10 — Home/Away performance split**
- Pull each team's home vs. away xGD separately. FBref match logs → filter.
- Some teams are dramatically stronger at home (strong crowd effect, familiar surface); some are unexpectedly strong away.
- A team with +0.8 xGD at home but −0.3 xGD away is very different from a team with +0.4 xGD in both splits.

---

### Situational and Context Factors

**Point 11 — Identify the motivational context**
- Is either team in a must-win situation?
- Is either team's league position secured/relegated — a dead rubber?
- Revenge match? Manager sacked here before? (Less statistically reliable but worth flagging)
- Is it a derby or rivalry fixture? These produce different intensity levels and higher foul/card rates.

**Point 12 — Check the referee**
- Who is the assigned official? (Listed on SofaScore 24–48 hours before kickoff)
- Pull that referee's cards/game, fouls/game, and penalty rate on SofaScore.
- Does the referee's style advantage or disadvantage either team's playing style?
- If targeting cards market: strict official + two physical/confrontational teams = over lean.

**Point 13 — Weather and venue check**
- Is the match outdoors? Check weather forecast for kickoff time.
- Temperature above 30°C: lean toward second-half under.
- Heavy rain expected: slight over lean, assess which team benefits from a fast wet surface.
- Is this a 3G pitch? Does the home team regularly play on it? Does the visiting team?
- Altitude above 2,000 meters: major home advantage signal.

---

### Final Validation

**Point 14 — Calculate your implied probability vs. book probability**
- Convert the line to implied probability (see CLAUDE.md break-even table).
- Compare to your model-estimated true probability.
- If your edge is less than 3%: no bet. If 3–6%: 1 unit. If 7–12%: 2 units. If 12%+: 3 units (maximum).
- Run the bias checklist (crowd-bias.md): are public biases inflating one side?

**Point 15 — Line shop on Klashi vs. other available books**
- Is Klashi's line better or worse than the market consensus?
- Which Asian Handicap line or total goal line gives the most value?
- Best odds available = mandatory final step before placing.
- Log the bet immediately in `picks/2026/` with full reasoning using the template in `picks/template.md`.

---

## Quick Reference: Market-Specific Research Priority

| Market | Top 5 research priorities |
|---|---|
| 1X2 / Asian Handicap | xGD power ratings, home/away splits, key injuries, rotation risk, motivation |
| Over/Under 2.5 Goals | xG/xGA for both teams, defensive structure (PPDA), weather, GK quality, referee pace |
| BTTS (Both Teams Score) | xGA for both teams, clean sheet rate, GK dependency, set piece strength |
| Corners | Possession dominance, attacking width, team corner rates, referee style |
| Total Cards | Referee card rate, both teams' foul rates, rivalry/derby flag, PPDA (press = more fouls) |
| First Half Result | Press intensity in first 15 min, recent first-half xGD, squad freshness |
| Player to Score | Individual xG rate per 90, minutes expected, set piece delivery role |
| Clean Sheet | xGA, GK PSxG performance, opposing striker absence, set piece concessions |

---

## Key Tools Summary

| Tool | Cost | Primary Use |
|---|---|---|
| FBref.com | Free | xG, xGA, PPDA, progressive passes, player logs, squad stats |
| Understat.com | Free | Situation-split xG, shot maps, xG timeline per match |
| SofaScore.com | Free | Referee stats, live lineups, injury updates, head-to-head |
| WhoScored.com | Free | Opta-based match stats, tactical formations, league averages |
| Transfermarkt.com | Free | Squad depth, injury history, player values, ages |
| StatsBomb (GitHub) | Free | Open event-level data for select competitions; Python/R modeling |
| Eloratings.net | Free | National team Elo ratings (most reliable for tournament power ratings) |
| Club-elo.com | Free | Club-level Elo ratings across all European leagues |

---

*This guide should be reviewed and updated at the start of each major competition cycle. Referee databases should be refreshed seasonally as officials' statistical tendencies can shift with appointment changes and evolving interpretations from governing bodies.*
