---
name: create-story-seeds
description: Create and archive fiction story seeds through a lightweight dialogue. Use when the user wants AI-assisted story brainstorming, asks what to write, turns a brainwave into a seed, explores urban melodrama or romance hooks, builds short-drama style plots, or wants finished story seeds saved into a dedicated folder.
---

# Create Story Seeds

## Goal

Help the user turn a vague spark into a compact, usable story seed through conversation, then save the finished seed to a dedicated folder. Favor lively, emotionally specific urban romance and melodrama when the user has no other genre preference.

## Conversation Workflow

1. Start from the user's raw spark. If the spark is vague, ask up to 3 short questions; if it is already strong, draft immediately.
2. Default the genre to urban melodrama romance, short-drama energy, and high emotional tension unless the user chooses another direction.
3. Ask for missing pieces only:
   - protagonist: who is carrying the story
   - relationship hook: who they are entangled with
   - conflict: what makes the situation painful or hard
   - twist: what secret or reversal changes the meaning
   - emotional flavor: sweet, bitter, revenge, regret, ambiguous, healing, forbidden, or hot-blooded
4. Offer 2-3 seed directions when the user is undecided. Keep each option short enough to compare quickly.
5. Expand the selected direction into the story seed format below.
6. Save only after the seed is usable or the user explicitly asks to archive rough ideas. If the user is still brainstorming, keep talking.

## Story Seed Format

Use this format for final seeds:

```markdown
# <Title>

Date:
Status: seed
Genre:
Tone:

## One-Line Hook

## Logline

## Core Cast

## Relationship Engine

## Central Conflict

## Twist

## Emotional Promise

## Opening Scene

## Expansion Notes
```

Keep the seed specific enough that another agent can later expand it into a 1500-3000 word short story or short-drama outline.

## Save Rules

Default destination:

- If the current workspace has an `outputs/` directory, save to `<workspace>/outputs/story-seeds/`.
- Otherwise save to `<workspace>/story-seeds/`.

Name files as `YYYYMMDD-short-title.md`. Maintain an `index.md` in the same folder.

Prefer using `scripts/save_story_seed.py`:

```bash
python3 <skill-dir>/scripts/save_story_seed.py --workspace <workspace> --title "<title>" --body-file <seed.md>
```

If using the script is awkward, create or update the Markdown files directly. Always tell the user where the seed was saved.

## Quality Bar

- Make the relationship painful, specific, and legible.
- Make the choice difficult; avoid conflicts that can be solved by one honest sentence.
- Make the twist reframe the relationship, not merely add noise.
- Let the protagonist have agency, even when the setup is messy.
- Avoid real company secrets, identifiable private details, or direct reuse of real people's sensitive stories. Fictionalize anything personal.

## Optional Reference

Read `references/urban-romance-seeds.md` when the user wants examples, asks what makes a good seed, or is working specifically in urban romance, dog-blood melodrama, or short-drama style.
