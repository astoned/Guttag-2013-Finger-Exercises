#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Fri Jan 11 16:20:22 2019

@author: astoned
"""

# =============================================================================
# Finger exercise: Let s be a string that contains a sequence of decimal numbers
# separated by commas, e.g., s = '1.23,2.4,3.123' . Write a program that prints
# the sum of the numbers in s .
# =============================================================================

s = '1.23,2.4,3.123'
sInt = []
total = 0

for i in s:
    if i in '123456789':
        sInt.append(int(i))

print(sum(sInt))