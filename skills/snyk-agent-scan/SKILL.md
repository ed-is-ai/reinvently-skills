---
name: snyk-agent-scan
description: Scan one agent skill, skill folder or MCP configuration with Snyk Agent Scan and explain the results. Use when asked to run Snyk Agent Scan, to scan a skill or MCP server with Snyk, or to check a downloaded skill before installing it.
---

# Scan a skill with Snyk Agent Scan

[Snyk Agent Scan](https://github.com/snyk/agent-scan) is Snyk's open-source scanner for agent skills and MCP servers. This skill runs it on a single path and explains what it finds.

## Before scanning

- **Check the prerequisites.** It needs [uv](https://docs.astral.sh/uv/) and a `SNYK_TOKEN` environment variable. If the token is not set, tell the user to create a free account at snyk.io, copy the API token from app.snyk.io/account and run `export SNYK_TOKEN=...` themselves. Never ask for the token in chat, and never print it.
- **Tell the user what leaves the machine.** Agent Scan uploads the scanned content to Snyk's analysis API, with secrets redacted. If the skill or configuration is private or internal, ask before scanning.
- **Scan one path, not the whole machine.** Run without a path only if the user asks for a full scan, and warn them first: a full scan discovers every agent configuration and can start the MCP servers it finds.
- **For a skill that is not installed yet,** work on a local copy. Clone it into a new empty temporary directory with `git clone --depth 1 <url> <dir>`, and do not install it.

## Scan

```bash
uvx snyk-agent-scan@latest <path>
```

`<path>` can be a skill folder, a `SKILL.md` file, a skills directory such as `~/.claude/skills`, or an MCP configuration file. Add `--json` if you need to parse the output. Add `--print-full-descriptions` to see untruncated skill text.

If the output says "Daily usage limit reached", tell the user. That is the free tier's limit. Do not retry.

## Report

- Give each finding with the component, the file, the risk name and Snyk's severity, then one plain sentence on what it means for this skill.
- State what was not scanned, such as files Agent Scan skipped or reported errors for.
- If there are no findings, say so, and add: "A clean scan is not clearance. Read the skill before installing it." For a full manual review, use the `vet-agent-skill` skill in this repository.
- Do not fix, edit or delete anything the scan flags unless the user asks.
