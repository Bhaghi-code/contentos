---
name: growth-engine
description: Apply proven LinkedIn growth mechanics (hook engineering, tension/payoff structure, proof over claims, contrast, visual strategy) on top of a drafting skill's output. Read this AFTER voice.md and BEFORE writing a draft, as part of any drafting skill in the ContentOS chain (news-breakdown, build-in-public, etc). This is a mechanics layer, not a voice — it never overrides voice.md's structure or banned phrases.
---

# Growth Engine

## What this is and isn't

This is the *architecture* that makes a post hard to scroll past — the mechanics behind why some LinkedIn posts get read and shared and others don't, regardless of author. It is benchmarked against what high-performing LinkedIn creators (e.g. Basia Kubicka) structurally do, but this skill never reproduces anyone's specific phrases, jokes, stories, or opinions. Nothing here is copied content — it's a reusable mechanism.

`voice.md` still owns Bhaghi's actual voice, structure, and banned phrases. This skill sits on top of it: same structure (hook → recap → pivot → arrow takeaways → optional caveat → optional personal anchor → closing question → hashtags), sharper execution at each step.

## Before drafting: the hook is a separate product

Never write the first line and move on. Before drafting, silently generate at least 5-8 genuinely different hook angles for the topic, using different mechanisms:

- surprising/counterintuitive observation
- specific quantified result
- mistake or failed attempt → lesson
- before vs. after / expected vs. actual
- conventional wisdom vs. reality
- hidden problem or pattern noticed
- "I thought X. Then Y happened."
- a very specific reader problem named directly

Then pick the one strongest on: curiosity, specificity, credibility, relevance, and whether the body can actually pay it off. Don't show the discarded hooks unless asked — just draft with the winner.

**A hook must earn its curiosity honestly.** It should make the reader feel "wait, what happened?" or "that's exactly my problem" — never rely on withholding obvious information just to force a click. voice.md's existing "open a loop, don't resolve it" rule still applies; this just gives more ways to open one.

## Structure: create tension early, then pay it off

Within voice.md's fixed structure, sequence the *reasoning* like this:

```
HOOK → TENSION/QUESTION → CONTEXT (the recap) → PAYOFF (pivot + takeaways)
```

Every strong hook creates payoff debt. The arrow takeaways exist to repay it — never follow a sharp hook with generic advice. If the hook promises a reframe, the takeaways must be the reframe, not a summary of the news.

## Proof over claims

Before drafting, check what real proof is available: a project Bhaghi shipped, a specific number, a real experience, a documented tradeoff, something she actually tried, built, or misjudged. Specificity is what makes a post credible — use it wherever it genuinely exists.

**Never invent** metrics, results, conversations, timelines, or experiences that aren't in the source material or Bhaghi's own stated background. If no real proof exists for a claim, say so plainly and either drop the claim or keep it as reported fact, not personal experience.

Prefer "I built/tried/saw X" over "you should always X" whenever real first-hand material exists.

## Contrast, sparingly

Natural contrasts make an idea memorable: prototype vs. product, demo vs. production, what looked impressive vs. what actually mattered, theory vs. reality. Use one genuine contrast if the material supports it — never force a false binary where the real answer is nuanced.

A "the real problem isn't X, it's Y" reframe is powerful but overused by AI writing — use it at most once per post, and only when it's the actual insight, not a rhetorical trick to sound insightful.

## The non-obvious angle

Before drafting, ask: "what's the most obvious post anyone could write about this?" Then don't write that one. Ask instead: what surprised me, what would a PM actually do differently Monday morning, what does everyone else's take on this miss. This is the same job news-breakdown's "buried number" rule already does — apply it to every archetype, not just news.

## Density and payoff

Once the hook has earned attention, the body has to pay for it. Every section should survive a "so what?" test — if the implication for an AI PM reader isn't obvious, make it explicit rather than leaving it implied.

Stop once the point has landed. Don't re-explain a conclusion that already landed in the takeaways — this is what voice.md's "no wrap-up paragraph" rule already protects against; this just extends it to mean don't overexplain mid-post either.

## Visual strategy

After the post text is done, decide deliberately whether it's text-only or needs one supporting visual — don't default to always adding one. A visual earns its place only if it teaches something the text alone doesn't (a comparison, a mechanism, a before/after, a stat that lands harder visually). If visual-first, pick exactly one concept — this project's existing card/animation templates (`scripts/card_template.html`, `scripts/animation.html`) are the production path; a visual should communicate its point within 1-2 seconds, so favor large headline + strong hierarchy + limited text over decoration.

## Final self-check before handing off a draft

Silently confirm, don't narrate:
- Could 1,000 other AI-LinkedIn accounts have posted this word-for-word? If yes, it needs more of Bhaghi's specific experience or interpretation before it's done.
- Is there one line or section someone would actually screenshot or quote?
- Would the first three lines alone (before "...see more") make someone click?
- Does the post make clear what a reader should now believe Bhaghi is good at, without saying so directly?

This feeds into `hook-check` and `post-grader`, which check the finished draft mechanically — this skill is about how the draft gets built in the first place.
