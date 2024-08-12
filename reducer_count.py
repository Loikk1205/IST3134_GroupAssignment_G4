#!/usr/bin/env python3
import sys

current_airline = None
current_count = 0
airline = None

# Read input from standard input
for line in sys.stdin:
    line = line.strip()
    airline, count = line.split('\t')

    try:
        count = int(count)
    except ValueError:
        continue

    if current_airline == airline:
        current_count += count
    else:
        if current_airline:
            print(f'{current_airline}\t{current_count}')
        current_count = count
        current_airline = airline

if current_airline == airline:
    print(f'{current_airline}\t{current_count}')
    
    
    
    
