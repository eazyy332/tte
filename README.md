# TTE — EBA Taxonomy & DPM Hub (Fetcher • Normalizer • Validators)

This repo **does not redistribute** EBA packages. It provides scripts to:
- **Fetch** official EBA taxonomy/DPM/rule packages into `data/`
- **Unpack & normalize** folder layout per version
- **Validate** XBRL instances via Arelle (OSS) or Altova RaptorXML (commercial)
- **Extract** DPM tables to CSV (when EBA provides CSV bundles or after local export)

> Compliance: artifacts are fetched from official EBA URLs; `data/` is gitignored.

## Quick start

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -U pip -r requirements.txt

# See configured releases
python scripts/list_releases.py

# Fetch, then unpack a release (example: 4.0)
python scripts/fetch_eba_release.py --version 4.0
python scripts/unpack_taxonomy.py --version 4.0

# Extract DPM to CSV (uses CSV bundle if present)
python scripts/extract_dpm_csv.py --version 4.0

# Validate an instance with Arelle
python scripts/validate_instance_arelle.py --instance data/samples/finrep_sample.xbrl --version 4.0
```

## Layout (after fetch)

```text
data/
  downloads/eba_4.0/*.zip
  taxonomies/4.0/{corep,finrep,...}/...
  dpm/4.0/{CSV tables or ACCDB}
  rules/4.0/{filing_rules.pdf, validation_list.xlsx, parsed_rules.json}
  samples/ (optional, keep tiny)
```

## Notes
- **Arelle** CLI must be installed (`arelleCmdLine` in your PATH).
- **Altova RaptorXML** is optional; see `tools/altova/README.md`.
- Fill **official EBA URLs** in `config/sources.json`.
