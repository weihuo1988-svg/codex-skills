# Codex Skills

This repository stores Codex skills developed for my personal workflows.

Each skill lives in its own top-level folder. A skill folder should keep the standard Codex skill structure:

```text
skill-name/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
```

Only include folders a skill actually uses. For example, a skill without references should not create an empty `references/` folder.

## Skills

- `capture-mobile-dictation`: Capture Codex mobile dictation, split it into structured slices, route notes into project documents, handle calendar items, and extract long-term memory candidates.

## Publishing Rule

When adding or updating a skill in this repository:

1. Keep the repository root for this README and repository-level files.
2. Put each skill in a separate folder named exactly like the skill.
3. Copy the complete skill contents into that folder, including `SKILL.md`, `agents/`, and any used `references/`, `scripts/`, or `assets/`.
4. Validate the skill before committing.
5. Commit and push the repository only after confirming the top-level layout is still one folder per skill.
