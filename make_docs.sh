#!/usr/bin/env bash

set -Eeuo pipefail

rm -rf docs/*
fd -e py --exclude __init__.py --exclude bpython_setup.py -0 | xargs -0 pdoc  -o docs -d markdown --show-source --mermaid

