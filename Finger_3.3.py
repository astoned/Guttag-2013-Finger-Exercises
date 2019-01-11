#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Fri Jan 11 16:53:52 2019

@author: astoned
"""

# =============================================================================
# Finger exercise: What would have to be changed to make the code in Figure
# 3.4 work for finding an approximation to the cube root of both negative and
# positive numbers? (Hint: think about changing low to ensure that the answer
# lies within the region being searched.)
# =============================================================================

number = int(input('Number? '))
x = abs(number)
root = int(input('Root? '))
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0

while abs(ans**root - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**root < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0

print('numGuesses =', numGuesses)

if number < 0:
    if root%2 == 1:
        ans = -ans
    else:
        ans = str(ans)+'i'

print(ans, 'is close to square root of', number)