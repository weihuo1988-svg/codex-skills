---
name: write-xhs-jiedilian-notes
description: Create Xiaohongshu-style 姐弟恋/年下恋 notes from one or more viral post screenshots while respecting the account positioning file. Use when the user provides 爆款小红书截图 or asks to 复刻/仿写/拆解/生成 a 姐弟恋赛道笔记 with one couple image, title, body text, hashtags, stable account voice, user confirmation, and saving to a specified folder.
---

# Write XHS Jiedilian Notes

## Core Workflow

Use this skill to turn user-provided Xiaohongshu viral-note screenshots into an original 姐弟恋 note package.

1. Read `references/note-workflow.md` before drafting from screenshots or saving a confirmed note.
2. Before drafting, read the account positioning file. Default path: `/Users/alinyao/Vicky/小红书笔记/姐弟恋赛道/账号定位.md`. If the user provides another account-positioning file, read that one instead.
3. Inspect every screenshot. Extract the reusable structure, hook pattern, emotional arc, paragraph rhythm, CTA, title formula, tag mix, and cover-image direction.
4. Draft an original note that mirrors the winning structure and voice without copying distinctive sentences from the source screenshots.
5. Include exactly these user-facing parts in the draft: one 姐弟恋 image or image-generation prompt, one note title, body text, and hashtags.
6. Ask the user to confirm or request edits. Do not save before explicit confirmation.
7. After confirmation, save to the folder specified by the user. If no folder is specified, ask for the destination folder.

## Account Positioning

Classify each note against the account positioning before drafting: 主理人日常, 投稿/会客厅故事, or 女性成长/方法论. Let the positioning shape the note's point of view, but do not paste positioning slogans into the public note.

Every note must carry a stable subtext: the older sister can be moved, sweet, and vulnerable, but she stays independent, clear-headed, and self-respecting. Turn that value into scenes, choices, and questions rather than direct preaching.

Make each note discussable. Build around one concrete tension or open question, then end with a soft comment prompt that readers naturally want to answer.

## Published Account Learnings

These rules come from the account's previously published notes, including the `数据好` and `数据不好` samples reviewed on 2026-07-05. Use them as house style unless the user explicitly changes direction.

### Continuity Guardrails

- The account display voice can use `Vicky 姐姐的小酒馆`, `今晚的 Vicky 小酒馆，聊聊八卦`, `酒馆互动时间`, and `酒馆故事征集`.
- Do not treat every first-person note as account-owner daily content. Many published posts are 会客厅/身边姐姐 stories, such as: a self-media sister with a photographer弟弟, a finance sister with a younger boyfriend, an art/freedom-oriented sister, a VP sister, or a studio-owner sister. These are case characters, not the fixed account-owner couple.
- Early social or invitation posts can mention the account voice around Shanghai/Yongjia Road citywalk, coffee, travel, interests, workplace, e-commerce, and AI, but mark them as 主理人口吻/社交帖. Do not merge them into the fixed CP timeline unless `账号定位.md` explicitly says so.
- When a note says `我有个姐们`, `我一闺蜜`, `有姐妹给我留言`, or uses story-collection framing, classify it as 投稿/会客厅故事 by default.
- If a future note adds durable facts about the account owner or fixed CP, update `账号定位.md` after confirmation. Do not infer real identity, city, occupation, relationship stage, family, income, or timeline from case stories.

### Winning Content Patterns

- `下头瞬间系列` works when the title uses one concrete trigger: `一条朋友圈`, `一碗螺蛳粉`, `一串钥匙`, `一句话`, `一张纸条`. The formula is `姐弟恋下头的那一瞬间，是因为 X`.
- The best `下头瞬间` posts first let the reader feel the sweet part, then reveal a specific imbalance: she enters his private album but not his public life; she pays and cares for him but he treats her care as default; she gives him a key but his future has no seat for her.
- The conflict must be `我给了什么 / 他没有给什么`, not merely a pretty object or vague disappointment.
- `姐姐优点反噬系列` works when it challenges a virtue that sisters identify with, such as 懂事、独立、成熟、会照顾人、会赚钱. The hook can be: `抱歉，你的「懂事」在弟弟眼里可能一文不值`.
- Methodology posts should still begin with a concrete scene or sentence. High-level insight is useful only after the reader is already inside the story.
- `许愿互动帖` can drive comments: use a simple big-text card, direct desire, and short copy such as wanting a 帅弟弟/甜弟弟 after being hurt by older men. Keep it lightweight and obvious.
- `意外开始系列` should use one exact action as the entry point: he left 胃药和小米粥, wrote a note, remembered a detail, waited in the rain, or noticed she was exhausted. The title should name that action.
- `故事征集/咖啡小酒馆` posts can work only when they bring readers back to 姐弟恋 stories. A coffee/citywalk invitation should ask for 年下恋经历, not become a generic local social post.

### Weak Patterns To Avoid

- Avoid abstract course-like titles such as `为什么你总吸引弟弟`, `情绪价值能力段位鉴定`, or titles dominated by concepts instead of scenes.
- Avoid red-check/green-check test sheets, multi-level ranking systems, and long conceptual checklists unless they are anchored by one vivid story first. If using levels, keep at most three.
- Avoid high-density terms like `情绪包容力`, `人生框架清晰度`, `情感需求密度`, or `吸引力核心` unless immediately translated into daily behavior.
- Avoid literary-but-blurry lines when the topic is already strong. For marriage, childbirth, future plans, money, and public commitment, ask a plain stand-taking question.
- Avoid comment prompts that are too heavy, such as asking readers to confess a deep lack or debt. Prefer low-friction prompts with two clear choices.
- Avoid pure non-track social posts. Coffee, citywalk, travel, workplace, e-commerce, or AI details must serve the 姐弟恋 account, or they dilute the account label.
- Avoid workplace power imbalance framing such as boss/intern or manager/subordinate romance unless the user explicitly requests it and the adults, consent, and power boundary are handled carefully. Prefer 合作方、项目搭档、朋友介绍、行业活动认识.

