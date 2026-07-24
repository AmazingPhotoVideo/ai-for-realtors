import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("page_builder", ROOT / "scripts" / "build.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)

class PropertyPageBuildTests(unittest.TestCase):
    def setUp(self):
        self.listing = json.loads((ROOT / "data" / "listing.sample.json").read_text())
        self.branding = json.loads((ROOT / "data" / "branding.sample.json").read_text())

    def test_sample_data_validates(self):
        self.assertEqual([], builder.validate(self.listing, self.branding))

    def test_all_designs_build_without_placeholders_and_keep_attribution(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "site"
            built = builder.build(ROOT / "data" / "listing.sample.json", ROOT / "data" / "branding.sample.json", output, "https://property.example.com/demo", ROOT / "assets")
            self.assertEqual(set(builder.DESIGNS), {p.name for p in built})
            pages = []
            for target in built:
                page = (target / "index.html").read_text()
                pages.append(page)
                self.assertFalse(builder.TOKEN_RE.search(page))
                self.assertIn("Property marketing toolkit by Amazing Photo Video", page)
                self.assertIn("https://amazingphotovideo.com", page)
                self.assertIn("static page for one listing", page)
                self.assertTrue((target / "app.js").is_file())
                self.assertTrue((target / "assets" / "sample-exterior.svg").is_file())
            self.assertEqual(3, len(set(pages)), "design templates must be genuinely distinct")

    def test_dangerous_urls_are_rejected(self):
        for bad in ("javascript:alert(1)", "data:text/html,bad", "//evil.example/x", "../secret.jpg", "http://insecure.example/x"):
            listing = copy.deepcopy(self.listing)
            listing["media"]["gallery"][0]["src"] = bad
            self.assertTrue(any("URL" in error for error in builder.validate(listing, self.branding)), bad)

    def test_endpoint_requires_https_and_no_credentials(self):
        for bad in ("http://forms.example/lead", "https://user:pass@forms.example/lead", "javascript:alert(1)"):
            branding = copy.deepcopy(self.branding)
            branding["form"]["endpoint"] = bad
            self.assertTrue(any("endpoint" in error for error in builder.validate(self.listing, branding)), bad)

    def test_missing_required_facts_are_reported(self):
        listing = copy.deepcopy(self.listing)
        listing["description"] = ""
        listing["agent"]["brokerage"] = ""
        errors = builder.validate(listing, self.branding)
        self.assertIn("missing required fact: description", errors)
        self.assertIn("missing required fact: agent.brokerage", errors)

    def test_price_and_custom_address_rules(self):
        listing = copy.deepcopy(self.listing)
        listing["price"] = {"visible": True, "currency": "CAD"}
        listing["address"]["display"] = "custom"
        listing["address"]["customLabel"] = ""
        errors = builder.validate(listing, self.branding)
        self.assertTrue(any("price.amount" in e for e in errors))
        self.assertTrue(any("address.customLabel" in e for e in errors))

    def test_json_ld_omits_unknown_and_hidden_price(self):
        listing = copy.deepcopy(self.listing)
        listing["price"]["visible"] = False
        listing["specs"].pop("interiorSize")
        data = builder.json_ld(listing, self.branding, "https://property.example.com/demo")
        self.assertNotIn("offers", data)
        self.assertNotIn("floorSize", data)
        self.assertNotIn("numberOfBedrooms", builder.json_ld({**listing, "specs": {**listing["specs"], "bedrooms": None}}, self.branding, "https://property.example.com/demo"))

    def test_gallery_requires_alt_text(self):
        listing = copy.deepcopy(self.listing)
        listing["media"]["gallery"][0]["alt"] = ""
        self.assertTrue(any("meaningful alt" in e for e in builder.validate(listing, self.branding)))

    def test_structured_values_and_open_house_timezone_are_validated(self):
        listing = copy.deepcopy(self.listing)
        listing["features"] = "not-a-list"
        listing["specs"]["bedrooms"] = -2
        listing["openHouses"][0]["start"] = "2026-08-08T14:00:00"
        errors = builder.validate(listing, self.branding)
        self.assertTrue(any("features must" in e for e in errors))
        self.assertTrue(any("specs.bedrooms" in e for e in errors))
        self.assertTrue(any("with timezone" in e for e in errors))

if __name__ == "__main__":
    unittest.main()
