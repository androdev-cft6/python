# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def polysum(n, s):
   '''
   n: number of sides of regular polygon
   s: length of one side
   
   returns: sum of the area and square of the perimeter
            of the regular polygon
   '''
   from math import pi, tan
   
   area=(0.25*n*s**2)/tan(pi/n) #formula provided
   print("area: " + str(area))
   
   perim=n*s
   print("perim: " + str(perim))
   
   return round((area+perim**2),4)

print(polysum(3, 5))
   