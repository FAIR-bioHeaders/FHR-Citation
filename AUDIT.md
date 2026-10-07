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
