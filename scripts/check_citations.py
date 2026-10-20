"""Offline syntax, identity and README consistency checks; does not render TeX."""
import argparse
import json
from pathlib import Path
import re

from bibtexparser.bparser import BibTexParser

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "article": {"author", "title", "year", "journal", "doi"},
    "misc": {"author", "title", "year", "doi", "url"},
    "software": {"author", "title", "year", "doi", "url"},
}


def normalize(value):
    return " ".join(value.split())


def parse_records(text):
    parser = BibTexParser(ignore_nonstandard_types=False)
    implicit_comments = []
    # Pinned bibtexparser 1.4.3 exposes no public strict-recovery flag. Observe
    # only its implicit-comment production: explicit @comment examples are valid.
    # Keep this integration covered when upgrading the parser.
    parser._expr.implicit_comment.add_parse_action(
        lambda source, location, tokens: implicit_comments.append(tokens[0])
    )
    database = parser.parse(text, partial=False)
    # bibtexparser preserves malformed entries as implicit comments, even with
    # partial=False. Do not silently treat a dropped entry as successful parsing.
    for comment in implicit_comments:
        if re.search(r"(?m)^\s*@[A-Za-z]+\s*[{(]", comment):
            raise ValueError("unparsed/malformed BibTeX declaration: " + comment[:80])
    if not database.entries:
        raise ValueError("no citation entries parsed")
    records = {}
    for entry in database.entries:
        key = entry["ID"]
        if key in records:
            raise ValueError(f"{key}: duplicate citation key")
        kind = entry["ENTRYTYPE"]
        if kind not in REQUIRED:
            raise ValueError(f"{key}: unsupported entry type {kind}; review its field rules")
        missing = [field for field in sorted(REQUIRED[kind]) if not entry.get(field, "").strip()]
        if missing:
            raise ValueError(f"{key}: missing required fields: {', '.join(missing)}")
        if not re.fullmatch(r"[0-9]{4}", entry["year"]):
            raise ValueError(f"{key}: year must have four digits")
        if not re.fullmatch(r"10\.[0-9]+(?:\.[0-9]+)*/\S+", entry["doi"]):
            raise ValueError(f"{key}: expected a bare DOI, not a resolver URL")
        records[key] = entry
    return records


def check_consistency(records, manifest, readme):
    expected = manifest["records"]
    if set(records) != set(expected):
        raise ValueError("citation keys differ from reviewed record manifest")
    for key, rule in expected.items():
        for field, value in rule["fields"].items():
            if normalize(records[key].get(field, "")) != normalize(value):
                raise ValueError(f"{key}.{field}: differs from reviewed record manifest")
        if rule.get("readme_citation") and normalize(rule["readme_citation"]) not in normalize(readme):
            raise ValueError(f"{key}: maintained README citation differs from reviewed record")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bib", type=Path, default=ROOT / "citation.bib")
    parser.add_argument("--readme", type=Path, default=ROOT / "README.md")
    args = parser.parse_args()
    try:
        records = parse_records(args.bib.read_text(encoding="utf-8"))
        manifest = json.loads((ROOT / "tests/expected-records.json").read_text())
        check_consistency(records, manifest, args.readme.read_text(encoding="utf-8"))
    except (ValueError, KeyError) as exc:
        parser.exit(1, f"Citation check failed: {exc}\n")
    print(f"Checked {len(records)} citation records and maintained README entries offline.")
    for note in manifest["known_discrepancies"]:
        print("REVIEW NOTE: " + note)
    print("Rendering, style compatibility and live DOI metadata were not checked.")


if __name__ == "__main__":
    main()
