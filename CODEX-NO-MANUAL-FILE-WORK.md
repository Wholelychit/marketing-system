# Codex No Manual File Work

## Problem

Production slows down when AI asks Gerry to create files, paste files, update files, or approve routine safe work manually.

## Solution

AI and Codex must do file work directly through repository tools.

Use repository instructions so every active website follows the same rule.

## Approval setting

For Codex CLI production work, use the approval setting that removes routine approval pauses:

`--ask-for-approval never`

Use it with workspace write access for normal website production tasks:

`codex exec --ask-for-approval never --sandbox workspace-write "Review this repo, fix safe issues directly, commit useful changes, and report what changed."`

Do not use broad bypass modes unless the environment is externally hardened.

## Required repo file

Every active website repo needs `AGENTS.md`.

That file must say:

- AI and Codex do file work directly.
- Do not ask Gerry to create files.
- Do not ask Gerry to paste files.
- Do not ask Gerry to update files.
- Do not ask Gerry for thumbs-up approval on routine safe edits.
- Use direct file updates for normal website work.
- Use full-file updates when cleaner than small patches.
- Commit useful changes with clear messages.

## Active repos covered

- readeasy30.com
- matheasy30.com
- my-petneeds
- restaurantaibot.com
- slotsfreeusa.com
- marketing-system

## Codex task wording

Use this wording for Codex tasks:

Review the repo. Fix safe issues directly. Create, edit, or replace files yourself when needed. Do not ask Gerry to paste, update files, or give thumbs-up approval for routine safe edits. Keep the current tech stack. Commit useful changes. Stop only for blocked writes, major code deletion, framework changes, private keys, payment setup, live tracking, live ads, or unclear repo state.

## Faster production rule

Do not create long plans before simple fixes.

Review files, fix safe issues, commit, and continue.
