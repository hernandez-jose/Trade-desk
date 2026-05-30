# Line Movement Analysis

## Why Lines Move

Lines move for two reasons:
1. **Sharp/professional money** — respected bettors put large wagers on one side
2. **Public/square money** — high betting volume from the casual public forces the book to balance its liability

Understanding which type of money is moving a line is the core skill in reading the market.

> **See also**: `analysis/crowd-bias.md` — a deeper breakdown of *why* the public bets the way it does, how personal bias and fighter/team narratives distort lines, and how to systematically exploit it. Includes the Chimaev vs. Strickland (UFC 328) case study.

## Crowd Sentiment and Line Distortion

Public money is not random — it is systematically biased. The crowd reliably overvalues:
- Hyped, undefeated, or "feared" fighters and teams
- Recent dominant performances (recency bias)
- Popular, likable, or exciting fighters over boring grinders
- Heavy favorites (favorite–longshot bias)

And undervalues:
- Disliked or controversial fighters — public suppresses bets on them emotionally
- Decision grinders and defensive specialists
- Large underdogs regardless of structural matchup quality

When the crowd is strongly biased, the closing line reflects that distortion. The popular side is **overpriced** and the unpopular side is **underpriced** — often by 10–30 percentage points in extreme cases.

**Identification signal**: If the line moved further *toward* the already-popular side after opening, the crowd pushed it. The other side is now more +EV than it was at open.

**UFC 328 example**: Chimaev opened −400, got bet up to −513 by crowd action. Strickland moved from +300 to +390. The crowd's bias inflated a near-coinflip matchup (per the model: 51%/49%) into an 84%/20% implied split. Strickland won.

## Sharp vs. Square Action

### Square (Public) Action
- Bets the favorite
- Bets the over
- Bets primetime teams and marquee matchups
- Bets with their heart (hometown teams, recent hot teams)
- Effect on line: Moves the favorite's price up and the total up

### Sharp (Professional) Action
- Looks for inefficiently priced lines
- Bets early (morning lines, before the public acts)
- Uses large bet sizes that trigger book limits
- Often bets underdogs and unders
- Effect on line: Counter to public; creates reverse line movement

## The Line Movement Decision Tree

```
Step 1: What direction did the line move?

  Line moved toward favorite (e.g., -3 → -4):
    → Normal direction. Is public % also going to the favorite?
      YES → Public-driven move. No edge signal.
      NO (public % going to dog) → REVERSE LINE MOVEMENT. Sharp signal on the FAVORITE.

  Line moved toward underdog (e.g., -4 → -3):
    → Unusual direction. Is public % also going to the underdog?
      YES → Public reversal (maybe after injury news). Neutral signal.
      NO (public % still on favorite) → REVERSE LINE MOVEMENT. Sharp signal on the DOG.
```

## Reading Reverse Line Movement (RLM)

**Reverse Line Movement** is the clearest sharp money signal:
- The line moves OPPOSITE to where the public betting % would push it
- This means the book is adjusting to sharp action, not public action

**Example:**
- Lakers vs. Clippers: 60% of bets on Lakers, but line moves from Lakers -4 to Lakers -3
- The book moved AGAINST the public — sharp money is on the Clippers +4 or +3
- **Signal**: Follow the sharp action → Clippers +3

## Steam Moves

A **steam move** is when multiple books simultaneously move the same line within seconds or minutes. It indicates a large syndicate or network of sharp bettors has hit the same side across multiple books.

**How to identify on Klashi:**
1. Track the opening line
2. If the line jumps 1+ points in less than 5 minutes with no news, it's a steam move
3. Check if other books are also moving (compare manually)

**Response:** Jump on the same side before the line moves further. You won't always get the best of it, but you're on the right side.

## Key Timing Windows

| Time | Who's Betting | Quality of Action |
|------|--------------|-------------------|
| Line release (Sunday night/Monday AM for NFL) | Sharp money | Highest quality signal |
| Tuesday–Wednesday | Mixed | Moderate signal |
| 24 hours before game | Light sharp + moderate public | Moderate |
| 2 hours before game | Heavy public | Lowest quality (square) |
| 30 min before tip (NBA) | Late public + informed bettors | Watch for lineup news |

**Best time to bet:**
- If you're on the **same side as sharps**: Get in early after the line release
- If you're **fading the public**: Wait until 30–60 minutes before game time when public has pushed the line furthest

## Line Shopping on Klashi

Always compare Klashi's line to the market consensus. Even a half-point difference matters:

| Difference | Impact on -110 Bet |
|------------|-------------------|
| 0.5 pts on spread | Changes outcome in ~3–5% of games |
| 1 pt on spread | Changes outcome in ~5–8% of games |
| +5¢ on the juice | Saves 0.5% per bet — adds up over 100+ bets |
| +100 vs -110 ML | 2.4% difference in implied probability |

If Klashi has the best number: Bet now before it moves.  
If Klashi has a worse number: Wait or find another outlet.

## Closing Line Value (CLV) Tracking

Record every bet at the time you place it and the closing line:

```
Placed: Team A -3.5 (-110) at 10am
Closed: Team A -5 (-110) at 7:30pm
CLV: +1.5 points in your favor — you got the better number
```

CLV targets:
- **Positive CLV on >55% of bets**: Your process is sound
- **Average CLV of +0.5 points or more**: Elite sharp territory
- **Negative average CLV**: Your line-reading process needs work

## Half-Time and Live Line Movement

Live betting (in-game) lines reset at half-time. The half-time market is less efficient than pre-game:
- Books have limited time to set accurate lines
- Early live lines often shade toward the team that controlled the first half
- **Angle**: If the favored team is trailing by less than the spread suggested they should be, and they have the better team, the live spread may undervalue them

Live betting on Klashi:
- Move quickly — lines update every 30–60 seconds
- Never place a live bet during a commercial break (odds are often unfavorable)
- Focus on teams you've already analyzed pre-game; live betting a cold game is guessing

## Key Line Values by Sport

### NFL Key Lines
- 3.0 and 7.0 (most critical — never pay more than −125 to buy through these)
- 6.0, 10.0, 14.0 (secondary key numbers)
- Half-point purchases through 3 and 7 are almost always +EV

### NBA Key Lines
- Less rigid than NFL, but 4, 5, and 6 are common margins
- Worth paying 10–15¢ extra to get through these on large bets

### MLB
- Run line (+1.5 / -1.5) creates binary outcomes — one run is everything
- For totals, the first run is huge (shutouts are ~15% of all games)

### Soccer
- 0 and 1 are everything in soccer — clean sheets drive massive outcomes
- Asian handicap eliminates the draw, making these cleaner to bet
