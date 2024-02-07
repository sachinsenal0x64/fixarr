#!/bin/sh

REPO_URL="https://github.com/sachinsenal0x64/FIXARR"
CLONE_DIR="FIXARR"

# Check if fixarr.py exists
if [ -e "${CLONE_DIR}/fixarr.py" ]; then
    echo "fixarr.py already exists. Skipping Git clone."
else
    echo "fixarr.py does not exist. Cloning Git repository..."
    git clone "${REPO_URL}" "${CLONE_DIR}"
fi

cd "${CLONE_DIR}"
echo "Installing Packages......"

# Create virtual environment
python -m venv fixarr

# Activate virtual environment
source fixarr/bin/activate

pip install -r requirements.txt
chmod +x fixarr.py
python fixarr.py
