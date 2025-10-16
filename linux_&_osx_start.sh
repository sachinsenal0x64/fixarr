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

# Detect Python version and use python3.12 if available, fallback to python3
PYTHON_CMD="python3"
if command -v python3.12 >/dev/null 2>&1; then
    PYTHON_CMD="python3.12"
    echo "Using Python 3.12"
else
    echo "Python 3.12 not found, using python3"
fi

# Create virtual environment
$PYTHON_CMD -m venv fixarr

# Activate virtual environment
source fixarr/bin/activate

# Install setuptools first (replaces distutils removed in Python 3.12)
pip install setuptools

# Install remaining dependencies
pip install -r requirements.txt
chmod +x fixarr.py
python fixarr.py
