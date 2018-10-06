# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 21:39:06 2018

@author: andrew
"""
s = 'azcbobobegghaklsazcbobobegghaklazcbobobegghaklsazcbobobegghaklazcbobobegghaklsazcbobobegghakl'
s_pattern='bob'
count = 0 # number of occurencies found

for n in range(len(s)):
    index=0
    for l in s_pattern:
        if l==s[n+index]:
            index +=1
        else:
            break
        if (index==len(s_pattern)):
            count+=1
print("found: " + str(count) + " occurences of " + s_pattern)    