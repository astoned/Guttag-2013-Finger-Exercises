#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Mon Jan 14 18:42:29 2019

@author: astoned
"""
# =============================================================================
# 
# Finger exercise: Write a function isIn that accepts two strings as arguments
# and returns True if either string occurs anywhere in the other, and False
# otherwise. Hint: you might want to use the built-in str operation in .
# 
# =============================================================================

def isIn(string1, string2):
    return bool(string1 in string2 or string2 in string1)

word1 = 'abc'
word2 = 'abcdef'

test = isIn(word1, word2)

print(test)