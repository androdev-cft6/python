# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result=0
    if exp==0:
        result=1
    else:
        result=base * recurPower(base, exp-1)
    return result

print(recurPower(2,8))