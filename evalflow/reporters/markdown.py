from pathlib import Path
from typing import Dict, List, Any

def render_md(out_dir: Path, rows: List[Dict[str, Any]], aggregate: Dict[str, float], baseline_aggregate=None):
    lines = ["# EVALFlow Report"]
    for k, v in aggregate.items():
        lines.append(f"- **{k}**: {v:.4f}")
    if baseline_aggregate:
        lines.append("\n## Δ vs Baseline")
        for k in aggregate.keys():
            base = baseline_aggregate.get(k, 0)
            lines.append(f"- {k}: {aggregate[k]-base:.4f}")
    lines.append("\n## Samples (first 20)\n")
    lines.append("| # | Input | Prediction | Reference |")
    lines.append("|---|-------|------------|-----------|")
    for i, r in enumerate(rows[:20], 1):
        lines.append(f"| {i} | {r['input'][:60]} | {r['prediction'][:60]} | {r['reference'][:60]} |")
    (out_dir / "report_extra.md").write_text("\n".join(lines), encoding="utf-8")
