#!/usr/bin/env bash

set -Eeuo pipefail

# Update API Docs
echo -n "Updating API docs..."
rm -rf docs/*
fd -e py --exclude __init__.py --exclude bpython_setup.py -0 | xargs -0 pdoc  -o docs -d markdown --show-source --mermaid
echo "done"

# Update Changelog
echo -n "Updating Changelog..."
rm CHANGELOG.md
git cliff > CHANGELOG.md
echo "done"

