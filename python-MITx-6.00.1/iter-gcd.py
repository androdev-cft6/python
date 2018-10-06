# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    gcd=0 #gcd is the greatest common divisor
    for i in range(1,b+1):
       if a%i==0 and b%i==0:
           gcd=i
    return gcd

print(gcdIter(625,25))