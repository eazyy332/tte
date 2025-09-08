import argparse, zipfile, pathlib
from utils import ensure_dirs, DATA

parser = argparse.ArgumentParser()
parser.add_argument("--version", required=True)
args = parser.parse_args()

ensure_dirs()
dl_root = DATA/"downloads"/f"eba_{args.version}"
tx_root = DATA/"taxonomies"/args.version
tx_root.mkdir(parents=True, exist_ok=True)

for z in sorted(dl_root.glob("taxonomies_*.zip")):
    with zipfile.ZipFile(z) as zf:
        zf.extractall(tx_root)

print(f"Unpacked taxonomies → {tx_root}")
