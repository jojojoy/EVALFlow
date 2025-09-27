from pathlib import Path
import json
import os

def ensure_dir(path):
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p

def read_jsonl(path):
    items = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            items.append(json.loads(line))
    return items

def write_json(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)

def write_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def load_baseline_metrics(baseline_path):
    if not baseline_path:
        return None
    p = Path(baseline_path)
    if p.is_dir():
        p = p / "metrics.json"
    if not p.exists():
        return None
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)
