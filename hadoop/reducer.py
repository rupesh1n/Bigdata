#!/usr/bin/env python3
import sys
 
for line in sys.stdin:
    line = line.strip()
    # Parse the input from the mapper
    try:
        year, avg_val = line.split('\t', 1)
        avg_val = int(avg_val)
        # Filtering logic: only output if average > 30
        if avg_val > 30:
            print(f"{year}\t{avg_val}")
    except ValueError:
        # Ignore lines that don't have valid integers
        continue