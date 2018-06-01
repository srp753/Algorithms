#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:15:08 2018

@author: snigdha
"""
"""
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.


"""
def solution(A):
    # write your code in Python 3.6
    maxi = max(A)
    dicty = {}
    
    if(maxi < 0):
        return 1
    else:
        for i in A:
            if i not in dicty:
                dicty[i] = 1
            else:
                dicty[i] = dicty[i] + 1
        for j in range(1,maxi+1):
            if(j not in dicty):
                return j
    
    return (j+1)
        