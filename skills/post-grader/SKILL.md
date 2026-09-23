---
name: post-grader
description: Score a finished, cleaned LinkedIn post draft against a fixed checklist derived from Bhaghi's own voice rules and past post structure, before it's shown to the user. Use this as the last automated step in the ContentOS pipeline, after hook-check and anti-slop have both run. Should ideally be run by a different agent/session than the one that drafted the post, so it isn't grading its own work.
---

# Post Grader

## Why grading has to be independent of drafting

A model grading its own writing tends to grade generously — it already believes its choices were reasonable, because it just made them. This skill should be invoked as a separate subagent from whichever one drafted the post, and it should be given ONLY the finished draft plus this checklist — not the drafting skill's reasoning, not the source article, not any explanation of why the writer made the choices it made. Grade what's on the page, not the intent behind it.

## Checklist (score each 0-10, then give one overall verdict)

1. **Hook strength**: does it open a real curiosity loop and use bold formatting? (This should already have passed hook-check, but confirm.)
2. **Structure adherence**: hook → recap → pivot → arrow takeaways (3-4) → optional caveat → optional personal anchor → closing question → hashtags, in that order, nothing missing that the archetype requires.
3. **One point per bullet**: does each arrow takeaway say one distinct, concrete thing, or do any of them repeat each other in different words?
4. **Reading level**: could a smart stranger with no AI background follow every sentence? Flag any jargon that isn't explained inline.
5. **No AI tells remaining**: spot-check for anything anti-slop should have caught but didn't (wrap-up paragraphs, hedging, em dashes, corporate filler).
6. **Specificity**: does the post contain at least one concrete number, name, or detail rather than staying abstract throughout?
7. **Closing question quality**: is it specific to this post's takeaway, not a generic "thoughts?"
8. **Hashtag fit**: are the hashtags actually relevant to the content, not generic filler?

## Scoring and verdict

- Give each of the 8 items a score 0-10 and one line of evidence for the score.
- Sum to a total out of 80.
- **Pass threshold: 60/80**, AND no individual item scoring below 4 (a single bad failure shouldn't be averaged away by strong scores elsewhere).
- If it fails, name the single most important fix — not a laundry list — so the drafting skill can make one targeted revision rather than a full rewrite.

## Output format

```
Score: XX/80
Item scores: [list all 8 with score + one-line evidence]
Verdict: PASS / FAIL
If FAIL: the one most important fix, described concretely enough that a rewrite could act on it directly.
```