### Title Rules From Published Samples

- Strong titles are specific, concrete, and slightly刺痛. They usually contain `姐弟恋`, `姐姐`, `弟弟`, `年下`, or a concrete trigger.
- Prioritize titles a reader understands in one second:
  - `姐弟恋下头的那一瞬间，是因为一条朋友圈`
  - `姐弟恋下头的那一瞬间，是因为一碗螺蛳粉`
  - `我给了他工作室钥匙，他的未来却没有我`
  - `小我12岁的他，说司令不能先倒下`
  - `他越喊你姐姐，你越别急着心动`
- Weak titles can often be repaired by replacing abstractions with a scene:
  - Instead of `为什么你总吸引弟弟？这是赞美，也是陷阱`, use `你吸引年下男，可能不是因为你特别`.
  - Instead of `姐弟恋开始的那一瞬间，往往是个意外`, use `弟弟把胃药放我桌上那一刻，我没躲过`.
  - Instead of `给弟弟的情绪价值能力做个段位鉴定`, use `弟弟有没有情绪价值，看他回你这句话`.

### Cover Rules From Published Samples

- Winning covers are easy to decode: close couple tension, age-gap labels, night street, face-to-face intimacy, hand-holding, turning-away breakup mood, or a clean big-text card for direct interactive wishes.
- Strong cover words should be short: `姐姐~`, `再见爱人。`, `想找个帅弟弟谈恋爱！`.
- Use big-text cards sparingly. They work for simple wish/interact posts, but not for complex method posts.
- Single-boy covers are weak for complex relationship analysis because they do not show the sister-brother dynamic. Use them only for light `想找弟弟` or `弟弟类型` posts.
- Avoid covers that look like celebrity portraits, studio photos, hotel luxury shoots, or generic couple sweetness when the text is about 下头、清醒、压力、未来规划 or relationship imbalance.
- For story posts, choose a scene matching the core trigger: phone/social feed for朋友圈, food/takeout for螺蛳粉, key/studio/door for钥匙, rain/subway/medicine note for照顾瞬间.

### Structure And CTA

- Open within three lines with the core contradiction. Do not spend too long decorating the romantic setup.
- Use this emotional arc for story posts: sweet detail -> specific imbalance -> the sister's inner realization -> clear but non-preachy insight -> easy comment question.
- Use this arc for method posts: one reader-recognizable scene -> name the pattern -> give 2-3 concrete signals -> end with a choice question.
- Good CTA examples:
  - `如果你是这个姐姐，你会继续吗？`
  - `弟弟说为你不要孩子，你会感动还是有压力？`
  - `你遇到过被藏起来的瞬间吗？`
  - `他这样算少年感，还是没责任感？`
- Pinned or author comments can be lighter than the body, such as asking where readers met younger men or inviting one-sentence story openings.

## Image Requirement

Provide one cover image for each note. For the 姐弟恋赛道, make the age gap visible on the cover whenever possible: place birth years or ages near the two adults, such as `93` above the older sister and `03` above the younger boyfriend. Treat this age-gap label as a primary visual hook, not as optional decoration. Keep the labels in nearby background/negative space; do not place text on faces, hair, heads, or bodies. Match the reference screenshot style with modest white numbers rather than oversized, high-contrast poster text. Because these labels are usually white, place them over darker or textured areas such as trees, dark buildings, clothing-adjacent negative space, or shaded backgrounds; avoid pale sky, white walls, and other low-contrast light areas.

When generating an image, ensure both people are clearly adults and keep the scene romantic, intimate, and non-explicit. If image generation cannot reliably render text, generate or choose a clean couple image first, then add birth-year or age labels with an image editor before presenting the draft. If image generation is unavailable, provide a ready-to-use image prompt and mark the note as waiting for image generation before final archive.

If the note is account-owner daily content, keep the female lead, male lead, birth years, age gap, and visual style consistent with the account positioning and prior confirmed daily covers. Do not randomize faces, ages, or the `93` / `03` style age labels unless the user explicitly changes the account setting.

## Saving Confirmed Notes

Prefer `scripts/save_note.py` for confirmed archives. It creates a timestamped note folder, copies the cover image when provided, and writes `note.md` with the title, body, tags, image reference, and source metadata.

Use manual saving only when the script does not fit the user's requested folder format.

## Quality Bar

- Preserve the source screenshot's structure, not its exact wording.
- Read and follow the account positioning file before drafting.
- Write in natural Xiaohongshu Chinese: concrete scenes, short paragraphs, emotional tension, and a soft comment/save CTA.
- Keep the note grounded in adult, consensual relationships.
- Make the cover instantly communicate 姐弟恋 by labeling each person with birth year or age when the reference materials use that pattern.
- For account-owner daily notes, preserve consistent male/female appearances and age information across images.
- Keep the underlying viewpoint aligned with independent, clear-headed older-sister values without turning the note into explicit instruction or slogan copy.
- Give every note a discussable conflict or question that invites comments.
- Make tags discoverable and relevant to 姐弟恋/年下恋 rather than stuffing generic traffic tags.
- Favor concrete scenes, objects, and quoted lines over abstract relationship concepts.
- For 会客厅故事, protect continuity by separating case characters from account-owner facts.
- For method posts, hide the method inside lived details before summarizing the lesson.
- Treat confirmation as a hard gate before writing files.
