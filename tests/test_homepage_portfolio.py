from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SHIPPED_PRODUCTS = [
    "Masthead",
    "ChartStead",
    "Pip",
    "Hotel Cleaning Schedule",
    "Executioner",
    "Milkbench",
    "Rat Detective Online",
    "Wargus TypeScript",
]


class HomepageParser(HTMLParser):
    VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

    def __init__(self) -> None:
        super().__init__()
        self.in_main = False
        self.main_depth = 0
        self.top_level_sections = 0
        self.current_section = 0
        self.current_home_section = ""
        self.current_card: dict[str, object] | None = None
        self.card_depth = 0
        self.capture_heading = False
        self.cards: list[dict[str, object]] = []
        self.home_sections: list[str] = []
        self.numbered_cards: list[str] = []
        self.rounded_classes: list[str] = []
        self.work_heading = ""
        self.capture_work_heading = False
        self.work_header_paragraphs = 0
        self.work_header_labels = 0
        self.work_backgrounds: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        class_names = values.get("class", "") or ""
        self.rounded_classes.extend(
            token for token in class_names.split() if "rounded" in token
        )

        if tag == "main":
            self.in_main = True
            self.main_depth = 0
            return

        if not self.in_main:
            return

        if tag == "section" and self.main_depth == 0:
            self.top_level_sections += 1
            self.current_section = self.top_level_sections
            self.current_home_section = values.get("data-home-section", "") or ""
            if self.current_home_section:
                self.home_sections.append(self.current_home_section)

        if tag not in self.VOID_TAGS:
            self.main_depth += 1

        if self.current_home_section == "work" and self.current_card is None:
            if tag == "h2":
                self.capture_work_heading = True
            elif tag == "p":
                self.work_header_paragraphs += 1
            if "work-sheet-label" in class_names.split():
                self.work_header_labels += 1
            if tag == "img" and "data-work-background" in values:
                self.work_backgrounds.append(values.get("src", "") or "")

        if "data-project-card" in values:
            self.current_card = {
                "section": self.current_section,
                "home_section": self.current_home_section,
                "title": "",
                "images": 0,
                "links": 0,
            }
            self.card_depth = self.main_depth
            if values.get("data-index"):
                self.numbered_cards.append(values["data-index"])

        if self.current_card is not None:
            if tag in {"h2", "h3"}:
                self.capture_heading = True
            elif tag == "img":
                self.current_card["images"] = int(self.current_card["images"]) + 1
            elif tag == "a" and values.get("href"):
                self.current_card["links"] = int(self.current_card["links"]) + 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "main" and self.in_main:
            self.in_main = False
            return

        if not self.in_main:
            return

        if tag in {"h2", "h3"}:
            self.capture_heading = False
        if tag == "h2":
            self.capture_work_heading = False

        if self.current_card is not None and self.main_depth == self.card_depth:
            self.cards.append(self.current_card)
            self.current_card = None
            self.card_depth = 0

        if tag not in self.VOID_TAGS:
            self.main_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.capture_work_heading:
            self.work_heading = (self.work_heading + data).strip()
        if self.current_card is not None and self.capture_heading:
            self.current_card["title"] = (
                str(self.current_card["title"]) + data
            ).strip()


class HomepagePortfolioTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.parser = HomepageParser()
        cls.parser.feed(cls.source)

    def test_work_section_exposes_every_shipped_product(self) -> None:
        self.assertEqual(
            [card["title"] for card in self.parser.cards],
            SHIPPED_PRODUCTS,
        )
        self.assertTrue(
            all(card["home_section"] == "work" for card in self.parser.cards),
            "Every shipped product must appear in the Work section.",
        )

    def test_each_project_card_has_visual_proof_and_a_destination(self) -> None:
        self.assertEqual(len(self.parser.cards), len(SHIPPED_PRODUCTS))
        for card in self.parser.cards:
            with self.subTest(product=card["title"]):
                self.assertEqual(card["images"], 1)
                self.assertGreaterEqual(card["links"], 1)

    def test_homepage_uses_no_rounded_utility_classes(self) -> None:
        self.assertEqual(self.parser.rounded_classes, [])

    def test_original_homepage_sections_remain_present(self) -> None:
        self.assertEqual(
            self.parser.home_sections,
            ["hero", "services", "work", "thesis", "founder", "contact"],
        )
        self.assertEqual(
            self.parser.top_level_sections,
            6,
            "The integrated design must preserve the full six-section homepage.",
        )

    def test_project_cards_do_not_display_numeric_indices(self) -> None:
        self.assertEqual(self.parser.numbered_cards, [])

    def test_work_header_is_a_single_unannotated_statement(self) -> None:
        self.assertEqual(
            self.parser.work_heading,
            "A working set of shipped products.",
        )
        self.assertEqual(self.parser.work_header_paragraphs, 0)
        self.assertEqual(self.parser.work_header_labels, 0)

    def test_work_section_uses_selected_terminal_scan_background(self) -> None:
        self.assertEqual(
            self.parser.work_backgrounds,
            ["/assets/animas-line-field-05.svg"],
        )

    def test_hero_uses_split_identity_and_message_cards(self) -> None:
        hero = self.source.split('<section data-home-section="hero"', 1)[1].split(
            "</section>", 1
        )[0]
        shell_class = hero.split('class="home-hero-shell', 1)[1].split('"', 1)[0]
        self.assertIn('class="home-hero-profile"', hero)
        self.assertIn('class="home-hero-message"', hero)
        self.assertNotIn("relative", shell_class)
        self.assertNotIn("z-10", shell_class)
        self.assertNotIn("PRACTICAL AI SYSTEMS", hero)
        self.assertNotIn("Agents and internal tools", hero)
        self.assertNotIn("Product-minded builder", hero)
        self.assertNotIn('href="mailto:', hero)
        self.assertIn(
            'href="/case-studies.html" class="w-full sm:w-auto px-8 py-4 bg-slate-950',
            hero,
        )

    def test_contact_section_uses_contrast_safe_panel(self) -> None:
        contact = self.source.split('data-home-section="contact"', 1)[1].split(
            "</section>", 1
        )[0]
        self.assertIn('class="home-contact-panel', contact)
        self.assertIn('class="home-contact-copy"', contact)
        self.assertIn('class="home-contact-actions"', contact)


class WorkPageTest(unittest.TestCase):
    def test_masthead_case_study_uses_image_first_vertical_layout(self) -> None:
        source = (ROOT / "case-studies.html").read_text(encoding="utf-8")
        masthead = source.split('<article class="bg-slate-950', 1)[1].split(
            '<article class="bg-[#edf4f6]', 1
        )[0]
        self.assertLess(masthead.index("masthead-product-showcase.jpg"), masthead.index('<div class="p-8 md:p-12">'))
        self.assertIn("aspect-[2/1]", masthead)
        self.assertNotIn("lg:grid-cols", masthead)


if __name__ == "__main__":
    unittest.main()
