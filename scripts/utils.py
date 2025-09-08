import os, sys, json, yaml, pathlib, shutil
from dotenv import load_dotenv
from rich import print
from rich.progress import Progress
import requests

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config"
DATA = ROOT / "data"

load_dotenv(ROOT / ".env")

def load_yaml(p):
    with open(p, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_json(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def ensure_dirs():
    for p in [DATA, DATA/"downloads", DATA/"taxonomies", DATA/"dpm", DATA/"rules", DATA/"samples"]:
        p.mkdir(parents=True, exist_ok=True)

def download(url, out_path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with Progress() as progress:
        task = progress.add_task(f"Downloading {url}", total=None)
        with requests.get(url, stream=True, timeout=180) as r:
            r.raise_for_status()
            with open(out_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024*64):
                    if chunk:
                        f.write(chunk)
        progress.update(task, completed=1)
    print(f"[green]Saved → {out_path}[/green]")

def get_release_config(version: str):
    rels = load_yaml(CONFIG/"eba_releases.yml")["releases"]
    if version not in rels:
        print(f"[red]Unknown version: {version}[/red]"); sys.exit(1)
    key = rels[version]["sources_key"]
    sources = load_json(CONFIG/"sources.json")[key]
    return rels[version], sources

def move_unpacked(src, dest):
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        shutil.rmtree(dest)
    shutil.move(str(src), str(dest))
