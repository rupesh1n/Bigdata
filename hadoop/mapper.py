#!/usr/bin/env python3

import sys
 
# Read each line from standard input

for line in sys.stdin:

    # Remove leading/trailing whitespace

    line = line.strip()

    # Split the line by tabs (matching your sample.txt format)

    parts = line.split('\t')

    if len(parts) >= 2:

        # First token is the year, last token is the average

        year = parts[0]

        avg_consumption = parts[-1]

        # Output the key and value separated by a tab

        print(f"{year}\t{avg_consumption}")
 