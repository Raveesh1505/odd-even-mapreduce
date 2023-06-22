#!/usr/bin/env python

"""MAPPER FUNCTION"""

import sys

for line in sys.stdin:

    # Strip will be used to remove the whitespaces
    # from front and end of the line.
    #
    # Split will be used to seperate out all the numbers.
    # ',' will be used as split delimeter as present in the
    # input file.
    line = line.strip()
    numbers = line.split(',')

    # Mapping every number with their type
    # and writting them using stdout
    for number in numbers:
        if (int(number) % 2 == 0):
            print('%s\t%s' % (number, 'EVEN'))      # For even numbers
        elif (int(number) % 2 != 0):
            print('%s\t%s' % (number, 'ODD'))       # For odd numbers