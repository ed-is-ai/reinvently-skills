# Reinvently skills

Agent skills published alongside [Reinvently](https://reinvently.co.uk) research. Each one is short enough to read in full before you install it. Please do.

| Skill | What it does | Write-up |
|---|---|---|
| [vet-agent-skill](skills/vet-agent-skill/SKILL.md) | Reviews a third-party agent skill for security risks before you install it. Read-only: it never runs the skill under review. | [How to vet an AI agent skill before you install it](https://reinvently.co.uk/blog/how-to-vet-ai-agent-skill/) |

## Install

Read the `SKILL.md` first. Then copy the skill folder into your agent's skills directory. For Claude Code:

```bash
git clone --depth 1 https://github.com/ed-is-ai/reinvently-skills.git
cp -r reinvently-skills/skills/vet-agent-skill ~/.claude/skills/
```

Pin to the commit you reviewed, and review the diff before updating.

## vet-agent-skill

Ask your agent to check a skill folder, `SKILL.md` or repository URL before you install it. It clones the skill into a temporary directory, flags oversized files, runs [Snyk Agent Scan](https://github.com/snyk/agent-scan) if `SNYK_TOKEN` is set, reads every instruction and script, lists every external URL, checks the publisher, and returns PASS, WARN or FAIL with the evidence for each finding.

Snyk Agent Scan needs a free Snyk account, has a daily limit on the free tier, and uploads the skill's content to Snyk for analysis. The skill asks before scanning a private or internal skill.

A clean result is not clearance. Scanners and reviews both miss things.

## Licence

MIT. See [LICENSE](LICENSE).
