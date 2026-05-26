# AGENTS.md

## Codex no-pause rule

For routine safe website production, do not pause for thumbs-up approval.

Keep working through safe tasks until the requested batch is complete or a real blocker appears.

## Safe tasks that do not need another approval

- fix broken links
- fix file paths
- improve page copy
- improve mobile layout
- update README files
- update instruction files
- add simple planning files
- remove obvious duplicate non-working files after checking references
- improve HTML and CSS without changing the stack

## Stop only for real blockers

Stop only if:

- a tool blocks the write
- a change would delete major working code
- a change would change the framework or build system
- credentials or private keys are involved
- payment setup is involved
- live tracking or live ads are involved
- the repository state is unclear after checking files

## Production rhythm

1. Read README and AGENT-INSTRUCTIONS.
2. Check current files.
3. Make the safest useful edit.
4. Commit the edit.
5. Continue to the next safe edit.
6. Report after several useful commits.

## Tech rule

Keep simple website repos on HTML, CSS, and JavaScript unless the owner clearly requests a rebuild.
