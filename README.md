# FHR Citation

Citation metadata for the FHR paper and FAIR BioHeaders specification/software. Use the published paper for general FHR
citations, and the specification/software DOI for direct use of those resources.
The v0.3 documentation release is historical; current maintenance preserves
registered bibliographic identities and stable entry keys.

[Download citation.bib](citation.bib) or copy the Chicago bibliography entries below.
Existing BibTeX keys are preserved. The preprint remains available as a historical
resource; prefer the published paper when describing the standard.

## Citing FHR

Chicago bibliography entries are used below. Cite the published paper for a
general description of FHR; cite the specification or converter when using that
resource directly. The software and specification links are concept DOIs; for a
specific release, use the corresponding version DOI from Zenodo. Authors and
years follow the records resolved by the concept DOIs at the v0.3 documentation
update, and can change as later records are published.

### Published paper

Wright, Adam, Mark D. Wilkinson, Christopher Mungall, Scott Cain, Stephen Richards, Paul Sternberg, Ellen Provin, Jonathan L. Jacobs, Scott Geib, Daniela Raciti, Karen Yook, Lincoln Stein, and David C. Molik. “FAIR Header Reference Genome: A TRUSTworthy Standard.” *Briefings in Bioinformatics* 25, no. 3 (2024): bbae122. https://doi.org/10.1093/bib/bbae122.

### Specification

Molik, David, and Adam Wright. *FAIR-bioHeaders Specification*. Data set. 2026. https://doi.org/10.5281/zenodo.6762549.

### Converter

Molik, David, and Adam Wright. *FHR File Converter*. Computer software. 2026. https://doi.org/10.5281/zenodo.6762547.

