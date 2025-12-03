#!/usr/bin/env bash

set -e

if [ $# -ne 1 ]; then
  echo "Usage: $0 <day-number>"
  exit 1
fi

DAY="$1"
YEAR=2025
README="README.md"

if ! [[ "$DAY" =~ ^[0-9]+$ ]]; then
  echo "Error: day must be a number"
  exit 1
fi

URL="https://adventofcode.com/${YEAR}/day/${DAY}"
HTML=$(curl -s "$URL")

TITLE=$(echo "$HTML" | grep -oP '(?<=--- Day '"$DAY"': ).*(?= ---)')
if [ -z "$TITLE" ]; then
  echo "Could not extract the title"
  exit 1
fi

echo "Found title: $TITLE"

ROW="| [🎄 Day ${DAY}: ${TITLE}](https://adventofcode.com/${YEAR}/day/${DAY}) | ⭐⭐ | [🎯 Part 1](${YEAR}/day${DAY}/part1.ml) | [🎯 Part 2](${YEAR}/day${DAY}/part2.ml) |"

CURRENT_STARS=$(grep -oP '(?<=Progress ⭐\().*(?=/24)' "$README")
NEW_STARS=$((CURRENT_STARS + 2))

sed -i "s/Progress ⭐(${CURRENT_STARS}\/24)/Progress ⭐(${NEW_STARS}\/24)/" "$README"
echo "Updated star counter: $CURRENT_STARS → $NEW_STARS"

awk -v newRow="$ROW" '
  BEGIN { lastTableLine = 0 }
  /^\|/ { lastTableLine = NR }
  { lines[NR] = $0 }
  END {
    for (i = 1; i <= NR; i++) {
      print lines[i]
      if (i == lastTableLine) {
        print newRow
      }
    }
  }
' "$README" > "${README}.tmp"

mv "${README}.tmp" "$README"

echo "Added row for Day $DAY"
