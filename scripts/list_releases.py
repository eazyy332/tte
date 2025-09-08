from utils import load_yaml, CONFIG

rels = load_yaml(CONFIG/"eba_releases.yml")["releases"]
for k, v in rels.items():
    print(f"{k}: {v['label']}")
