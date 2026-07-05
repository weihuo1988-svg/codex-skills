# Routing and Memory Reference

## Slice Types

- `side-business-idea`: 副业灵感, monetization ideas, product/service concepts, channels, pricing, audiences.
- `parenting-reflection`: 带娃感受, child development observations, parenting lessons, family routines.
- `work-project-note`: project decisions, implementation ideas, research notes, product requirements.
- `task-commitment`: explicit to-dos, promises, deadlines, reminders, follow-ups.
- `calendar-event`: 具体日程安排，例如吃饭、会议、约见、出行、预约；需要创建手机提醒、日历事件，或写入 Markdown 日程账本以便后续查询和冲突检查。
- `personal-reflection`: mood, values, life observations, non-project journaling.
- `relationship-note`: stable relationship context, family/social roles, important people.
- `preference-identity`: identity, durable likes/dislikes, working style, communication preferences.
- `anniversary-date`: birthdays, anniversaries, recurring dates, annual rituals.
- `health-life-admin`: health, appointments, home/admin/finance logistics; keep private and avoid long-term memory unless explicit.
- `durable-project-rule`: long-lived collaboration rules, QA standards, role splits, operating methods.
- `unrouted`: insufficient context to choose a destination safely.

## Routing Heuristics

Infer destination from the strongest evidence:

1. User-named project, repo, folder, or document.
2. Keywords in the slice that match existing filenames or headings.
3. Current working directory or active repo, if the slice is clearly about that work.
4. Existing docs with names like `ideas`, `inbox`, `notes`, `journal`, `diary`, `parenting`, `family`, `todo`, `roadmap`, `AGENTS`, or their Chinese equivalents: `灵感`, `想法`, `收件箱`, `笔记`, `日记`, `带娃`, `家庭`, `待办`, `路线图`, `协作规则`.

Prefer these common destinations when present:

- `side-business-idea` -> idea bank, business notes, product opportunities, project roadmap.
- `parenting-reflection` -> parenting journal, family notes, personal journal.
- `work-project-note` -> project notes, roadmap, requirements, design docs, implementation notes.
- `task-commitment` -> project todo/task list, personal action log, or an inbox if no task system exists.
- `calendar-event` -> reminder/calendar/schedule-ledger flow first; check the user's schedule ledger for conflicts before adding a new active or tentative event.
- `durable-project-rule` -> project `AGENTS.md`, contributor guide, operating handbook, or long-term memory when it describes the user's stable preference.
- `preference-identity`, `relationship-note`, `anniversary-date` -> long-term memory first; optionally also a personal/private journal if the user asked for project/file storage.

If a destination is ambiguous, do not scatter the same slice across many files. Ask for the missing project or document.

Keep project storage and memory storage separate. A slice can produce both a project note and a memory update, but the project file should hold the contextual note while the memory update should hold only the stable future-useful fact.

## Memory Extraction Rules

Write or propose long-term memory only for facts that are:

- stated by the user or strongly implied by direct wording;
- stable across weeks or months;
- useful for future assistance;
- not merely a task, passing emotion, or temporary situation;
- allowed by the active system and privacy policy.

Good memory candidates:

- "I am building an AI product workshop."
- "I prefer compact progress digests."
- "My partner is named X."
- "My child's birthday is YYYY-MM-DD."
- "For project Y, always validate route availability separately from DB-backed behavior."

Poor memory candidates:

- "I feel tired today."
- "Remind me to buy milk tomorrow."
- "Tonight at 7 I am having dinner with a friend." Treat this as a calendar event, not long-term memory, unless it is recurring or otherwise important beyond the event itself.
- "A third party's private medical/financial fact."
- "A password, token, or credential."

When writing an ad hoc memory note, keep it small:

```markdown
# Memory update: <short title>

Add/update/delete:
- <durable fact>

Evidence:
- User said: "<short supporting phrase>"

Scope:
- personal | project | relationship | anniversary | preference

Confidence:
- high | medium | low
```

If the evidence is uncertain, ask before writing.
