# AGENTS.md

## Work mode

Operate as a no-local-Git production assistant.

Use ChatGPT 5.5, Codex, GitHub, and Cloudflare-connected publishing where applicable. Do not require local Git, terminal Git, VS Code, or manual file editing.

## Main rule

Use Codex/GitHub access or the ChatGPT GitHub connector to create, update, replace, and commit safe files directly in this repository.

Do not ask Gerry to paste files. Do not ask Gerry to create files. Do not ask Gerry to replace files. Do not ask Gerry to manually update files. Do not stop after one small fix. Work in productive batches.

## Preferred rhythm

Continue through the safe queue until blocked or complete enough for a useful report.

Report only after useful commits or a real blocker. Keep the report short:

- repo worked
- files changed
- commits made
- blockers
- next queue

## Safe work allowed

- README updates
- AGENTS.md updates
- CODEX-WORKFLOW.md updates
- CODEX-CURRENT-TASK.md updates
- PROJECT-STATUS.md updates
- CHANGELOG.md updates
- documentation cleanup
- safe scripts and templates
- planning docs
- checklist files
- non-secret configuration examples
- HTML/CSS/JS fixes if website files exist
- navigation/footer fixes if website files exist
- titles/meta/canonical URLs if website files exist
- sitemap.xml and robots.txt if website publishing applies

## Do not add without direct approval

- private keys
- API keys
- tokens
- live tracking
- live ad scripts
- payment setup
- affiliate links
- account credentials
- production automation that sends messages or spends money
- public AI tools
- upload systems
- user accounts
- ordering integrations
- framework rebuilds
- major code deletion

## Cloudflare rule

Cloudflare Pages should publish from GitHub only when this repo is connected for publishing.

Recommended static setup when applicable:

- Production branch: main
- Build command: blank
- Output directory: .
- No manual file uploads
- No live tracking, ads, payments, or API keys unless approved

## Repository notes

- Repo: Wholelychit/marketing-system
- Purpose: marketing support system for Gerry's websites
- Treat this as a support/planning/tooling repo unless current files clearly show otherwise.
- Never commit secrets or live credentials.
