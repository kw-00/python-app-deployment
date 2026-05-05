#!/usr/bin/env bash

# Usage:
# ./find_and_dump.sh "<root_path>" "<regex>"

ROOT_PATH="$1"
REGEX="$2"

if [ -z "$ROOT_PATH" ] || [ -z "$REGEX" ]; then
  echo "Usage: $0 <root_path> <regex>"
  exit 1
fi

find "$ROOT_PATH" -type f | while read -r file; do

  # Match against full path
  if [[ "$file" =~ $REGEX ]]; then
    echo "===================================="
    echo "FILE: $file"
    echo "===================================="
    cat "$file"
    echo -e "\n"
  fi

done