# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 02:45:48 2018

@author: andrew
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    rTup=()
    for i in range(len(aTup)):
        if i%2==0:
            rTup+= (aTup[i]),
    return rTup

def oddTuples2(aTup):
    return aTup[::-2]
        
print(oddTuples2(("I", "love", "America", "and", "the", "world")))