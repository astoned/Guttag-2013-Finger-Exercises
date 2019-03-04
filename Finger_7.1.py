#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Wed Jan 30 21:03:41 2019

@author: astoned
"""
#Finger exercise: Implement a function that meets the specification below. Use
#a try-except block.

def sumDigits(s):
    """Assumes s is a string
        Returns the sum of the decimal digits in s
           For example, if s is 'a2c3c' it returns 5"""
           
    group = []
    numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
    counter = 0
    for i in s:
        group.append(i)
        print(group)
    for e in group:
        if e in numbers:
            counter += int(e)
            print(e, "was added to", counter)
    return counter
            
querry = input("Enter a string: ")
print (sumDigits(querry))
       