Machine-readable entries are maintained in
[FHR-Citation](https://github.com/FAIR-bioHeaders/FHR-Citation/blob/main/citation.bib).

## Citation metadata audit

The concept DOIs are preserved. Before the v0.3.0 deposit they resolved to records
identifying the converter as a 2024 resource by David Molik and Adam Wright, and the
specification as a 2022 resource by David Molik; both now resolve to the 2026 v0.3.0
records by David Molik and Adam Wright, which the entries above follow. This does not redefine project authorship.
For exact release provenance, select a version DOI from the Zenodo record rather
than assuming a concept DOI identifies a fixed version.

The published paper uses article identifier `bbae122`, volume 25, issue 3. Its
citation year is 2024; the print issue date and online publication date differ.
The software title spelling and specification repository URL have been corrected.

On November 20, 2026, the registered DataCite concept records were checked
again: [specification concept metadata](https://api.datacite.org/dois/10.5281/zenodo.6762549)
names *FAIR-bioHeaders Specification*, while
[toolkit concept metadata](https://api.datacite.org/dois/10.5281/zenodo.6762547)
still names *FHR File Converter*. Both retain David Molik then Adam Wright.
The concept citations above follow those registered titles. The
[toolkit 0.13.1 version metadata](https://api.datacite.org/dois/10.5281/zenodo.24387470)
also retains *FHR File Converter*. The current repository/product name does
not by itself rename a registered bibliographic title. The website's release and citation metadata
are maintained separately in its
[publication update](https://github.com/FAIR-bioHeaders/fair-bioheaders.github.io/pull/70).
No concept DOI, key, author order or historical license field is changed by
this title correction.

## Licensing

[![License: MPL-2.0](https://img.shields.io/badge/License-MPL--2.0-blue.svg)](LICENSE)

New project contributions from March 2025 onward use [MPL-2.0](LICENSE). David Molik left USDA in February 2025. Historical USDA public-domain material remains public domain within the United States; its original notice is preserved in LICENSE. Previously granted permissions and third-party terms remain intact. The project includes both historical material and subsequent MPL-2.0 contributions; file notices and history identify provenance.

## Setup and maintainer API

Use Python 3.13 and an isolated environment. No runtime package is shipped; the checks install only the pinned parser stack. From a clean clone:

```sh
git clone https://github.com/FAIR-bioHeaders/FHR-Citation.git
cd FHR-Citation
python3.13 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-ci.txt
```

`parse_records(text)` in `scripts/check_citations.py` returns a dictionary keyed
by stable BibTeX ID and raises `ValueError` for malformed/duplicate/unsupported
records. It does not normalize or write the source. `check_consistency(records,
manifest, readme)` raises on baseline drift. The CLI accepts `--bib PATH` and
`--readme PATH`, exits 1 for its documented validation failures, and prints the
remaining provenance notes on success. `scripts/check_docs.py` checks local
Markdown targets and whitespace (exit 1 on validation/read failure, exit 2 for
non-Markdown arguments); it does not contact remote services. These are
maintenance helpers, not a supported citation-rendering API. Empty bibliographies
are rejected. Recovery detection intentionally depends on bibtexparser 1.4.3 and
pyparsing 3.2.3 internals; the existing malformed-entry controls must pass before
upgrading either.

Run the checks below after edits. Another actual model reviews every PR, agents
address CI/review findings, and a human performs the merge.

## Automated checks

Pull requests, pushes to `main` and manual runs execute **Citation records** and
**Markdown lint**. The workflow uses Python 3.13, pinned parser dependencies and
read-only permissions. It does not publish releases or change records. Installing
the tools uses the network; the validation logic itself is offline. As verified against its pinned package manifest on 2026-11-20,
markdownlint action v24.2.0 bundles CLI 0.23.2.

```sh
python -m pip install -r requirements-ci.txt
python -m unittest discover -s tests -v
python scripts/check_citations.py
python scripts/check_docs.py AGENTS.md README.md
npx markdownlint-cli2@0.23.2 AGENTS.md README.md
```

The citation checker uses bibtexparser 1.4.3 with nonstandard types enabled, so
`@software` is retained. It rejects duplicate citation keys, unparsed malformed
entries, missing required fields for the supported article/misc/software types,
invalid years and resolver-prefixed DOI fields. Tests exercise corporate authors,
Unicode, protected titles and TeX escapes without normalizing the source file.
These required fields describe this repository's maintained records, not every
valid BibTeX bibliography.

`tests/expected-records.json` is an explicit offline consistency baseline for
entry types, keys, titles, ordered authors, years and DOIs, plus the maintained
README citation lines. Review a changed field against authoritative records,
then update both representations and the baseline deliberately; do not regenerate
the baseline simply to hide a failure. This verifies consistency, not independent
bibliographic truth or live DOI metadata. The preprint remains historical.

The checker reports the converter's existing PDDL-1.0 field and historical
repository URL for separate provenance review. They are not automatically changed
or treated as proof that all current contributions share that license.

Local Markdown checks cover whitespace, conflict markers and inline/reference
file targets, including images. They do not check URL availability, HTML links,
anchors or general Markdown semantics. The `check_docs.py` helper does not handle nested parentheses/brackets or
multiline Markdown destinations. Markdown lint covers the two owned files. Line length is unrestricted and bare
URLs are allowed to preserve the existing human-readable bibliography layout.

### Remaining validation and website handoff

This is the parser/consistency stage of #8. **No bibliography rendering or
style compatibility is claimed.** A later rendering lane must choose and pin a
compatible tool/style; classic BibTeX may not support `@software` without a
reviewed fallback, while a BibLaTeX profile has different capabilities. Remote
DOI/link checks remain a separate scheduled/manual follow-up and must distinguish
service failures from record errors. #8 closed after the offline slice; these limitations remain explicitly outside
that delivered scope and are not represented as tested.

Verified citation changes may need a companion update to website
`_data/references.yml` and its citation tests. The website has its own resource
scope and historical-title rules; these checks neither fetch it nor assume that
its records must match every entry here byte-for-byte.
