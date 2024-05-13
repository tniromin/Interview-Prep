#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # frequency = length of the final word/ length of orignal string(Quotient) x Number of a in String
    ### Also add the final string repetition, see how many a were repeated
    ## Increase exe speed
    if s.count("a")==0:
        return 0
    else
        return n//len(s)*s.count("a")+ s[:n%len(s)].count("a")   
    ## One line code
    
    #freq = n//len(s)*s.count("a")+ s[:n%len(s)].count("a")
    #return n//len(s)*s.count("a")+ s[:n%len(s)].count("a")
    
    ## Conventional
    #freq = n//len(s)*s.count("a")+ s[:n%len(s)].count("a")
    #return freq
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
