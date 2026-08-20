from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
ROOT_PAGES = [
    "index.html",
    "case-studies.html",
    "chartstead.html",
    "how-it-works.html",
    "masthead.html",
    "pip.html",
    "resume.html",
    "solutions.html",
    "tools.html",
]
INCLUDED_PAGES = [ROOT / name for name in ROOT_PAGES] + sorted((ROOT / "blog").glob("*.html"))
EXCLUDED_TOOLS = [
    ROOT / "audit/index.html",
    ROOT / "calculator/index.html",
    ROOT / "intake/index.html",
    ROOT / "scorecard/index.html",
]


class ShellParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.body_classes: set[str] = set()
        self.stylesheets: list[str] = []
        self.local_assets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "body":
            self.body_classes.update((values.get("class", "") or "").split())
        if tag == "link" and values.get("rel") == "stylesheet":
            self.stylesheets.append(values.get("href", "") or "")
        asset = values.get("src") if tag in {"img", "script"} else values.get("href") if tag == "link" else None
        if asset and asset.startswith("/") and not asset.startswith("//"):
            self.local_assets.append(asset)


class SitewideDesignSystemTest(unittest.TestCase):
    def test_every_included_page_loads_the_shared_animas_shell(self) -> None:
        self.assertEqual(len(INCLUDED_PAGES), 36)
        for path in INCLUDED_PAGES:
            with self.subTest(page=path.relative_to(ROOT)):
                parser = ShellParser()
                parser.feed(path.read_text(encoding="utf-8"))
                self.assertIn("animas-site", parser.body_classes)
                self.assertTrue(
                    any(
                        href.startswith("/assets/animas-site.css")
                        for href in parser.stylesheets
                    )
                )

    def test_standalone_tools_remain_outside_the_sitewide_shell(self) -> None:
        for path in EXCLUDED_TOOLS:
            with self.subTest(page=path.relative_to(ROOT)):
                parser = ShellParser()
                parser.feed(path.read_text(encoding="utf-8"))
                self.assertNotIn("animas-site", parser.body_classes)
                self.assertNotIn("/assets/animas-site.css", parser.stylesheets)

    def test_shared_shell_uses_terminal_scan_paths_as_the_default_background(self) -> None:
        source = (ROOT / "assets/animas-site.css").read_text(encoding="utf-8")
        self.assertIn("/assets/animas-line-field-05.svg", source)
        self.assertNotRegex(source, re.compile(r"(?:linear|radial|conic)-gradient\s*\(", re.I))

    def test_included_pages_do_not_reintroduce_rounded_or_gradient_utilities(self) -> None:
        banned = re.compile(r"(?:^|:)(?:rounded(?:-|$)|[^\s]*gradient[^\s]*|from-|via-|to-)")
        for path in INCLUDED_PAGES:
            source = path.read_text(encoding="utf-8")
            class_values = re.findall(r'class="([^"]*)"', source)
            tokens = [token for value in class_values for token in value.split()]
            violations = [token for token in tokens if banned.search(token)]
            with self.subTest(page=path.relative_to(ROOT)):
                self.assertEqual(violations, [])

    def test_included_pages_use_the_single_blue_brand_accent_family(self) -> None:
        legacy_accents = re.compile(
            r"(?:text|bg|border)-(?:teal|amber|emerald|rose|cyan)-|"
            r"#(?:dfe8d7|f4f1e8|e8eef2|a7f3d0)",
            re.I,
        )
        for path in INCLUDED_PAGES:
            source = path.read_text(encoding="utf-8")
            with self.subTest(page=path.relative_to(ROOT)):
                self.assertIsNone(legacy_accents.search(source))

    def test_included_pages_reference_existing_local_assets(self) -> None:
        for path in INCLUDED_PAGES:
            parser = ShellParser()
            parser.feed(path.read_text(encoding="utf-8"))
            for asset in parser.local_assets:
                local_path = ROOT / urlsplit(asset).path.lstrip("/")
                with self.subTest(page=path.relative_to(ROOT), asset=asset):
                    self.assertTrue(local_path.is_file(), f"Missing local asset: {asset}")


if __name__ == "__main__":
    unittest.main()
