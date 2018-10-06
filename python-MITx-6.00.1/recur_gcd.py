# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b==0:
        return a
    else:
        return gcdRecur(b, a%b) # according to Euclid's algorithm
    
print(gcdRecur(1121358, 462))