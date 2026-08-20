from __future__ import annotations

from pathlib import Path
import re
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
PROTOTYPE = ROOT / "docs/design/animas-work-background-directions.html"
GENERATED = ROOT / "docs/design/generated"
DIRECTION_NAMES = [
    "Routed Circuit Traces",
    "Processor Pin Fan-Out",
    "Signal Ring Array",
    "Angular Data Lanes",
    "Terminal Scan Paths",
    "Network Bus Weave",
    "Chip Interconnect Field",
    "Packet Route Mesh",
    "Diagnostic Vector Field",
    "Machine Schematic Channels",
]


class BackgroundDirectionsTest(unittest.TestCase):
    def test_generator_emits_dense_uniform_cyber_line_fields(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory)
            subprocess.run(
                [
                    "node",
                    str(ROOT / "scripts/generate-animas-line-fields.mjs"),
                    "--output",
                    str(output),
                ],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            files = sorted(output.glob("animas-line-field-*.svg"))

            self.assertEqual(len(files), 10)
            namespace = {"svg": "http://www.w3.org/2000/svg"}
            geometries: set[str] = set()
            for path in files:
                with self.subTest(path=path.name):
                    root = ET.parse(path).getroot()
                    lines = root.findall(".//svg:path", namespace)
                    self.assertGreaterEqual(
                        sum(line.attrib.get("d", "").count("M") for line in lines),
                        140,
                    )
                    self.assertEqual(
                        {(line.attrib.get("stroke"), line.attrib.get("stroke-opacity"), line.attrib.get("stroke-width")) for line in lines},
                        {("#2563eb", "0.08", "1")},
                    )
                    geometries.add("".join(line.attrib.get("d", "") for line in lines))

            self.assertEqual(len(geometries), 10)

    def test_prototype_uses_ten_generated_line_fields(self) -> None:
        source = PROTOTYPE.read_text(encoding="utf-8")
        for index, name in enumerate(DIRECTION_NAMES, start=1):
            with self.subTest(direction=name):
                self.assertIn(name, source)
                self.assertIn(f"animas-line-field-{index:02d}.svg", source)

    def test_every_direction_is_a_static_line_only_svg(self) -> None:
        files = sorted(GENERATED.glob("animas-line-field-*.svg"))
        self.assertEqual(len(files), 10)
        namespace = {"svg": "http://www.w3.org/2000/svg"}
        for path in files:
            with self.subTest(path=path.name):
                root = ET.parse(path).getroot()
                self.assertEqual(root.attrib.get("viewBox"), "0 0 1600 2200")
                self.assertEqual(root.attrib.get("aria-hidden"), "true")
                paths = root.findall(".//svg:path", namespace)
                self.assertGreaterEqual(len(paths), 8)
                self.assertTrue(all(node.attrib.get("fill") == "none" for node in paths))
                self.assertEqual(root.findall(".//svg:linearGradient", namespace), [])
                self.assertEqual(root.findall(".//svg:radialGradient", namespace), [])

    def test_prototype_css_contains_no_gradients_or_rounded_shapes(self) -> None:
        source = PROTOTYPE.read_text(encoding="utf-8")
        self.assertNotRegex(source, re.compile(r"(?:linear|radial|conic)-gradient\s*\(", re.I))
        radius_values = re.findall(r"border-radius\s*:\s*([^;]+);", source, re.I)
        self.assertTrue(all(value.strip() in {"0", "0px", "0rem", "0em"} for value in radius_values))

    def test_design_system_explicitly_prohibits_gradients_and_pills(self) -> None:
        source = (ROOT / "DESIGN.md").read_text(encoding="utf-8")
        self.assertIn("Gradients are prohibited", source)
        self.assertIn("Pill-shaped", source)


if __name__ == "__main__":
    unittest.main()
