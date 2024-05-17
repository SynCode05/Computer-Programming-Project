#!/bin/bash

# Check if requirements.txt file exists
if [ ! -f requirements.txt ]; then
    echo "requirements.txt not found!"
    exit 1
fi

# Check if the required libraries are already installed by trying to import them
# If not installed, then install them using pip
echo "Checking required libraries..."

# Use a temporary file to check if pip installs are needed
pip freeze > installed_packages.txt

while IFS= read -r package; do
    if ! grep -i "$package" installed_packages.txt > /dev/null; then
        echo "Installing $package..."
        pip install "$package"
    else
        echo "$package already installed."
    fi
done < requirements.txt

rm installed_packages.txt

# Navigate to the data directory
cd ./data || { echo "Directory ./data not found!"; exit 1; }

# Run the Python script
python pages.py

echo "Script execution completed."
