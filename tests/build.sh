#!/bin/sh
# Assemble the test set in tests/work/: our samples, generated large files, Snyk's
# ToxicSkills demo skills and Anthropic's public skills at pinned commits.
set -eu
cd "$(dirname "$0")"
GOOF_SHA=80ce2e06f52fd384163c4bd6778676019723773c      # snyk-labs/toxicskills-goof
ANTHROPIC_SHA=e4bb5d960d87126ff3b3a8af1a104b7db67560ba # anthropics/skills
rm -rf work && mkdir -p work/malicious work/clean
cp -R samples/malicious/. work/malicious/
cp -R samples/clean/. work/clean/

# Padding: payload at the top, then 22 MB of filler (the evasion Unit 42 described).
p=work/malicious/pdf-page-counter
{ cat "$p/README.md.head"; i=0; while [ $i -lt 22 ]; do head -c 1048576 /dev/zero | tr '\0' ' '; i=$((i+1)); done; } > "$p/README.md"
rm "$p/README.md.head"

# A legitimate 2 MB asset, which should be a WARN at most.
mkdir -p work/clean/sales-sample-data/assets
python3 -c "
import random; random.seed(1)
print('order_id,date,region,product,units,price')
for i in range(30000): print(f'{i},2026-{random.randint(1,12):02d}-{random.randint(1,28):02d},{random.choice([\"North\",\"South\",\"East\",\"West\"])},P{random.randint(1,40)},{random.randint(1,20)},{random.randint(5,500)}.00')
" > work/clean/sales-sample-data/assets/sales.csv

fetch() { # repo sha dest
  git init -q "$3" && git -C "$3" fetch -q --depth 1 "https://github.com/$1.git" "$2" && git -C "$3" checkout -q FETCH_HEAD
}
fetch snyk-labs/toxicskills-goof "$GOOF_SHA" work/.goof
for s in google vercel clawhub; do cp -R "work/.goof/.agents/skills/$s" "work/malicious/goof-$s"; done
fetch anthropics/skills "$ANTHROPIC_SHA" work/.anthropic
for s in pdf docx xlsx pptx skill-creator mcp-builder webapp-testing frontend-design brand-guidelines internal-comms; do
  cp -R "work/.anthropic/skills/$s" "work/clean/anthropic-$s"
done
rm -rf work/.goof work/.anthropic
echo "built: $(ls work/malicious | wc -l | tr -d ' ') malicious, $(ls work/clean | wc -l | tr -d ' ') clean"
