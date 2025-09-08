import argparse, pathlib
from utils import ensure_dirs, DATA, get_release_config, download

parser = argparse.ArgumentParser()
parser.add_argument("--version", required=True)
args = parser.parse_args()

ensure_dirs()
rel_cfg, sources = get_release_config(args.version)
dl_root = DATA/"downloads"/f"eba_{args.version}"

# taxonomies
for i, url in enumerate(sources.get("taxonomies_zip", []), start=1):
    download(url, dl_root/f"taxonomies_{i}.zip")

# dpm
dpm = sources.get("dpm", {})
if "accdb" in dpm:
    download(dpm["accdb"], dl_root/"dpm.accdb")
if "csv_bundle" in dpm:
    download(dpm["csv_bundle"], dl_root/"dpm_csv.zip")

# rules
rules = sources.get("rules", {})
for key, url in rules.items():
    # derive extension or file name from url
    ext = pathlib.Path(url).suffix or ".bin"
    download(url, dl_root/f"{key}{ext}")
