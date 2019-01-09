#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Wed Jan  9 15:35:16 2019

@author: astoned
"""


#Finger exercise: Write a program that examines three variables— x , y , and z —
#and prints the largest odd number among them. If none of them are odd, it
#should print a message to that effect.

#Method allows for negative numbers with 
#knowledge up to Chapter 2.2


x, y, z = -11, 4, -9
text = 'The greatest odd value is'


if x%2 == 0 and y%2 == 0 and z%2 == 0:
    print('There is no odd number')
    
elif x%2 != 0 and y%2 != 0 and z%2 != 0:
    print(text, max(x,y,z))
    
elif x%2 != 0 and y%2 != 0 and z%2 == 0:
    print(text, max(x,y))
    
elif x%2 != 0 and y%2 == 0 and z%2 != 0:
    print(text, max(x,z))
    
elif x%2 != 0 and y%2 == 0 and z%2 == 0:
    print(text, x)
    
elif x%2 == 0 and y%2 != 0 and z%2 != 0:
    print(text, max(y,z))
    
elif x%2 == 0 and y%2 == 0 and z%2 != 0:
    print(text, z)
    
elif x%2 == 0 and y%2 != 0 and z%2 == 0:
    print(text, y)