#!/bin/python3

import math
import os
import random
import re
import sys



def countingValleys(steps, path):

    valleys=0
    
    # Before Sea level should be a -1 and the sea level should come to 0
    ## This is a valley    
    sea=0
    b_sea=0
    
    
    for x in path:
        b_sea=sea        
        if x == 'U':
            sea+=1
        else:
            sea-=1
    
        if sea==0 and b_sea<0:
            valleys +=1
                    
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
