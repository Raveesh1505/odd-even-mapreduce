#!/usr/bin/env python

"""REDUCER FUNCTION"""

import sys

# Setting the variables
even_sum = 0
odd_sum = 0
number = None
odd_count = 0
even_count = 0

for line in sys.stdin:
    line = line.strip()
    # Reading the mapped numbers and their types
    # presented by mapper
    number, type = line.split('\t')
    number, type = int(number), str(type)

    if (type == "EVEN"):
        even_count += 1
        even_sum += int(number)
    elif (type == "ODD"):
        odd_count += 1
        odd_sum += int(number)

print("Sum of odd numbers = %s" % (odd_sum))
print("Total number of odd numbers = %s" % (odd_count))
print("Sum of even numbers = %s" % (even_sum))
print("Total number of even numbers = %s" % (even_count))
