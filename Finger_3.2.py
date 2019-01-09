#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:32:17 2019

@author: daniel
"""

# Finger exercise: Write a program that asks the user to enter an integer and
# prints two integers, root and pwr , such that 0 < pwr < 6 and root**pwr is equal
# to the integer entered by the user. If no such pair of integers exists, it should
# print a message to that effect.

x = int(input('Number? '))
root = 0

for pwr in range(1,6):
    if x > 0:
        while root <= x:
            root += 1
        
            if root**pwr == x:            
                print('root = ', root, ' and pwr = ', pwr)
        root = 0
    elif x < 0:
        while root >= x:
            root -= 1
        
            if root**pwr == x:            
                print('root = ', root, ' and pwr = ', pwr)
        root = 0
    elif x == 0:
        print('There is no such pair')
        break