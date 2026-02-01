#!/bin/bash
# Git push with automatic code review via Codex

# Commit message from args or default
MSG="${1:-$(date '+%Y-%m-%d %H:%M')}"

# Commit and push
cd /root/clawd/transcription-automation
git add .
git commit -m "$MSG"
git push origin main

# Spawn sub-agent for code review
echo "🚀 Spawning code review agent..."

# This would spawn a sub-agent - syntax for OpenClaw sessions_spawn
# For now, return the git diff for manual review
git diff HEAD~1 HEAD --stat

# Show all files in repo for review context
echo "📁 Repo contents:"
find . -type f -not -path './.git/*' -not -path './.credentials/*' | head -20
