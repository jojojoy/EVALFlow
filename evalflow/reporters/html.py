from pathlib import Path
from jinja2 import Template
from typing import Dict, List, Any

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>EVALFlow Report</title>
  <style>
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; margin: 24px; }
    h1, h2 { margin: 0.2em 0; }
    table { border-collapse: collapse; width: 100%; margin-top: 16px; }
    th, td { border: 1px solid #ddd; padding: 8px; vertical-align: top; }
    th { text-align: left; }
    code { background: #f6f8fa; padding: 2px 4px; border-radius: 4px; }
    .kpi { display: inline-block; padding: 8px 12px; margin-right: 12px; border: 1px solid #eee; border-radius: 8px; }
  </style>
</head>
<body>
  <h1>EVALFlow Report</h1>
  <div>
    {% for k, v in aggregate.items() %}
      <span class="kpi"><strong>{{k}}</strong>: {{ '%.4f' % v }}</span>
    {% endfor %}
  </div>

  {% if baseline_aggregate %}
    <h2>Δ vs Baseline</h2>
    <ul>
      {% for k in aggregate.keys() %}
        <li>{{k}}: {{ '%.4f' % (aggregate[k] - baseline_aggregate.get(k, 0)) }}</li>
      {% endfor %}
    </ul>
  {% endif %}

  <h2>Samples (first 50)</h2>
  <table>
    <thead>
      <tr><th>#</th><th>Input</th><th>Prediction</th><th>Reference</th></tr>
    </thead>
    <tbody>
      {% for row in rows[:50] %}
      <tr>
        <td>{{loop.index}}</td>
        <td>{{row["input"]}}</td>
        <td>{{row["prediction"]}}</td>
        <td>{{row["reference"]}}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</body>
</html>
"""

def render_html(out_dir: Path, rows: List[Dict[str, Any]], aggregate: Dict[str, float], baseline_aggregate=None):
    html = Template(TEMPLATE).render(rows=rows, aggregate=aggregate, baseline_aggregate=baseline_aggregate)
    (out_dir / "report.html").write_text(html, encoding="utf-8")
