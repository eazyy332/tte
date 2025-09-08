.PHONY: setup list-releases fetch unpack dpm-csv validate-arelle validate-altova clean

PY=python3

setup:
	@$(PY) -m venv .venv && . .venv/bin/activate && pip install -U pip
	@. .venv/bin/activate && pip install -r requirements.txt || true
	@echo "Remember to copy config/env.example to .env and set variables if needed."

list-releases:
	@$(PY) scripts/list_releases.py

fetch:
	@if [ -z "$(VERSION)" ]; then echo "Usage: make fetch VERSION=4.0"; exit 1; fi
	@$(PY) scripts/fetch_eba_release.py --version $(VERSION)

unpack:
	@if [ -z "$(VERSION)" ]; then echo "Usage: make unpack VERSION=4.0"; exit 1; fi
	@$(PY) scripts/unpack_taxonomy.py --version $(VERSION)

dpm-csv:
	@if [ -z "$(VERSION)" ]; then echo "Usage: make dpm-csv VERSION=4.0"; exit 1; fi
	@$(PY) scripts/extract_dpm_csv.py --version $(VERSION)

validate-arelle:
	@if [ -z "$(FILE)" ]; then echo "Usage: make validate-arelle FILE=path/to/file.xbrl VERSION=4.0"; exit 1; fi
	@$(PY) scripts/validate_instance_arelle.py --instance $(FILE) --version $(VERSION)

validate-altova:
	@if [ -z "$(FILE)" ]; then echo "Usage: make validate-altova FILE=path/to/file.xbrl VERSION=4.0"; exit 1; fi
	@$(PY) scripts/validate_instance_altova.py --instance $(FILE) --version $(VERSION)

clean:
	rm -rf data/downloads/* data/taxonomies/* data/dpm/* data/rules/*
