#!/usr/bin/env python3
import sys

# Read input from standard input
for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')

    # 'DepDelayed' is in the 10th column and 'Airline' in the 2nd column
    dep_delay = parts[9]
    airline = parts[1]

    try:
        if float(dep_delay) >= 1:
            print(f'{airline}')
    except ValueError:
        continue
        
        
        
        
