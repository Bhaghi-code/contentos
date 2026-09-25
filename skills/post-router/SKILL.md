---
name: post-router
description: Use this skill first, before drafting any LinkedIn post for Bhaghi, to decide which post archetype the topic belongs to (contrarian/reach, build-in-public/trust, or lead-gen). It never drafts content itself — it only classifies and hands off. Trigger whenever a raw topic, article, or news item needs to become a LinkedIn post and the format hasn't been decided yet.
---

# Post Router

Your only job is to read a topic and decide which drafting skill should handle it. You never write the post yourself.

## Why this exists

Different post types have different jobs and different rules (see `voice.md`). A story about your own shipped project should never be drafted like a news breakdown, and a contrarian take on someone else's data should never be drafted like a personal story. Routing first keeps each drafting skill narrow and good at one thing, instead of every skill trying to do everything.

## How to decide

Read the topic/angle you were given and ask:

1. **Is this about something that happened externally** (a study, a benchmark, industry news, a stat that's being misread)? → **news-breakdown** (reach/TOFU)
2. **Is this about something Bhaghi personally built, shipped, or is learning** (a project, a course, a career pivot moment)? → **build-in-public** (trust/MOFU)
3. **Is this asking people to take an action** (comment for a resource, book a call, try a tool)? → **lead-gen** (BOFU) — flag that we don't have a lead-gen skill built yet; ask the user before proceeding, don't improvise one.

If a topic genuinely fits two shapes (e.g., external news that connects to something Bhaghi is personally building), say so explicitly, give a one-line reason for each, and let the user pick. Don't guess silently on a genuine tie.

## Output format

State your routing decision plainly before handing off:

```
Routing: [topic] → [archetype] skill
Reason: [one line]
```

Then proceed to invoke that drafting skill with the topic and any source material.

## Note for every archetype

Every drafting skill reads `voice.md` first, then `growth-engine` (hook-generation and structural mechanics that apply regardless of archetype), then drafts. This routing decision only picks which drafting skill's topic-specific rules apply on top of those two.
