import os, subprocess, argparse
from utils import DATA

parser = argparse.ArgumentParser()
parser.add_argument("--instance", required=True)
parser.add_argument("--version", required=True)
args = parser.parse_args()

RAPTOR = os.environ.get("RAPTORXML", "raptorxmlxbrl")
taxo_dir = DATA / "taxonomies" / args.version

cmd = [
    RAPTOR,
    "validate-xbrl",
    "--taxonomy-package", str(taxo_dir),
    args.instance
]
print(" ".join(cmd))
subprocess.run(cmd, check=False)
