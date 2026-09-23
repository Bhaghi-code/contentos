# ContentOS

I'm not going to pretend I sit down and write a LinkedIn post from a blank page every day. I don't. I'm building an AI PM portfolio while working a full-time job, and the honest version of "consistency" is a system, not willpower.

So I built one. This is it.

**What it isn't:** a prompt that spits out a finished post. I tried that path first and it reads exactly like what it is — generic, hedge-y, nobody's voice. **What it is:** a chain of small, dumb, single-job skills that get a draft 80% of the way there in my actual voice, so the 20% I do by hand (the part that decides if something's actually good) is the only part left for me to do.

Inspired by [this piece](https://freerollhq.substack.com/p/i-moved-my-contentos-from-claude) on a creator's self-improving content system — rebuilt from scratch, scaled down, as a way to actually learn how AI "skills" and independent grading loops work instead of just reading about them.

## The problem this solves

Every time I asked an AI to "write a LinkedIn post about X," I'd re-explain the same rules — no em-dashes, hook in line one, no wrap-up paragraph at the end, arrow bullets not numbers — and it would still drift back to generic AI voice by paragraph three. Re-explaining your own voice every single time isn't a system. It's just a longer prompt.

## How it actually works

The rules live once, in `voice.md`. Every drafting skill reads it first, so I never repeat myself. A topic goes through a chain of single-purpose skills:

```
topic → router → drafting skill (reads voice.md) → hook check → anti-slop pass → grader
```

The grader is the part that actually changed the output quality. It runs as an independent pass that never sees why the draft made the choices it made — only the finished text against a fixed checklist. A model grading its own writing is generous to itself by default; a cold, separate check isn't. A post needs 60/80 with no single category below 4 to pass. If it fails, it comes back with one specific fix, not "try again."

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

- `build-in-public` drafting skill, for personal-project and career-pivot style posts
- Performance tracking — pulling real post engagement back in to catch the edits I keep making by hand, and testing skill changes against that data before they ship (the "champion vs. challenger" idea the source article describes)
- The daily research brief currently runs on a schedule outside this repo, not as code in it — see note below

## Example run

A [test topic](docs/example-run.md) — a new AI agent benchmark launch — run through the full chain, including a first draft that actually failed the grader (a stray wrap-up paragraph the rules explicitly ban) and the corrected version that passed.

## Why this exists

I don't publish anything I wouldn't want to read myself, and I'm not interested in a system that writes posts I'd be embarrassed to have my name on. This isn't about not doing the work — it's about not spending the work on the parts that don't need a human, so there's more of me left for the parts that do. Built as hands-on portfolio work for my pivot into AI Product Management: less "I read about agentic AI," more "here's one I use every week and can show you exactly how it fails and gets fixed."
