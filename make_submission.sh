#!/bin/sh
# Builds submission.tar.gz with Makefile at the archive root (never tar "."; the grader rejects it).
set -e
tar czf submission.tar.gz --exclude='__pycache__' --exclude='*.pyc' --exclude='.DS_Store' \
  Makefile .gitignore src tests
tar tzf submission.tar.gz | grep -qx Makefile && echo "Makefile at archive root: OK"
