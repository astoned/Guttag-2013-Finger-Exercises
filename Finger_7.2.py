#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Mon Mar  4 18:14:07 2019

@author: astoned
"""

#Finger Exercise: Implement a function that satisfies the specification

def findAnEven(l):
    """Assumes l is a list of integers
        Returns the first even number in l
        Raises ValueError if l does not contain an even number"""
    
    ticker = 0
    even = None
    for i in l:
        ticker += 1
        if i %2 == 0:
            even = i
            break
        elif ticker == len(l):
            raise ValueError('List', l, 'does not contain an even number')
    return even

testCase1 = [1,2,3,4]
testCase2 = [1,3,5]
print (findAnEven(testCase1))
print (findAnEven(testCase2))
