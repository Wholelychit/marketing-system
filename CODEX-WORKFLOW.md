# Codex Workflow

Last updated: 2026-05-28

## Purpose

Codex is the main workflow for routine GitHub repository editing across Wholelychit projects.

The goal is simple: Gerry should not waste time manually pasting, creating, replacing, repairing, or updating repo files when Codex can safely do that work directly.

## Why Codex Is Used

Codex is better for multi-file repository work because it can:

- read the repository first
- understand the current file structure
- keep the existing tech stack
- create safe new files
- update existing files
- repair broken files
- commit useful changes
- continue through a safe queue without stopping after one tiny task

## Why the ChatGPT GitHub Connector Is Secondary

The ChatGPT GitHub connector may show internal write-action names like `create_file` or `update_file`.

Those labels can make it look like Gerry is being asked to manually create or update files. That is confusing and slows the work down.

For that reason, the ChatGPT GitHub connector should be used only for:

- small file reads
- quick repo checks
- reviewing file contents
- emergency single-file edits when Codex is unavailable

Routine repo editing should happen in Codex.

## Primary Rule

Do not ask Gerry to paste, create, replace, or update repo files manually.

When write access is available, Codex should create, update, replace, repair, and commit safe files directly.

## Required Codex Work Pattern

1. Read the repo first.
2. Check `README.md`.
3. Check `AGENTS.md`.
4. Check `AGENT-INSTRUCTIONS.md` if present.
5. Check `PROJECT-STATUS.md` if present.
6. Check any locked checkpoint or file-management notes if present.
7. Keep the current tech stack.
8. Do not migrate frameworks.
9. Do not delete major working code.
10. Make safe edits directly.
11. Commit each useful group of changes.
12. Continue through the safe queue until blocked.
13. Report only after several useful commits or a real blocker.

## Real Blockers Only

Stop only for:

- missing repo permission
- account sign-in problem
- credentials or private keys
- billing or payment setup
- live ads
- live tracking scripts
- framework migration
- major code deletion
- unclear production risk that cannot be safely repaired

## Safe Work Codex Can Do Directly

Codex may directly handle:

- Markdown documentation updates
- README updates
- AGENTS.md updates
- PROJECT-STATUS.md updates
- CODEX-WORKFLOW.md updates
- robots.txt updates
- sitemap.xml updates
- SEO checklist updates
- launch checklist updates
- content planning files
- campaign files
- simple HTML updates
- simple CSS updates
- simple JavaScript repairs
- broken link fixes
- footer/navigation cleanup
- accessibility improvements
- mobile layout improvements
- safe copy improvements

## Work Not Allowed Without Direct Approval

Do not proceed without direct approval for:

- private keys
- API tokens
- payment processing
- checkout setup
- billing setup
- live ad network scripts
- live tracking scripts
- deleting major working code
- changing the site framework
- switching to React, Vite, Next.js, TypeScript, or build tools unless the repo already uses them and the project checkpoint allows it

## Future Wholelychit Starter Repo Recommendation

Future repos should start from a simple template that already includes:

- `README.md`
- `AGENTS.md`
- `PROJECT-STATUS.md`
- `CODEX-WORKFLOW.md`
- `robots.txt`
- `sitemap.xml`
- `SEO-CHECKLIST.md`
- `LAUNCH-CHECKLIST.md`
- `REVIEW-CHECKLIST.md`
- basic `/css` and `/js` folders when the site is static
- clear deployment notes

This avoids repeating setup work and keeps every repo ready for Codex-first production edits.

## Commit Message Examples

Use clear commit messages such as:

- `Add Codex workflow documentation`
- `Update agent instructions for direct repo edits`
- `Add project status and safe queue`
- `Add SEO checklist`
- `Update launch checklist`

## Final Operating Rule

Codex should keep moving through safe repo work without making Gerry babysit routine file changes.

Record blockers. Commit safe progress. Report only when useful work is complete or a real blocker appears.
