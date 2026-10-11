#!/usr/bin/env python3
"""Generate static project-card data from explicitly selected public GitHub repos."""
import argparse
import json
import os
import re
import ssl
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = re.compile(r"[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9_.-]+\Z")


def selection(path):
    items = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(items, list) or not items:
        raise ValueError("Select at least one repository")
    seen = set()
    for item in items:
        name = item.get("repository", "")
        if not REPOSITORY.fullmatch(name) or name.lower() in seen:
            raise ValueError("Invalid or duplicate repository selection")
        if not isinstance(item.get("title"), str) or not item["title"].strip():
            raise ValueError("Each project needs a title")
        seen.add(name.lower())
    return items


def project_data(item, payload):
    name = item["repository"]
    if payload.get("private") is not False:
        raise ValueError(f"Refusing non-public repository: {name}")
    if payload.get("full_name", "").lower() != name.lower():
        raise ValueError(f"Repository identity mismatch: {name}")
    for key in ["stargazers_count", "forks_count"]:
        if type(payload.get(key)) is not int or payload[key] < 0:
            raise ValueError(f"Invalid {key}: {name}")
    license_info = payload.get("license") or {}
    license_name = license_info.get("spdx_id")
    return {
        "repository": name,
        "title": item["title"].strip(),
        "url": f"https://github.com/{name}",
        "description": payload.get("description") or "",
        "stars": payload["stargazers_count"],
        "forks": payload["forks_count"],
        "language": payload.get("language") or None,
        "license": license_name if license_name and license_name != "NOASSERTION" else None,
        "archived": payload.get("archived") is True,
    }


def fetch_repository(name, token):
    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2026-03-10",
               "User-Agent": "Jingming-GitHub-Project-Cards"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(f"https://api.github.com/repos/{name}", headers=headers)
    context = ssl.create_default_context(cafile=os.environ.get("SSL_CERT_FILE") or None)
    with urlopen(request, timeout=20, context=context) as response:
        return json.load(response)


def cached_selection_matches(path, items):
    try:
        cached = json.loads(path.read_text(encoding="utf-8"))
        # Never silently retain a removed project, or substitute a different list.
        return (cached.get("source") == "GitHub REST API" and
                [p["repository"] for p in cached["projects"]] ==
                [i["repository"] for i in items] and bool(cached.get("updated_at")))
    except (OSError, ValueError, KeyError, TypeError):
        return False


def refresh(config, output):
    items = selection(config)
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    try:
        projects = [project_data(item, fetch_repository(item["repository"], token))
                    for item in items]
    except (HTTPError, URLError, TimeoutError) as exc:
        # 401/404 are configuration/visibility problems, not transient fallback cases.
        transient = not isinstance(exc, HTTPError) or exc.code in [403, 429, 500, 502, 503, 504]
        if transient and cached_selection_matches(output, items):
            print("::warning::GitHub data refresh failed; retaining the previous dated snapshot.",
                  file=sys.stderr)
            return False
        raise
    snapshot = {"source": "GitHub REST API",
                "updated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "projects": projects}
    output.parent.mkdir(parents=True, exist_ok=True)
    # Do not truncate the last good snapshot if writing is interrupted.
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=output.parent,
                                     delete=False) as handle:
        temporary = Path(handle.name)
        json.dump(snapshot, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    try:
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)
    print(f"Updated {len(projects)} public project(s) from GitHub REST API.")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=ROOT / "_data/github_repositories.json")
    parser.add_argument("--output", type=Path, default=ROOT / "_data/github_projects.json")
    args = parser.parse_args()
    try:
        refresh(args.config, args.output)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        # No tokens, request headers, or API payloads are logged.
        print(f"Project data refresh failed ({type(exc).__name__}).", file=sys.stderr)
        sys.exit(1)
