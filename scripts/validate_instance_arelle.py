import os, subprocess, argparse
from utils import DATA

parser = argparse.ArgumentParser()
parser.add_argument("--instance", required=True)
parser.add_argument("--version", required=True)
args = parser.parse_args()

ARELLE = os.environ.get("ARELLE_CMD", "arelleCmdLine")
taxo_dir = DATA / "taxonomies" / args.version

cmd = [
    ARELLE,
    "--file", args.instance,
    "--packages", str(taxo_dir),
    "--validate",
    "--calcDecimals",
    "--formulaAssertions",
    "--disclosureSystem", "none"
]

print(" ".join(cmd))
subprocess.run(cmd, check=False)
