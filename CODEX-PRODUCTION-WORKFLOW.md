# Codex Production Workflow

## Purpose

This workflow tells Codex how to safely improve Wholelychit repositories without wasting Gerry's time or breaking working sites.

## Main rule

Codex does the file work directly.

Do not ask Gerry to paste, create, or update files manually.

## First files to read

For any website repository, read these first when present:

1. `README.md`
2. `AGENTS.md`
3. `AGENT-INSTRUCTIONS.md`
4. `LOCKED-CHECKPOINT.md`
5. `FILE-MANAGEMENT.md`
6. `PROJECT-STATUS.md`
7. `DEPLOYMENT-NOTES.md`
8. `CHANGELOG.md`

## Safe production queue

For each active website repo:

1. Confirm tech stack.
2. Keep the current stack.
3. Check homepage title.
4. Check meta description.
5. Check canonical URL.
6. Check navigation links.
7. Check footer links.
8. Check required legal links.
9. Check `robots.txt`.
10. Check `sitemap.xml`.
11. Check mobile layout.
12. Check primary user action.
13. Fix safe issues directly.
14. Commit each useful safe change.
15. Record blockers.
16. Continue to next safe item.

## Stack protection

Do not switch a simple HTML/CSS/JS website to React, Vite, Next.js, TypeScript, or a build tool unless the repo already uses that stack or Gerry clearly asks for a rebuild.

Do not delete major working code.

Do not replace a working architecture with a starter template.

## Commit rules

Commit useful changes with clear messages.

Good commit messages:

- `Add launch checklist`
- `Improve homepage SEO metadata`
- `Add robots and sitemap files`
- `Update footer legal links`
- `Document production workflow`

Avoid vague commit messages:

- `update`
- `fix`
- `changes`
- `stuff`

## Blocker rules

If blocked, do not stop the full queue. Record the blocker and continue with the next safe item.

Blockers include:

- blocked write access
- unclear repo state
- major code deletion needed
- framework migration requested by mistake
- private keys or tokens needed
- payment setup
- live tracking setup
- live ad setup
- domain/account permissions needed

## Report format

After a work batch, report:

1. Repos checked.
2. Files changed.
3. Commits made.
4. Issues fixed.
5. Blocked items.
6. Next safe queue.

Keep reports short and practical.

## Default priority order

1. ReadEasy30
2. MathEasy30
3. PetNeeds.ai
4. Resturants.ai
5. SlotsFreeUSA
6. Marketing-system maintenance

## Quality bar

Each useful change should make the project clearer, safer, faster, easier to maintain, easier to launch, or easier to monetize later.
