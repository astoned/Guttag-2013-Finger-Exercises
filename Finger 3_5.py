#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Sun Jan 13 11:17:15 2019

@author: astoned
"""

# =============================================================================
# Finger exercise: Add some code to the implementation of Newton-Raphson that
# keeps track of the number of iterations used to find the root. Use that code as
# part of a program that compares the efficiency of Newton-Raphson and bisection
# search. (You should discover that Newton-Raphson is more efficient.)
# =============================================================================

number = int(input('Number? '))
guess = abs(number)
#root = int(input('Root? '))
# uncomment to allow for other root values, but comment Newton-Raphson bellow
# that works only with root = 2

root = 2
epsilon = 0.01
numGuessesBS = 0
low = 0.0
high = max(1.0,guess)
ans = (high + low)/2.0

while abs(ans**root - guess) >= epsilon:
   # print('low =', low, 'high =', high, 'ans =', ans)
    numGuessesBS += 1
    if ans**root < guess:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0

print('numGuessesBS =', numGuessesBS)

if number < 0:
    if root%2 == 1:
        ans = -ans
    else:
        ans = str(ans)+'i'

print(ans, 'is close to square root of', number)



# ===========================

#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0

#epsilon = 0.01
k = number
guess = k/2.0
numGuessesNR = 0

while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    numGuessesNR += 1

print('numGuessesNR =', numGuessesNR)
print('Square root of', k, 'is about', guess)