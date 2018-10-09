# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 05:21:44 2018

@author: andrew
"""
def removeDups(L1,L2):
    L1_copy=L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
            
l1=[1,2,3,4]        
l2=[1,2,5,6]
removeDups(l1,l2)
print(l1)
