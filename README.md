# Codex Skills

This repository stores Codex skills developed for my personal workflows.

Each skill lives in its own top-level folder. A skill folder should keep the Codex skill files it actually uses:

```text
skill-name/
├── SKILL.md
├── agents/          # optional
│   └── openai.yaml
├── references/      # optional
├── scripts/         # optional
└── assets/          # optional
```

Only include folders a skill actually uses. For example, a skill without references should not create an empty `references/` folder.

## Skills

- `andrej-karpathy-skill`: Apply Karpathy-inspired coding-agent checks for assumptions, scoped edits, simplicity, and verification.
- `capture-mobile-dictation`: Capture Codex mobile dictation, split it into structured slices, route notes into project documents, handle calendar items, and extract long-term memory candidates.
- `create-story-seeds`: Turn vague fiction sparks into archived urban romance or melodrama story seeds through a lightweight dialogue.
- `grill-me`: Interview the user through a plan or design until the decision tree is fully stress-tested.
- `submit-skill-to-github`: Validate a Codex skill, place it in its own folder in this repository, commit it, push it to GitHub, and verify the remote commit.
- `write-xhs-jiedilian-notes`: Generate Xiaohongshu-style 姐弟恋/年下恋 notes from viral screenshots while respecting account positioning.
- `write-xhs-qinzi-notes`: Generate Xiaohongshu-style 亲子/单亲妈妈 notes from viral screenshots or topic briefs while respecting account positioning.

## Publishing Rule

When adding or updating a skill in this repository:

1. Keep the repository root for this README and repository-level files.
2. Put each skill in a separate folder named exactly like the skill.
3. Copy the complete skill contents into that folder, including `SKILL.md`, `agents/`, and any used `references/`, `scripts/`, or `assets/`.
4. Validate the skill before committing.
5. Commit and push the repository only after confirming the top-level layout is still one folder per skill.
