# -*- coding: utf-8 -*-
"""
Created on sunday oct  16 2022

@author: LORD-MODH
"""

# Finger exercise: Write a program that asks the user to enter an integer and
# prints two integers, root and pwr , such that 0 < pwr < 6 and root**pwr is equal
# to the integer entered by the user. If no such pair of integers exists, it should
# print a message to that effect.

x = int(input('Enter a Number : '))
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
##EASY WAY    
x=int(input("enter a number"))
root=0
while root<abs(x):
    root+=1
    for a in range(1,6):
        if root**a == abs(x):
            if x<0 :
                if a%2==0:
                    pass
                else :
                    print(-root, "power",a, "gives", x)
            else:
                print(root,"power",a,"gives",x)
 

                
    
