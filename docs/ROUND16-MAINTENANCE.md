# Round 16B citation maintenance — 2026-11-20

Refs FAIR-bioHeaders/FAIR-bioHeaders-Specification#211. Base `a5dca66`.
Continues prior policy commit `f61ddd5`; no citation bytes, stable keys, author
order, DOIs, reviewed record baseline or license notices are changed.

README now distinguishes historical v0.3 documentation from current maintenance,
provides clean setup and important checker APIs/errors, and corrects obsolete
wording that asked readers to keep the already-closed #8 open. Rendering/style
compatibility and live DOI checks remain explicitly unimplemented.

Independent configured `nrp/qwen3` reviewed all first-party scripts, workflow,
manifest, citation source, README and pending diff read-only; no executed checks
are attributed to that model. Confirmed usability fixes: bad CLI input paths now
report concise errors, documentation checks reject non-Markdown inputs, and
repository-root link resolution no longer depends on the working directory.
Regressions exercise all three. Existing malformed-entry, explicit-comment,
duplicate, identity and Unicode controls remain unchanged and pass.

## Bounded scan receipts

On Python 3.13.16: pinned bibtexparser 1.4.3 and pyparsing 3.2.3 installed into
an isolated environment. `python -m unittest discover -s tests -v` passed after
changes; citation and owned Markdown CLI checks passed. Markdownlint-cli2 0.23.2
matches the pinned action v24.2.0 dependency and passes the two owned files.

- Gitleaks 8.30.1: `gitleaks git --log-opts=--all --redact=100`, zero matches.
- Bandit 1.8.6 under Python 3.13: `bandit -r scripts -f json`, zero findings
  and zero scanner errors.
- pip-audit 2.9.0: `pip-audit --no-deps -r requirements-ci.txt --format json`,
  both exact pinned parser packages have zero known advisories as queried.
- zizmor 1.16.3: all workflow files, zero findings.
- actionlint 1.7.12: workflow syntax check passed.

These are bounded checks, not proof of no vulnerabilities. The parser uses a
private recovery hook intentionally pinned and covered by malformed-entry tests;
upgrades require those tests and source review. Tool installation uses network
access; the checks themselves are offline. Action transitives are not separately
resolved/advisory-audited. Source BibTeX retains historical license provenance.

## Cleanup and human handoff

Other branches/worktrees are retained pending ownership/activity proof. No
historical record, tag, release or unknown work is removed. The PR contains the
attributed review and every finding disposition, current head/checks and these
limitations. Agents never merge; a human reviews and merges through normal controls.
