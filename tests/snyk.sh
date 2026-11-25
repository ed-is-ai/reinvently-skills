#!/bin/bash
# Run Snyk Agent Scan alone on every sample. Stops at the daily limit; re-run to resume.
# Needs SNYK_TOKEN. Uploads each sample to Snyk.
cd "$(dirname "$0")"; mkdir -p results-snyk
for d in work/malicious/* work/borderline/* work/clean/*; do
  out=results-snyk/$(basename "$(dirname "$d")").$(basename "$d").json
  [ -s "$out" ] && continue
  uvx snyk-agent-scan@latest --json "$d" > "$out" 2> "$out.err"
  if grep -q 'Daily usage limit' "$out" "$out.err"; then rm -f "$out"; echo "limit reached at $d"; exit 1; fi
  echo "$d done"
done
