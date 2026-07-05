---
name: write-xhs-qinzi-notes
description: Create Xiaohongshu-style 亲子/单亲妈妈/离异带娃 notes from viral post screenshots while respecting the account positioning file. Use when the user provides 爆款小红书截图 or asks to 复刻/仿写/拆解/生成 a 亲子赛道笔记 about 离异带娃、育儿日记、育儿经验、亲子关系讨论、单亲妈妈成长, with one cover image or image prompt, title, body text, hashtags, user confirmation, and saving to a specified folder.
---

# Write Xhs Qinzi Notes

## Core Workflow

Use this skill to turn user-provided Xiaohongshu viral-note screenshots or a clear topic brief into an original 亲子赛道 note package.

1. Read `references/note-workflow.md` before drafting from screenshots or saving a confirmed note.
2. Before drafting, read the account positioning file. Default path: `/Users/alinyao/Vicky/小红书笔记/亲子赛道/账号定位.md`. If the user provides another account-positioning file, read that one instead. If no positioning file exists, ask for the account direction unless the user explicitly wants a temporary draft.
3. Inspect every screenshot. Extract the reusable structure, hook pattern, emotional arc, paragraph rhythm, CTA, title formula, tag mix, and cover-image direction.
4. Draft an original note that mirrors the winning structure and voice without copying distinctive sentences from the source screenshots.
5. Include exactly these user-facing parts in the draft: one parent-child cover image or image-generation prompt, one note title, body text, and hashtags.
6. Ask the user to confirm or request edits. Do not save before explicit confirmation.
7. After confirmation, save to the folder specified by the user. If no folder is specified, ask for the destination folder.

## Account Positioning

Classify each note against the account positioning before drafting: 主理人育儿日记, 离异带娃生活片段, 育儿经验/方法论, 亲子关系讨论, 妈妈成长/边界感, or 投稿/妈妈来信. Let the positioning shape the note's point of view, but do not paste positioning slogans into the public note.

Every note must carry a stable subtext: 离异不是人生污点，带娃不是苦情人设，妈妈可以疲惫、柔软、偶尔失控，但她仍在学习把自己和孩子都照顾好. Turn that value into scenes, choices, and questions rather than direct preaching.

Make each note discussable. Build around one concrete tension or open question, then end with a soft comment prompt that readers naturally want to answer.

## Continuity And Privacy Guardrails

- Do not infer real facts about the account owner, child, ex-partner, custody, city, income, school, diagnosis, or family timeline from a single draft, screenshot, or case story.
- If a future note adds durable facts about the account owner or child, update the account positioning file only after user confirmation. Do not update cross-project personal memory unless the user explicitly asks.
- Protect the child first: avoid real names, birthdays, school names, school badges, addresses, license plates, medical records, identifiable conflict details, or face-forward real-child images unless the user has explicitly provided consent and intent.
- For 投稿/妈妈来信, anonymize people and locations. Make clear whether the story is a submission, a reader's note, or the account owner's own diary.
- Discuss divorce, co-parenting, single parenting, and emotional pressure without making legal, medical, or psychological claims that are not in the source material.
- Do not attack or dox an ex-partner. Write conflict through scenes and boundaries, not public shaming.

## Content Patterns

Use these as house patterns unless the user provides stronger reference screenshots:

- `离异带娃破防瞬间` works when the title names one concrete trigger: 一句童言, 一张家长会通知, 一只没洗的饭盒, 一次发烧, 一盏夜灯, 一通电话.
- `一个人带娃后才懂系列` works when it starts from a scene and lands on a small insight: 边界、情绪稳定、钱和时间、家务分工、陪伴质量、妈妈的自我修复.
- `孩子懂事反噬系列` works when it challenges the reflex to夸孩子懂事. The note should protect the child from adult emotional labor.
- `育儿经验/方法论` should begin with one reader-recognizable scene, then give 2-3 concrete signals or做法. Hide the method inside lived details before summarizing the lesson.
- `亲子讨论题` can drive comments when it asks a plain stand-taking question: 要不要在孩子面前提离婚, 爸爸缺席时怎么解释, 妈妈该不该一直扛, 孩子发脾气先抱还是先讲道理.
- `妈妈成长/边界感` should show the mother reclaiming one small part of herself, not pretending she has solved everything.

