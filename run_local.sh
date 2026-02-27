#!/usr/bin/env bash
set -e

echo "Installing deps..."
pip install -r requirements.txt

echo "Launching Jupyter..."
jupyter notebook
