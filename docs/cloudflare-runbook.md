# Animas Cloudflare production runbook

## Production architecture

- Canonical repository: `MayberryDT/animas-ai`, branch `master`.
- Cloudflare Worker: `animas-ai-preview`.
- Public domains: `https://animasai.co`, `https://www.animasai.co`, and `https://animas-ai.animasai.co`.
- Cloudflare Worker Builds watches `master` and creates a production Worker version after each push.
- `wrangler.jsonc` serves the repository as static assets through `cloudflare/worker.js`.
- The Worker preserves explicit `.html` URLs, rewrites legacy short routes internally, applies security headers, and returns true 404 responses.

## Normal article publication

1. Create and QA the article and native PNG.
2. Commit and push the clean `master` commit.
3. Allow Cloudflare Worker Builds to deploy the commit.
4. Run:

```bash
python3 scripts/check-cloudflare-site.py https://animasai.co
```

5. Verify the new article URL, PNG URL, and sitemap entry before marking the draft published.

## Manual Cloudflare deployment

Halla has a protected Wrangler OAuth session for operator recovery. From a clean checkout:

```bash
python3 scripts/deploy-cloudflare.py --dry-run
python3 scripts/deploy-cloudflare.py
python3 scripts/check-cloudflare-site.py https://animasai.co
```

The helper pins Wrangler `4.114.0`, refuses dirty checkouts, and never prints the OAuth token.

## Verification contract

The verifier checks:

- every URL in `sitemap.xml`;
- every referenced article PNG;
- `/calculator`, `/intake`, `/audit`, `/scorecard`, and `/resume`;
- required security headers;
- exact `.html` URL behavior;
- true 404 handling;
- protection of `.git`, `.wrangler`, and Wrangler config paths.

## Rollback

List versions:

```bash
CLOUDFLARE_API_TOKEN=<protected-token> npx --yes wrangler@4.114.0 versions list --name animas-ai-preview
```

Rollback to the last verified version:

```bash
CLOUDFLARE_API_TOKEN=<protected-token> npx --yes wrangler@4.114.0 rollback <version-id> --name animas-ai-preview --message "Rollback failed Animas deployment" --yes
python3 scripts/check-cloudflare-site.py https://animasai.co
```
