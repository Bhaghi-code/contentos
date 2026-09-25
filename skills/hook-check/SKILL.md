---
name: hook-check
description: Check whether a drafted LinkedIn post's opening lines (the hook) will actually stop someone scrolling, based on Bhaghi's own patterns of what has worked. Use this on a finished draft, before the anti-slop pass and before the grader, as part of the post-drafting chain.
---

# Hook Check

## Why the hook matters more than anything else in the post

If the hook doesn't stop the scroll, nothing else in the post gets read. This check runs before grading the whole post because a structurally perfect post with a weak hook is still a failed post — you can't average your way to a good hook with good body copy.

## What to check, in order

1. **Does it open a real curiosity loop, or does it give away the ending?** A hook that previews a number but also reveals the outcome up front is a dead loop — nothing left to read for. Example of what NOT to do: "Here are 3 reasons AI agents are risky (spoiler: it's about safety)." That resolves the tension before the post starts.
2. **Is the first line's payoff still unclear at the fold** (the point where LinkedIn truncates and shows "...more")? If the punchline lands in the first line, there's nothing pulling the reader into the second line.
3. **Does it use one of the patterns that have worked for Bhaghi**, or a well-reasoned variant of one:
   - The two-beat reversal: "Everyone's quoting number A. The number that should worry you is B."
   - The scale reframe: a number placed against something people don't expect to compare it to (300 applications, 8x more likely, etc.)
   - Before/after or expected/actual: "It looked perfect in the demo. Real usage exposed something different."
   - A specific reader problem named directly, with no scene-setting first.
   (See `growth-engine` skill for the full hook-generation process this draft should already have gone through.)
4. **Is it in bold unicode formatting** (𝐥𝐢𝐤𝐞 𝐭𝐡𝐢𝐬), matching the visual pattern of her past hooks?
5. **Length**: 1-2 lines max. If the hook needs a third line to land, it's not sharp enough yet — cut, don't extend.
6. **Bad-hook filter** — fail immediately if the hook resembles any of these, unless the specific context makes the exact phrasing genuinely earn its place:
   - "AI is changing everything" / "AI is revolutionizing..."
   - "In today's fast-paced world..."
   - "Here are 5 things I learned..." / "Here are my thoughts on..."
   - "I wanted to share..." / "Let's talk about..." / "Excited to announce..."
   - "Game changer" / "Unlock the power of..."
   - Fake controversy, obvious clickbait, or a claim the body can't actually deliver on.
7. **First-three-lines test**: read only the first three lines in isolation (this is roughly LinkedIn's fold before "...see more"). Would a stranger scrolling their feed click to expand? If not, this is a FAIL even if lines 4+ are strong.

## Output

For the draft you're given, respond with:

```
Hook check: PASS or FAIL
If FAIL: which check above failed, and one concrete rewrite suggestion for the hook only (do not rewrite the rest of the post).
```

If it fails, hand the specific feedback back to whichever drafting skill produced the post so it can revise just the hook — don't silently rewrite the whole post yourself.
