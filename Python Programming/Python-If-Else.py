#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if(n%2==0):
        if(n>2 or n<5):
            print("Not Weird")
        elif(n>6 or n<20):
            print("Weird")
        elif(n>20):
            print("Not Weird")
    else:
        print("Weird")


