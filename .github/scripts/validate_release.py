#!/usr/bin/env python3
import sys
import json
from pathlib import Path

# --- Config ---
WILDERFORGE_JSON = Path("wilderforge.mod.json")

# --- Input check ---
if len(sys.argv) == 1:
    print("No version specified");
if len(sys.argv) != 2:
    print("Usage: validate_release.py <expected_version>", file=sys.stderr)
    sys.exit(1)

expected_version = sys.argv[1]

# --- Load JSON ---
try:
    with WILDERFORGE_JSON.open("r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Error: JSON file not found at {WILDERFORGE_JSON}", file=sys.stderr)
    sys.exit(3)
except json.JSONDecodeError as e:
    print(f"Error: Failed to parse JSON: {e}", file=sys.stderr)
    sys.exit(2)

# --- Validate version ---
actual_version = data.get("version")

if actual_version != expected_version:
    print(
        f"Error: Version mismatch. The version in '{WILDERFORGE_JSON}' "
        f"('{actual_version}') does not match the GitHub release tag '{expected_version}'.",
        file=sys.stderr
    )
    sys.exit(1)

print(f"Version check passed: {actual_version}")
