# v0.3 citation audit

The following organization repositories were checked for APA labels and copied
FHR citation prose: FHR-Specification, FHR-File-Converter, FHR-Citation,
FHT-Specification, FHT-File-Converter, fair-bioheaders.github.io, .github, and
gff-schema. The first six contain affected material and have coordinated changes.
The organization profile and gff-schema contained no matching FHR APA citation
prose in the audited text files. Binary files and historical Git revisions are
outside the current documentation audit.

The FHT READMEs reused FHR DOIs while labeling them as FHT resources. The updates
identify them as related FHR citations; they do not invent FHT DOIs or claim the
FHT tools themselves are archived under the FHR identifiers. Website publication
metadata now uses the same Chicago bibliography entry and DOI.

Author/year checks used the concept DOI records resolved during this update:
- Converter concept 10.5281/zenodo.6762547 resolves to record 10668911, dated
  2024-02-16, with David Molik and Adam Wright as deposited creators.
- Specification concept 10.5281/zenodo.6762549 resolves to record 6762550, dated
  2022-06-27, with David Molik as deposited creator; the historical archive title
  predates the FHR project rename.
- The published paper is 10.1093/bib/bbae122, volume 25, issue 3, article bbae122,
  2024. Its full author list is preserved.

The preprint is retained in citation.bib with its historical key and DOI;
the published paper is the recommended general citation. Existing BibTeX keys
are unchanged. Machine-readable CFF metadata distinguishes the resource DOI from
its preferred paper citation. Repository contributors/authors in CFF are separate
from the historical deposited specification authorship.

Verification: all three CFF files validate against CFF 1.2.0; citation.bib parses
with its four distinct entries when nonstandard software entries are enabled.

## Files and coordinated pull requests

| Repository | Audited citation files | Implementation PR |
| --- | --- | --- |
| FHR-Specification | README.md; CITATION.cff | [#28](https://github.com/FAIR-bioHeaders/FHR-Specification/pull/28) |
| FHR-File-Converter | README.md; CITATION.cff | [#19](https://github.com/FAIR-bioHeaders/FHR-File-Converter/pull/19) |
| FHR-Citation | README.md; citation.bib; CITATION.cff | [#2](https://github.com/FAIR-bioHeaders/FHR-Citation/pull/2) |
| FHT-Specification | README.md | [#1](https://github.com/FAIR-bioHeaders/FHT-Specification/pull/1) |
| FHT-File-Converter | README.md | [#1](https://github.com/FAIR-bioHeaders/FHT-File-Converter/pull/1) |
| fair-bioheaders.github.io | _publications/2024-05-31-title-number1.md | [#3](https://github.com/FAIR-bioHeaders/fair-bioheaders.github.io/pull/3) |
| .github | profile/README.md | No affected citations |
| gff-schema | README.md and tracked text documentation | No affected citations |

The concept DOIs intentionally identify evolving specification/software resources;
they are not version-specific v0.3 archive identifiers. No new v0.3 DOI is claimed.
The historical preprint remains machine-readable metadata, rather than replacing
the preferred published article. FHT resources without independently verified DOIs
retain repository links; the FHR citations identify related resources.

The six implementation PRs listed above have merged.

## v0.3.0 archives

The coordinated v0.3.0 release was deposited on 2026-10-07 with creators David Molik
and Adam Wright: specification version DOI 10.5281/zenodo.23224136 and converter
version DOI 10.5281/zenodo.23224137. Both concept DOIs above now resolve to these
records. Use the version DOIs to cite the exact v0.3.0 archives; reporting-contact
updates made on main after the tag are not included in them.
