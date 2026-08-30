#!/usr/bin/env bash
# Standalone skill installer for macOS, Linux, and Git Bash.
# Usage: ./install.sh [--claude|--codex] [--dest PATH]
set -euo pipefail

src="$(cd "$(dirname "$0")" && pwd)"
target="--claude"
destination=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --claude|--codex)
      target="$1"
      shift
      ;;
    --dest)
      if [[ $# -lt 2 ]]; then
        echo "--dest requires a path" >&2
        exit 2
      fi
      destination="$2"
      shift 2
      ;;
    --help|-h)
      echo "Usage: $0 [--claude|--codex] [--dest PATH]"
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      echo "Usage: $0 [--claude|--codex] [--dest PATH]" >&2
      exit 2
      ;;
  esac
done

case "$target" in
  --claude)
    default_destination="$HOME/.claude/skills"
    product="Claude Code"
    ;;
  --codex)
    default_destination="${CODEX_HOME:-$HOME/.codex}/skills"
    product="Codex"
    ;;
esac

dst="${destination:-$default_destination}"

skills=(fable-method fable-loop fable-judge fable-domain)
mkdir -p "$dst"
for skill in "${skills[@]}"; do
  cp -r "$src/skills/$skill" "$dst/"
done

echo "Installed: ${skills[*]} -> $dst"
echo "The skills will be available to $product in a new turn."
