#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Tue Jan 15 16:53:43 2019

@author: astoned
"""
# =============================================================================
# 
# Finger exercise: When the implementation of fib in Figure 4.7 is used to
# compute fib(5) , how many times does it compute the value fib(2) ?
# 
# =============================================================================

fibCount = 0 

def fib(n):
    global fibCount
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        fibCount += 1
        return 2 # fib(2) = 2
    else:
        return fib(n-1) + fib(n-2)
    
def testFib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))
        
mainFib = 5

fib(mainFib)

print('fib(2) was called', fibCount, 'times')

testFib(mainFib)
