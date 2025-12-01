#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <day_number>"
  exit 1
fi

DAY="day$1"
TARGET_DIR="$DAY"

mkdir -p "$TARGET_DIR"

touch "$TARGET_DIR/part1.ml"
touch "$TARGET_DIR/part2.ml"
touch "$TARGET_DIR/input.in"
touch "$TARGET_DIR/dune"

cat <<EOL > "$TARGET_DIR/part1.ml"
let filename = "$DAY/input.in"
EOL

cat <<EOL > "$TARGET_DIR/dune"
(executable
 (name part1)
 (libraries advent))

(executable
 (name part2)
 (libraries advent))
EOL

# Notify the user of completion
echo "Created folder and files:"
echo "$TARGET_DIR"
echo "$TARGET_DIR/part1.ml"
echo "$TARGET_DIR/part2.ml"
echo "$TARGET_DIR/dune"
echo "$TARGET_DIR/input.in"