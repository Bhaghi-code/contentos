---
name: post-grader
description: Score a finished, cleaned LinkedIn post draft against a fixed checklist derived from Bhaghi's own voice rules and past post structure, before it's shown to the user. Use this as the last automated step in the ContentOS pipeline, after hook-check and anti-slop have both run. Should ideally be run by a different agent/session than the one that drafted the post, so it isn't grading its own work.
---

# Post Grader

## Why grading has to be independent of drafting

A model grading its own writing tends to grade generously — it already believes its choices were reasonable, because it just made them. This skill should be invoked as a separate subagent from whichever one drafted the post, and it should be given ONLY the finished draft plus this checklist — not the drafting skill's reasoning, not the source article, not any explanation of why the writer made the choices it made. Grade what's on the page, not the intent behind it.

## Gate checks (pass/fail, run before scoring)

These are binary. **Any single failure here is an automatic overall FAIL**, regardless of the score below — a post can't average its way past these.

1. **Generic-AI test**: could 1,000 other AI/LinkedIn accounts have posted this word-for-word? If yes, FAIL — it's missing Bhaghi's specific experience, example, or interpretation.
2. **Proof-not-claims test**: any metric, result, or personal experience stated as fact must be traceable to the source material or Bhaghi's known background. If something reads fabricated or unverifiable, FAIL.
3. **Payoff-debt test**: does the hook promise something the body actually delivers, or does a sharp hook get followed by generic advice? FAIL if the body underdelivers on the hook's promise.
4. **So-what test**: for the core claim or news item, is it clear why it matters to an AI PM, not just what happened? FAIL if the implication is left implicit.

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
Gate checks: [PASS/FAIL each of the 4, one-line reason for any FAIL]
Score: XX/80
Item scores: [list all 8 with score + one-line evidence]
Verdict: PASS / FAIL
If FAIL: the one most important fix, described concretely enough that a rewrite could act on it directly.
```

A FAIL on any gate check overrides a passing score — report it as the verdict-determining reason.
