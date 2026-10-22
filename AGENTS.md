# Agent instructions

## Repository context

This repository maintains `citation.bib` and human-readable citation guidance.
Keep the paper, shared specification, toolkit and biological dataset identities
separate. Type-development clones do not inherit a DOI or citation identity merely
by containing copied files. Verify current citation metadata against the actual
publisher/DOI records when changing it; preserve BibTeX keys, author order, title
and historical records. Concept DOIs and immutable version DOIs serve different
purposes. Never invent a release date or archival record.

Read README and LICENSE. Review BibTeX syntax/escaping and compare human and
machine-readable records after edits; run available repository checks. An
AGENTS.md-only change needs diff/link review and `git diff --check`.

## Schema additions and their own development cycle

A new optional field, structured alternative, enum value, constraint, required
field or changed meaning is a schema-contract change, even when motivated by a
UI, exporter, parser fix or documentation task. Identify it explicitly as a
**schema addition** or other contract change in its issue and PR. Supporting an
already adopted field in a consumer is implementation work, not a new field.

Schema additions have their own proposal, review, compatibility, versioning and
release cycle. Keep them separately reviewable from routine fixes, website work,
packaging and dependency updates; link dependent implementation PRs rather than
silently adopting a field downstream. Shared fields/objects and cross-type rules
belong in FAIR-bioHeaders-Specification; type-specific design starts in the owning
development repository and is coordinated into shared publication. Name affected
types, requiredness, semantics, mappings, serializers and conformance fixtures.

During active construction of FHP, FHT and FHGFF3, maintainers may iterate on draft
fields with lighter process and include coordinated schema/implementation work in
one clearly scoped PR. Record the proposal and compatibility impact in that PR;
this flexibility does not make every field adopted or supported. Preserve already
published contracts and cited versions, label draft behavior, and obtain joint
maintainer review before publication. FHR additions retain the separate cycle.
Do not apply draft flexibility to released FHP/FHGFF3 schemas retroactively.

Use the shared specification's `docs/SCHEMA-VERSIONS.md` and
`schemas/versions.json`: contract versions are per type, distinct from repository
release tags and biological resource versions. Additive changes that preserve all
valid values and meanings qualify for a minor increment; invalidating records or
changing meanings requires a major increment. Do not assign a new version merely
for implementing an existing contract. Never rewrite immutable releases, fixed
schema aliases or existing file-bound headers as incidental cleanup. Header edits
require checksum recomputation and may affect downstream parent links.

Check the adoption decision and released support before implementing a proposal;
an issue or PR's existence does not establish adoption. Structured vouchers
(FAIR-bioHeaders-Specification#139/#140) and mapping profiles (#56 in that same
repository) have their own review history. Implemented subsets do not establish
full profile or header-family support. The mapping page tracked in
fair-bioheaders.github.io#29 depends on approved profiles. Recheck these records
rather than relying on a copied description of their temporary status.

## Citation verification and consumer updates

For changes to `citation.bib`, parse it with a named BibTeX parser and check the
rendered ordinary citation with a stated compatible tool/style; record versions
and any unsupported entry types. Run the parser/consistency checks documented in README; rendering remains a
separate unimplemented lane, so a parser success is not a render test. Check braces/case preservation, corporate authors, Unicode/TeX escaping,
DOIs and stable entry keys. Plain Markdown/link checks do not validate BibTeX.

Reconcile human-readable README entries and machine-readable records against the
same cited sources. A repository/package rename does not rename a registered
bibliographic title or change its DOI/creator order. Website citation records live
in `_data/references.yml` in fair-bioheaders.github.io and render/export through
its reference include and citation JavaScript. Link a companion update when a
verified citation changes; do not assume this repository automatically propagates
there, or replace website data without checking its current resource identities.

## CI commands and boundaries

Use Python 3.13 and `requirements-ci.txt`. Run `python -m unittest discover -s
tests -v` (one command), `python scripts/check_citations.py`, and
`python scripts/check_docs.py AGENTS.md README.md`. Markdown lint is configured
in `.markdownlint.json`; README gives the pinned CLI command. The offline record
manifest is reviewed evidence, not a substitute for checking authoritative sources
when metadata changes. Do not refresh it to conceal drift or silence the known
license/URL review notes. Preserve source BibTeX values; renderer/remote checks are
still follow-ups in #8. CI runs on documentation-only changes too.

## Issue, project and code-review behavior

### Issues and the connected project

- Add every issue you work on to the connected project (project #9, "FAIR
  BioHeaders — 2026 refresh") and set `Status` to `In Progress` when work starts.
- Keep `Status` current as the work moves (`Todo`, `In Progress`, `Blocked`,
  `Blocked - In Progress`, `Done`), and set `Outcome` when it closes.
- Link every PR to its issue (`Closes #N` or `Refs #N`). Do not do unreported work.
- After each work run (implementation, tests, review pass), post a status comment
  on the issue or PR: what changed, checks run and results, commit/PR links,
  blockers, and the next action. Do not rely on chat history.

### Code review on a PR

When a PR receives code review (human or Copilot):

1. Read the overall review and every inline comment before changing anything.
2. Make each fix in a **new commit**. Do not amend or force-push over reviewed
   commits; if a rebase is required, cite the new head in the replies.
3. Reply to each inline finding with the fix and the relevant commit hash.
4. Resolve that inline comment/thread.
5. After all findings are handled, post an overall reply to the review
   summarizing each finding's disposition and the commits.
6. Treat optional suggestions as required unless they are genuinely out of
   scope; state why and link a follow-up issue.

Do not push to a repository's main branch or merge a PR without maintainer
approval.
