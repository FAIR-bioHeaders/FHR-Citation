import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_citations import check_consistency, parse_records


class Citations(unittest.TestCase):
    def setUp(self):
        self.text = (ROOT / "citation.bib").read_text()
        self.records = parse_records(self.text)
        self.manifest = json.loads((ROOT / "tests/expected-records.json").read_text())
        self.readme = (ROOT / "README.md").read_text()

    def test_maintained_records(self):
        check_consistency(self.records, self.manifest, self.readme)
        self.assertEqual(len(self.records), 4)
        self.assertEqual(self.records["FHR_File_Converter"]["ENTRYTYPE"], "software")

    def test_duplicate_key(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            parse_records(self.text + self.text)

    def test_malformed_entry_is_not_silently_dropped(self):
        for fragment in ["@misc{broken,title={Oops}", "@misc{broken,title = }",
                         "% background comment\n@misc{broken,title = }"]:
            with self.subTest(fragment=fragment), self.assertRaisesRegex(ValueError, "malformed"):
                parse_records(self.text + "\n" + fragment)

    def test_explicit_comment_examples_are_not_rejected(self):
        records = parse_records(self.text + "\n@comment{@misc{illustrative}}")
        self.assertEqual(set(records), set(self.records))

    def test_missing_fields(self):
        with self.assertRaisesRegex(ValueError, "missing required"):
            parse_records("@article{x,title={X},author={A},year={2026}}")

    def test_bad_year_and_resolver_doi(self):
        for old, new in [("year = {2026}", "year = {today}"),
                         ("doi = {10.5281/zenodo.6762547}", "doi = {https://doi.org/10.5281/zenodo.6762547}")]:
            with self.subTest(new=new), self.assertRaises(ValueError):
                parse_records(self.text.replace(old, new, 1))

    def test_corporate_authors_unicode_and_protected_text(self):
        text = r"""@misc{example, author={{Example Genome Consortium} and García, Ana},
        title={{DNA} and A\&B}, year={2026}, doi={10.1234/example}, url={https://example.org}}"""
        entry = parse_records(text)["example"]
        self.assertEqual(entry["author"], "{Example Genome Consortium} and García, Ana")
        self.assertEqual(entry["title"], r"{DNA} and A\&B")

    def test_identity_and_author_order_changes_fail(self):
        for field, value in [("doi", "10.1234/other"), ("author", "Wright, Adam and Molik, David"),
                             ("title", "Another resource"), ("year", "2025")]:
            changed = copy.deepcopy(self.records)
            changed["FHR_Specification"][field] = value
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, field):
                check_consistency(changed, self.manifest, self.readme)

    def test_readme_drift_fails(self):
        with self.assertRaisesRegex(ValueError, "README"):
            check_consistency(self.records, self.manifest, self.readme.replace("Data set. 2026", "Data set. 2025"))

    def test_key_changes_require_review(self):
        changed = dict(self.records)
        changed.pop("Wright2024")
        with self.assertRaisesRegex(ValueError, "keys"):
            check_consistency(changed, self.manifest, self.readme)
