#!/bin/bash

# Update the package list
sudo apt-get update -y

# Install required system dependencies
sudo apt-get install -y python3-pip

# Upgrade pip
pip install --upgrade pip

# Install required Python dependencies from requirements.txt
pip install -r requirements.txt

echo "Setup completed successfully!"