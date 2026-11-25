# Contributing

1. Open an issue describing the skill, failure mode, expected behavior, and a **synthetic** input example.
2. Keep the `skills/<name>/SKILL.md` purpose and stop conditions explicit.
3. Separate `FACT / PLAN / HYPOTHESIS / NEEDS_CONFIRMATION` and cite source locations.
4. Never invent baselines, owners, or external approvals.
5. For cross-team dependencies, identify accountable result owners and data denominators.
6. For metric changes, update acceptance evidence and audit gates.
7. Run `python scripts/validate_trace.py examples/sample_trace.json` and `python -m compileall -q scripts`.
8. Do not commit credentials, corporate data, client events, identifiable information, or internal roadmaps.

## PR checklist
- [ ] New logic documented in the relevant skill
- [ ] Test/example is fictional
- [ ] No private data or secrets
- [ ] Human approval gates preserved
- [ ] No claim of causal proof from structural validation
