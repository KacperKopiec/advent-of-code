#!/bin/bash

# Ensure the script is being called with an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <day_number>"
  exit 1
fi

# Define the year and day folder structure
DAY="day$1"
TARGET_DIR="$DAY"

# Create the target directory
mkdir -p "$TARGET_DIR"

# Create the files within the target directory
touch "$TARGET_DIR/part1.py"
touch "$TARGET_DIR/part2.py"
touch "$TARGET_DIR/input.in"

# Add the Python code to part1.py
cat <<EOL > "$TARGET_DIR/part1.py"
import os

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\\n')
    
EOL

# Notify the user of completion
echo "Created folder and files:"
echo "$TARGET_DIR"
echo "$TARGET_DIR/part1.py"
echo "$TARGET_DIR/part2.py"
echo "$TARGET_DIR/input.in"
