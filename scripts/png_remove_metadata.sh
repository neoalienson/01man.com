#!/bin/sh

echo "Removing metadata from PNG files under current directory..."

# Find all PNG files
png_files=$(find . -type f -iname "*.png")

# Function to strip metadata from PNG files
strip_metadata() {
  file="$1"
  temp_file="$(mktemp)"
  convert "$file" -strip "$temp_file"
  mv -f "$temp_file" "$file"
}

# Process each staged PNG file
for file in $png_files; do
  strip_metadata "$file"
done
