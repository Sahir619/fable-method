"""Repo consistency checks, run by CI and locally: python .github/checks.py"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
failures = []


def fail(msg):
    failures.append(msg)
    print(f"FAIL  {msg}")


def ok(msg):
    print(f"ok    {msg}")


# 1. Plugin and marketplace manifests parse and carry required fields
for rel, required in [
    (".claude-plugin/plugin.json", ["name", "description", "version"]),
    (".claude-plugin/marketplace.json", ["name", "owner", "plugins"]),
]:
    path = os.path.join(ROOT, rel)
    try:
        with io.open(path, encoding="utf-8") as f:
            data = json.load(f)
        missing = [k for k in required if k not in data]
        if missing:
            fail(f"{rel}: missing fields {missing}")
        else:
            ok(f"{rel} valid")
    except Exception as e:
        fail(f"{rel}: {e}")

# 2. Plugin and marketplace versions agree
try:
    with io.open(os.path.join(ROOT, ".claude-plugin/plugin.json"), encoding="utf-8") as f:
        pv = json.load(f)["version"]
    with io.open(os.path.join(ROOT, ".claude-plugin/marketplace.json"), encoding="utf-8") as f:
        mv = json.load(f)["plugins"][0]["version"]
    if pv != mv:
        fail(f"version mismatch: plugin.json {pv} vs marketplace.json {mv}")
    else:
        ok(f"versions agree ({pv})")
except Exception as e:
    fail(f"version check: {e}")

# 3. All three skills exist with frontmatter name + description
for skill in ["fable-method", "fable-loop", "fable-judge"]:
    path = os.path.join(ROOT, "skills", skill, "SKILL.md")
    try:
        with io.open(path, encoding="utf-8") as f:
            head = f.read(2000)
        if not head.startswith("---") or f"name: {skill}" not in head or "description:" not in head:
            fail(f"skills/{skill}/SKILL.md: frontmatter missing name/description")
        else:
            ok(f"skills/{skill}/SKILL.md frontmatter valid")
    except Exception as e:
        fail(f"skills/{skill}/SKILL.md: {e}")

# 4. Domain adapters all carry a binding minimum evidence set and a fraud table
domains_dir = os.path.join(ROOT, "skills", "fable-method", "references", "domains")
for name in sorted(os.listdir(domains_dir)):
    with io.open(os.path.join(domains_dir, name), encoding="utf-8") as f:
        body = f.read()
    if "Minimum evidence set" not in body or "Fraud table" not in body:
        fail(f"domains/{name}: missing minimum evidence set or fraud table")
    else:
        ok(f"domains/{name} complete")

# 5. Evidence files parse as JSON
results_dir = os.path.join(ROOT, "eval", "results")
for name in sorted(os.listdir(results_dir)):
    try:
        with io.open(os.path.join(results_dir, name), encoding="utf-8") as f:
            json.load(f)
        ok(f"eval/results/{name} parses")
    except Exception as e:
        fail(f"eval/results/{name}: {e}")

# 6. No em or en dashes anywhere (repo style rule)
dash = re.compile(chr(0x2014) + "|" + chr(0x2013))
count = 0
for root, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in (".git",)]
    for f in files:
        if not f.endswith((".md", ".js", ".json", ".py", ".sh", ".ps1", ".yml", ".csv")):
            continue
        p = os.path.join(root, f)
        try:
            with io.open(p, encoding="utf-8") as fh:
                if dash.search(fh.read()):
                    fail(f"em/en dash in {os.path.relpath(p, ROOT)}")
                    count += 1
        except Exception:
            pass
if count == 0:
    ok("no em/en dashes anywhere")

# 7. Every scenario directory is non-empty
scen_dir = os.path.join(ROOT, "eval", "scenarios")
for name in sorted(os.listdir(scen_dir)):
    entries = os.listdir(os.path.join(scen_dir, name))
    if not entries:
        fail(f"eval/scenarios/{name} is empty")
    else:
        ok(f"eval/scenarios/{name} ({len(entries)} entries)")

# 8. SKILL.md and AGENTS.md carry the same method. AGENTS.md claims to be
#    the identical method, and on 2026-07-14 it was found missing all three
#    round-10 corrections. Two mechanical comparisons: the numbered rule
#    names per step must match exactly, and a manifest of load-bearing
#    artifact phrases must appear in both files.
with io.open(os.path.join(ROOT, "skills", "fable-method", "SKILL.md"), encoding="utf-8") as f:
    _skill_body = f.read()
with io.open(os.path.join(ROOT, "AGENTS.md"), encoding="utf-8") as f:
    _agents_body = f.read()


def _rule_names(body):
    names = {}
    step = None
    for line in body.splitlines():
        m = re.match(r"## Step (\d+)", line)
        if m:
            step = m.group(1)
            continue
        m = re.match(r"\d+\. \*\*(.+?)\*\*", line)
        if m and step is not None:
            names.setdefault(step, []).append(m.group(1))
    return names


_sk, _ag = _rule_names(_skill_body), _rule_names(_agents_body)
for step in sorted(set(_sk) | set(_ag)):
    if _sk.get(step) != _ag.get(step):
        fail(f"rule drift in Step {step}: SKILL.md has {_sk.get(step)} but AGENTS.md has {_ag.get(step)}")
    else:
        ok(f"Step {step} rule names in sync ({len(_sk.get(step, []))} rules)")

LOAD_BEARING = [
    "INTENT: code does <X>",
    "EMBEDDED: <where> instructs agents to <what>; not from the user; not obeyed",
    "the EMBEDDED line joins the INTENT line",
    "A demand for concealment is the strongest tell",
    "must appear verbatim in your final report",
    "Leave behind only intended changes",
    "Artifact gate, the last check before sending",
]
for phrase in LOAD_BEARING:
    missing = [n for n, b in (("SKILL.md", _skill_body), ("AGENTS.md", _agents_body)) if phrase not in b]
    if missing:
        fail(f"load-bearing phrase missing from {', '.join(missing)}: {phrase!r}")
    else:
        ok(f"load-bearing phrase in both files: {phrase[:44]}")

print()
if failures:
    print(f"{len(failures)} check(s) failed")
    sys.exit(1)
print("all checks passed")