## Weak Patterns To Avoid

- Avoid苦情卖惨、完美妈妈人设、单亲妈妈鸡汤、审判式育儿、夸大恐惧, and titles that turn divorce into shame.
- Avoid using the child as a prop to prove adult pain. Do not write scenes where the child must comfort the parent as a desirable outcome.
- Avoid abstract course-like titles such as `高能量妈妈养成法`, `情绪稳定型父母底层逻辑`, or `单亲家庭创伤修复指南` unless the note starts with a concrete lived scene.
- Avoid long conceptual checklists, red-check/green-check sheets, and multi-level rankings unless the reference screenshot clearly relies on them.
- Avoid diagnosing the child or the ex-partner from behavior. Use everyday language such as `他那晚哭了很久`, not unsupported labels.
- Avoid exposing litigation, custody, school, medical, or financial details beyond what the user explicitly intends to publish.

## Title Rules

Strong titles are concrete, readable in one second, and carry one emotional hook or open question. Prefer titles with `离异带娃`, `单亲妈妈`, `一个人带娃`, `孩子`, `妈妈`, `育儿`, or one specific object/action.

Good title directions:

- `离异带娃最怕的，不是累，是孩子突然懂事`
- `儿子问我爸爸什么时候来，我愣了三秒`
- `一个人带娃后，我把「懂事」还给了孩子`
- `离婚后第一次家长会，我没有躲`
- `孩子发脾气那晚，我终于没急着讲道理`
- `单亲妈妈带娃，最该省的是内耗`

## Image Requirement

Provide one cover image for each note. The cover must make the 亲子/带娃 theme instantly visible: parent-child daily scene, home table, bedtime reading, school gate without identifiable school marks, commute, playground, grocery run, hospital waiting area without medical details, or a quiet mother-alone-after-bedtime scene when the note is about the mother.

For generated images, prefer fictional or non-identifiable children. Use back view, side view, partial silhouette, or soft distance when the child is central. Avoid real-child face exposure, school uniforms with badges, license plates, home addresses, documents, hospital records, or screenshots of private chats.

Cover words, if used, should be short and easy to decode, such as `离异带娃`, `他那句话`, `不是我撑住了`, `妈妈也会累`. Put text in clean negative space; do not place it on faces, heads, school marks, documents, or the child's body.

If image generation is unavailable, provide a ready-to-use image prompt and mark the note as waiting for image generation before final archive.

## Saving Confirmed Notes

Prefer `scripts/save_note.py` for confirmed archives. It creates a timestamped note folder, copies the cover image when provided, and writes `note.md` with the title, body, tags, image reference, and source metadata.

Use manual saving only when the script does not fit the user's requested folder format.

## Quality Bar

- Preserve the source screenshot's structure, not its exact wording.
- Read and follow the account positioning file before drafting.
- Write in natural Xiaohongshu Chinese: concrete scenes, short paragraphs, emotional tension, useful reflection, and a soft comment/save CTA.
- Make the note feel like a real parent or mother thinking through a real day, not a marketing account or lecture.
- Give every note one discussable conflict or question.
- Keep the child's dignity and privacy intact even when the story is emotional.
- Make tags discoverable and relevant to 亲子/育儿/离异带娃 rather than stuffing generic traffic tags.
- Favor concrete scenes, objects, and quoted lines over abstract parenting concepts.
- For 投稿/妈妈来信, separate case characters from account-owner facts.
- For method posts, begin with lived detail before naming the method.
- Treat confirmation as a hard gate before writing files.
