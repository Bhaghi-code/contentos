---
name: morning-scan
description: Run Bhaghi's daily ContentOS research scan — find AI/agentic-AI/PM news, GitHub trends, and HN/Reddit discussions from the last 24 hours worth turning into a LinkedIn post, score them, and produce a short brief. Use this when running the scheduled daily morning brief, or any time the user asks "what should I post about today."
---

# Morning Scan

## What this produces

A short brief, one topic per post-family, ranked by fit — not a raw dump of every AI headline from the last day. The goal is 2-4 topic options Bhaghi can pick from in under 2 minutes over coffee, not a research report to read.

## Audience fit (the ICP filter)

Bhaghi's audience is AI/Data product managers and PMs pivoting into AI PM roles. A topic is worth surfacing only if it passes ONE of these:
- It changes what an AI PM should do differently this week (a new eval standard, an incident with a clear product lesson, a policy shift affecting AI shipping)
- It's directly relevant to the AI-PM-career-pivot narrative (a new skill/course/market signal for PMs moving into AI)
- It has a counter-intuitive number or reversal buried in it — the kind of detail that makes for a strong contrarian hook (see voice.md and the news-breakdown skill)

Skip pure hype ("new model beats benchmark by 2%"), pure engineering-only news with no product angle, and anything already covered by every AI newsletter this week (oversaturated = not an opportunity).

## How to scan

1. Web search for AI agent / LLM product / AI PM news from roughly the last 24-48 hours. Cover a few angles: a general AI product/agent news search, a search for AI safety or incident news, and a search for PM career / AI hiring market news.
2. For each candidate story, note: what happened (1 sentence), why it's not just hype (1 sentence), and which post-family it would route to (news-breakdown vs build-in-public — see post-router skill).
3. Cut anything that fails the ICP filter above. Don't force a weak story in just to hit a quota.
4. Rank what's left. Prefer stories with a genuine reversal or buried detail over stories that are just "X launched."

## Output format

Keep it scannable — this is read over coffee, not studied.

```
MORNING BRIEF — [date]

1. [Topic headline] — [routes to: news-breakdown/build-in-public]
   What happened: [1 sentence]
   Why it's worth a post: [1 sentence — the reversal or angle]
   Possible hook direction: [1 short line, not a full hook]

2. [repeat, max 4 topics]

Nothing else cleared the bar today beyond these [N]. [Or: "Thin day — only 1-2 worth your time, rest was noise."]
```

If genuinely nothing worth posting turned up, say so plainly rather than padding the brief with weak filler — an honest "quiet day" is more useful than manufacturing urgency.
