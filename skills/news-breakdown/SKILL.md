---
name: news-breakdown
description: Draft a reach/TOFU LinkedIn post for Bhaghi that breaks down external AI/product news, a study, or a benchmark and reframes what it actually means. Use this after post-router has classified a topic as news-breakdown, or directly when the user hands you an article/study/stat and asks for a LinkedIn post about it.
---

# News Breakdown Drafting Skill

## Before you write anything

Read `../../voice.md` (or wherever this project's voice file lives — ask if you can't find it) in full. It defines the structure, line-level rules, and banned phrases that every post must follow. Do not improvise a different structure even if it feels more natural for the topic — the structure is what makes Bhaghi's posts recognizably hers across dozens of different topics.

## What this archetype is for

A news-breakdown post takes something that already happened (a study, a benchmark, an incident, a policy move) and does the thing most people commenting on it won't: finds the detail that changes what it means, not just what it says. Look at Bhaghi's "1,200 agents" post as the model — the headline number (1,200 agents coordinating) is not the point of the post. The buried number (7 days before anyone noticed) is the point.

Your job when drafting: find that buried number or overlooked detail in the source material BEFORE you start writing the hook. If you can't find one, say so and ask for more source material rather than manufacturing a fake reversal.

## Structure to follow (from voice.md, applied to this archetype)

1. **Hook**: state the number/fact everyone will fixate on, then immediately hand over the number that should actually worry them. This two-beat structure (expected number → real number) is the single most identifiable feature of this archetype.
2. **Quick recap**: 2-4 sentences, plain text, giving just enough of the actual event that someone who hasn't seen it can follow along. Stay factual and reporter-voice here — no opinion yet.
3. **Pivot line**: explicitly name that most people are missing the real story. This is where opinion starts.
4. **Arrow takeaways** (3-4, never more): each one must be an actionable implication for someone building or shipping AI products — not a restatement of the news. Ask yourself "so what does a PM do differently Monday morning" for each bullet.
5. **Correction/caveat block** (only if needed): if the news is prone to being oversimplified or already being misreported elsewhere, correct it plainly here.
6. **No personal anchor** — this archetype stays in reporter/analyst voice throughout, unlike build-in-public posts.
7. **Closing question**: end on a question that invites people to apply the takeaway to their own stack/team/situation. End with 👇.
8. **Hashtags**: 6-8, mixing broad (#AIProduct, #ProductManagement) with topic-specific (#AIGovernance, #AIAgents, #AISafety) — pick from what's genuinely relevant to the source material, don't force ones that don't fit.

## What to avoid

- Don't editorialize in the recap section — save opinion for the pivot line onward.
- Don't use all the source material. Pick the 2-3 facts that build the reversal and the takeaways; cut the rest.
- Don't manufacture outrage or urgency that isn't earned by the actual facts.

## Output

Produce the full post text, ready to paste into LinkedIn. After the draft, briefly note (1-2 lines, not part of the post) which source fact you used for the hook reversal, so it's easy to sanity-check you didn't misread the source.
