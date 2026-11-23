#!/bin/sh
# Baseline: the skill's own size check and search command, with no agent. FAIL on any hit.
cd "$(dirname "$0")/work"
for d in malicious/* clean/*; do
  big=$(find "$d" -type f -size +1024k | head -1)
  hits=$(grep -rlIE 'curl|wget|\| *(bash|zsh|sh)|eval|base64|exec\(|subprocess|os\.system|chmod \+x|~/\.ssh|~/\.aws|\.env|id_rsa|keychain|crontab|systemctl|launchctl|LaunchAgents|https?://' "$d" | head -1)
  if [ -n "$big$hits" ]; then echo "$d FAIL"; else echo "$d PASS"; fi
done
