# ContentOS

A small, skill-based content pipeline for drafting LinkedIn posts that stay in one consistent voice — built to learn how AI "skills" and multi-agent grading loops actually work in practice, not just conceptually.

Inspired by [this piece](https://freerollhq.substack.com/p/i-moved-my-contentos-from-claude) on building a self-improving content system, scaled down and rebuilt from scratch as a personal project.

## What this is

Instead of re-explaining "write in my voice, no em-dashes, hook in line one" every time I want a post drafted, the rules live once in `voice.md`. Every drafting skill reads it first. A topic goes through a chain of single-purpose skills, each one doing exactly one job:

```
topic → router → drafting skill (reads voice.md) → hook check → anti-slop pass → grader
```

The grader is deliberately run as an independent pass that never sees the drafting reasoning — only the finished draft against a fixed checklist — so it can't rubber-stamp its own work. A post has to score 60/80 with no single category below 4 to pass; if it fails, it comes back with one concrete fix, not a vague "make it better."

## Structure

```
voice.md                       - single source of truth for tone, structure, banned phrases
skills/
  post-router/SKILL.md          - classifies a topic into an archetype, never drafts
  news-breakdown/SKILL.md       - drafts reach/TOFU posts from external news/studies/benchmarks
  hook-check/SKILL.md           - checks the opening 1-2 lines against what has actually worked
  anti-slop/SKILL.md            - strips AI writing tells (wrap-up paragraphs, hedging, em-dashes)
  post-grader/SKILL.md          - independent scoring pass, pass/fail with one fix if it fails
  morning-scan/SKILL.md         - daily research scan for topic ideas, scored against audience fit
```

## What's not built yet

- `build-in-public` drafting skill (for personal project / career-pivot style posts)
- Performance tracking — pulling real post engagement back into the loop to catch which edits I keep making by hand, and testing skill revisions against that data before they ship (the "champion vs. challenger" idea from the source article)
- A scheduled daily brief currently runs in a separate always-on environment and isn't part of this repo's automation — see note below.

## Example run

A [test topic](docs/example-run.md) — a new AI agent benchmark launch — run through the full chain, including a first draft that failed the grader (a stray wrap-up paragraph before the closing line) and the corrected version that passed.

## Why this exists

Built as a hands-on way to learn what "AI skills" actually are (instruction files an agent reads before acting) and how independent grading loops work, while building a real, usable tool for my own LinkedIn content — part of my ongoing self-directed portfolio work moving into AI Product Management.
