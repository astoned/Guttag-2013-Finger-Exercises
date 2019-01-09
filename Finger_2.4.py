#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Wed Jan  9 15:35:16 2019

@author: astoned
"""

# =============================================================================
# Finger exercise: Write a program that asks the user to input 10 integers, and
# then prints the largest odd number that was entered. If no odd number was
# entered, it should print a message to that effect.
# =============================================================================

list = []
odds = False

print('You will be asked to enter 10 integer numbers, one at a time.')

for i in range(1,11):
    i = int(input('Number: ')) 
    list.append(i)

list = sorted(list, reverse = True)

for j in list:
    if j%2 == 1:
        print('The largest odd number is', j, 'from', list)
        odds = True
        break

if odds == False:
    print('There is no odd number from', list)