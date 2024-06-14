#!/bin/bash

# check whether file argument is passed or not
if [ -z "$1" ]; then
    echo "Usage: $0 <file_name>"
    exit 1
fi

# 1. Count the different HTTP response status codes
echo "HTTP Response Status Codes:"
grep -oE 'HTTP/1.1" [0-9]+' "$1" | awk -F'"' '{print $2}' | sort | uniq -c | sort -n | awk '{print $2" "$1}'
echo ""  # Line break

# 2. Count the unique client IP addresses
echo "Unique Client IP Addresses:"
unique_client_count=$(grep -o '^[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*' "$1" | sort | uniq | wc -l)
echo "UNIQUE_CLIENT_ADDRESS - $unique_client_count"
echo ""  # Line break

# 3. Count the number of words for each line
echo "Word Count for Each Line:"
line_number=1
while read -r line; do
    words=$(echo "$line" | wc -w)
    echo "$line_number | $words"
    line_number=$((line_number + 1))
done < "$1"
