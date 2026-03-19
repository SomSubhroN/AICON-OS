#!/bin/bash

echo "Installing AICON..."

AICON_DIR=~/aicon

echo "[1] Creating directories..."
mkdir -p $AICON_DIR/{core,experiments,datasets,jobs,envs}

echo "[2] Installing dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install psutil

echo "[3] Setting up CLI command..."

sudo rm -f /usr/local/bin/aicon
sudo ln -s $(pwd)/core/aicon.py /usr/local/bin/aicon

echo "[4] Making executable..."
chmod +x core/aicon.py

echo "[5] Verifying Installation..."
if command -v aicon &> /dev/null; then
	echo "AICON command installed successfully!"
else
	echo "ERROR: AICON command not found!"
fi

echo "AICON installed Successfully!"
echo "Try:"
echo "aicon submit test.py --env testenv --dataset mydata"
echo "aicon scheduler"
