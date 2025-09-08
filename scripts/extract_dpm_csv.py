import argparse, zipfile, sys
from utils import ensure_dirs, DATA

parser = argparse.ArgumentParser()
parser.add_argument("--version", required=True)
args = parser.parse_args()

ensure_dirs()
dl_root = DATA/"downloads"/f"eba_{args.version}"
dpm_root = DATA/"dpm"/args.version
dpm_root.mkdir(parents=True, exist_ok=True)

csv_zip = dl_root/"dpm_csv.zip"
if csv_zip.exists():
    with zipfile.ZipFile(csv_zip) as zf:
        zf.extractall(dpm_root)
    print(f"Extracted CSV bundle → {dpm_root}")
    sys.exit(0)

accdb = dl_root/"dpm.accdb"
if accdb.exists():
    print("DPM .accdb detected. Export tables to CSV on Windows (Access) and place CSVs here:")
    print(f"  {dpm_root}/tables/*.csv")
else:
    print("No DPM found for this version.")
