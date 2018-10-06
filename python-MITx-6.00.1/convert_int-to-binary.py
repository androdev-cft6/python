# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
str_num_int=input("Please enter number: ")
num_int=int(str_num_int)
str_num_bin=''
isNeg=True

if num_int<0:
    isNeg=True
    num_int=abs(num_int)
else:
    isNeg=False
    
if num_int==0:
    str_num_bin=0
while num_int>0:
    str_num_bin=str(num_int%2)+str_num_bin
    num_int=num_int//2
if isNeg:
    str_num_bin="-"+str_num_bin
print(str_num_int + " in binary format is: " + str_num_bin)