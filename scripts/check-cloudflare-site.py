#!/usr/bin/env python3
"""Validate the public contract of an Animas Cloudflare deployment."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class ImageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.images: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "meta" and values.get("property") == "og:image" and values.get("content"):
            self.images.add(values["content"])


def request(opener, url: str) -> tuple[int, dict[str, str], bytes]:
    request_object = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 Animas-Deployment-Verifier/1.0"},
    )
    try:
        response = opener.open(request_object, timeout=30)
    except urllib.error.HTTPError as error:
        return error.code, dict(error.headers.items()), error.read()
    with response:
        return response.status, dict(response.headers.items()), response.read()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("base_url")
    args = parser.parse_args()
    base = args.base_url.rstrip("/")
    opener = urllib.request.build_opener(NoRedirect())
    failures: list[str] = []

    def check(path: str, expected: int = 200) -> bytes:
        code, headers, body = request(opener, base + path)
        normalized_headers = {name.lower(): value for name, value in headers.items()}
        if code != expected:
            failures.append(f"{path}: expected {expected}, got {code}")
        if code == 200:
            for name in ("content-security-policy", "strict-transport-security", "x-content-type-options", "x-frame-options"):
                if name not in normalized_headers:
                    failures.append(f"{path}: missing {name}")
        return body

    home = check("/")
    if b'<link rel="canonical" href="https://animasai.co/">' not in home:
        failures.append("/: canonical URL is missing or wrong")

    base_parts = urllib.parse.urlsplit(base)
    if base_parts.hostname == "animasai.co":
        redirect_path = "/blog/"
        redirect_query = f"canonical-probe={time.time_ns()}"
        www_url = urllib.parse.urlunsplit(
            (base_parts.scheme, "www.animasai.co", redirect_path, redirect_query, "")
        )
        code, headers, _ = request(opener, www_url)
        location = next((value for name, value in headers.items() if name.lower() == "location"), "")
        expected_location = f"https://animasai.co/blog/?{redirect_query}"
        if code != 308:
            failures.append(f"www canonical redirect: expected 308, got {code}")
        if location != expected_location:
            failures.append(
                f"www canonical redirect: expected {expected_location}, got {location or '<missing>'}"
            )

    sitemap = check("/sitemap.xml")
    check("/robots.txt")
    for path in ("/calculator", "/intake", "/audit", "/scorecard", "/resume"):
        check(path)
    for path in (
        "/definitely-not-a-real-animas-page",
        "/.git/config",
        "/.wrangler/cache/pages.json",
        "/netlify.toml",
        "/wrangler.jsonc",
    ):
        check(path, 404)

    image_paths: set[str] = set()
    try:
        root = ET.fromstring(sitemap)
        namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locations = [node.text for node in root.findall("s:url/s:loc", namespace) if node.text]
    except ET.ParseError as error:
        failures.append(f"sitemap.xml: invalid XML: {error}")
        locations = []

    for location in locations:
        parsed = urllib.parse.urlparse(location)
        path = parsed.path or "/"
        body = check(path)
        if path.endswith(".html") and not body:
            failures.append(f"{path}: empty HTML response")
        content_type = ""
        image_parser = ImageParser()
        try:
            image_parser.feed(body.decode("utf-8"))
        except UnicodeDecodeError:
            pass
        for image in image_parser.images:
            image_paths.add(urllib.parse.urlparse(image).path)

    for path in sorted(image_paths):
        body = check(path)
        if not body.startswith(b"\x89PNG\r\n\x1a\n"):
            failures.append(f"{path}: expected a PNG payload")

    if failures:
        print("Animas Cloudflare contract FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        "Animas Cloudflare contract passed: "
        f"{len(locations)} sitemap URLs, {len(image_paths)} article images, short routes, security headers, and 404 behavior."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
