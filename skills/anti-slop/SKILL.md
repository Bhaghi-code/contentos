---
name: anti-slop
description: Strip AI-writing tells from a drafted LinkedIn post before it reaches the grader or the user. Use this on any finished draft in the ContentOS pipeline, after the hook check passes, as the last cleanup pass before grading.
---

# Anti-AI-Slop Pass

## Why this is a separate step

Even a draft that follows voice.md's structure correctly can still read as obviously AI-written at the sentence level. This pass catches that — it's a targeted line edit, not a rewrite of content or structure.

## What to hunt for and remove

- **Wrap-up paragraphs**: any sentence that summarizes what was just said ("In conclusion...", "To sum up...", "At the end of the day..."). The closing question IS the ending — if there's a paragraph after the last arrow bullet that isn't the closing question, cut it.
- **Throat-clearing openers**: "Let's dive in", "Let's unpack this", "I want to talk about" before the actual hook.
- **Hedging language**: "I think maybe", "it could be argued", "in my opinion" (attributed opinions are fine when direct: "I think X" as a flat claim is fine; "I think maybe possibly X" is not).
- **Corporate filler words**: "leverage", "synergy", "unlock value", "circle back", "double-click on", "at scale" (unless literally about scale).
- **Tidy rule-of-three lists that aren't actually three distinct things**: if a "faster, better, cheaper"-style list has items that are just rephrasings of each other, either cut to the one real point or make each item genuinely concrete and different.
- **Em dashes**: replace with a period, comma, or restructure the sentence. Bhaghi's voice never uses them.
- **Generic hedge closers on the closing question**: "What do you think?" is too generic — the question should be specific to the post's takeaway (see voice.md examples: "Which part of your agent stack would survive a seven day blind spot?" not "What are your thoughts?").

## What NOT to touch

- Don't change the structure, the hook's content, or the arrow takeaways' substance — this pass is about word-level tells, not rewriting ideas.
- Don't remove the personal anchor section if the archetype calls for one.
- Don't over-correct into stiff, robotic-sounding "simple" prose — the goal is human and specific, not just short.

## Output

Return the cleaned post in full, plus a short list of what was changed (e.g., "removed 1 wrap-up sentence, replaced 1 em dash, cut 'unlock value'"). If nothing needed changing, say so plainly rather than inventing an edit.
