"""Tally Snyk-only results: highest risk score per sample (0-1000). A failed scan is ERROR, not clean."""
import glob, json, os
from collections import Counter

def worst(path):
    data = json.load(open(path)); risks = {}
    for r in data.get('scan_path_responses', []):
        if r.get('error'): return None, {}
        for s in r.get('skill_risks', []):
            for k, v in (s.get('risk_indexes') or {}).items():
                risks[k] = max(risks.get(k, 0), v.get('score', 0))
    return (max(risks.values()) if risks else 0), risks

def band(score):  # ponytail: fixed bands, tune if Snyk publishes its own thresholds
    return 'ERROR' if score is None else 'HIGH' if score >= 800 else 'MED' if score >= 400 else 'LOW'

tally = {}
for p in sorted(glob.glob('results-snyk/*.json')):
    label, name = os.path.basename(p)[:-5].split('.', 1)
    score, risks = worst(p); b = band(score)
    tally.setdefault(label, Counter())[b] += 1
    top = ', '.join(k for k, v in sorted(risks.items(), key=lambda kv: -kv[1])[:2])
    print(f'{label}/{name:40} {score if score is not None else "-":>5} {b:5} {top}')
print()
for label in ('malicious', 'borderline', 'clean'):
    if label in tally: print(label, dict(tally[label]))
