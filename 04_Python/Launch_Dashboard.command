#!/usr/bin/env bash
# Sun Pharma / Organon -- Interactive Valuation Dashboard launcher.
# Double-click this file in Finder to open the dashboard in your browser.
# Close this Terminal window (or press Ctrl+C) to stop the dashboard.

set -e
cd "$(dirname "$0")"

echo "=================================================================="
echo " Sun Pharma / Organon -- Interactive Valuation Dashboard"
echo "=================================================================="
echo "Starting up... your browser will open automatically."
echo "Keep this window open while you use the dashboard."
echo "To stop: close this window, or press Ctrl+C."
echo

PYTHON=python3
if ! command -v "$PYTHON" >/dev/null 2>&1; then
    echo "python3 was not found on this Mac."
    echo "Install Python 3 from https://www.python.org/downloads/ and double-click this file again."
    read -n 1 -s -r -p "Press any key to close this window..."
    exit 1
fi

if ! "$PYTHON" -c "import streamlit" >/dev/null 2>&1; then
    echo "First run: installing required packages (pandas, numpy, matplotlib, openpyxl, streamlit)..."
    echo "This can take a minute."
    "$PYTHON" -m pip install --quiet -r requirements.txt
    echo "Done."
    echo
fi

"$PYTHON" -m streamlit run dashboard.py

echo
read -n 1 -s -r -p "Dashboard stopped. Press any key to close this window..."
