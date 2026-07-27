#!/usr/bin/env python3
"""Deploy the current clean Animas checkout with Halla's Wrangler OAuth session."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess
import sys
import tomllib

WRANGLER_VERSION = "4.114.0"
ACCOUNT_ID = "e0f9e82703380afb5e7022ade62b906c"
AUTH_PATH = Path.home() / ".config/.wrangler/config/default.toml"


def run(command: list[str], *, env: dict[str, str] | None = None) -> None:
    completed = subprocess.run(command, env=env, check=False)
    if completed.returncode:
        raise SystemExit(completed.returncode)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--allow-dirty", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    os.chdir(root)

    status = subprocess.run(
        ["git", "status", "--porcelain"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    if status and not args.allow_dirty:
        print("Refusing Cloudflare deploy from a dirty checkout.", file=sys.stderr)
        return 2

    if not AUTH_PATH.is_file():
        print(f"Wrangler OAuth config is missing: {AUTH_PATH}", file=sys.stderr)
        return 2

    wrangler = ["npx", "--yes", f"wrangler@{WRANGLER_VERSION}"]

    # Let Wrangler refresh its OAuth session before reading the resulting token.
    run([*wrangler, "whoami"])
    auth = tomllib.loads(AUTH_PATH.read_text(encoding="utf-8"))
    token = auth.get("oauth_token")
    if not token:
        print("Wrangler OAuth token is missing after refresh.", file=sys.stderr)
        return 2

    env = os.environ.copy()
    env["CLOUDFLARE_API_TOKEN"] = token
    env["CLOUDFLARE_ACCOUNT_ID"] = ACCOUNT_ID

    command = [*wrangler, "deploy"]
    if args.dry_run:
        command.append("--dry-run")
    run(command, env=env)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
