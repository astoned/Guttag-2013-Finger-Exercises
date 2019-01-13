#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Fri Jan 11 18:21:47 2019

@author: astoned
"""

# =============================================================================
# Finger exercise: What is the decimal equivalent of the binary number
# 10011 ?
# =============================================================================

binNumber = '10011'
pwr = 0
number = 0

for i in reversed(binNumber):
    number = number + int(i)*2**pwr
    pwr += 1
    
print (number)
