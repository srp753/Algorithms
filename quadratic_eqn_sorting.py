#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 17:08:06 2018

@author: snigdha
"""
"""
Problem: 
    
Given a list of numbers x1,x2,....xn
and 
a quadratic equation:f(x) =  ax^2 + bx + c

Compute the f(x) for all the x's and sort them

Solution: Complexity total = O(n) + O(n*logn) = O(n*logn)
    
    if a > 0 (is positive)
    then we choose the minimum element in the f(x)-> [pivot]
    and split the f(x) array into left and right based
    on the pivot.
    
    We then apply some conditions with which computation time
    could be lesser in simple situations and if they are not 
    satisfied, we do a simple heap sort which has O(n*log n )
    time
    
    If a < 0
    
    We do the same as above, however pivot will be the maximum 
    element since a > 0 equation involves maxima.

"""
import numpy as np
import operator

     
def sorting(x,a,b,c):
    
    arr = []
    for i in x:
        arr.append(a*i*i + b*i + c)
        
    arr = np.array(arr)
    
    if(a > 0):
        new_arr = positive_a(arr)
    else:
        new_arr = negative_a(arr)
    
    return new_arr
    

def positive_a(arr):
    

    #Compute the minimum element and minimum element's index
    min_index, min_value = min(enumerate(arr), key=operator.itemgetter(1))
    

    #Split into left and right
    left = arr[0:min_index][::-1]
    right = arr[min_index+1:]

    #A new array to put our sorted results
    new_arr = []
    new_arr.append(min_value)

    if(len(left) == 0):
        new_arr = new_arr + list(right)
    
    elif(len(right) == 0):
        new_arr = new_arr + list(left)
    #If the largest of left is smaller than the smallest of right
    elif(left[-1] <= right[0]):
        new_arr = new_arr + list(left) + list(right)
    
    #If the largest of right is smaller than the smallest of left
    elif(right[-1] <= left[0]):
        new_arr = new_arr + list(right) + list(left)
    
    else:
        #Heap sort
        new_arr = new_arr + list(left) + list(right)
        heapSort(new_arr)
        
    return new_arr
    
def negative_a(arr):
    #Compute the maximum element and maximum element's index
    max_index, max_value = max(enumerate(arr), key=operator.itemgetter(1))
    
    #Split into left and right
    left = arr[0:max_index]
    right = arr[max_index+1:][::-1]

    #A new array to put our sorted results
    new_arr = []
    new_arr.append(max_value)

    if(len(left) == 0):
        new_arr = list(right) + new_arr
    
    elif(len(right) == 0):
        new_arr = list(left) + new_arr 
    #If the largest of left is smaller than the smallest of right
    if(left[-1] <= right[0]):
        new_arr = list(left) + list(right) + new_arr
    
    #If the largest of right is smaller than the smallest of left
    elif(right[-1] <= left[0]):
        new_arr = list(right) + list(left) + new_arr
    
    else:
        #heapsort
        new_arr = new_arr + list(left) + list(right)
        heapSort(new_arr)
        
    return new_arr

# Python program for implementation of heap Sort
#Reference taken from: https://www.geeksforgeeks.org/heap-sort/
 
# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)
    

x = [-5,-3,-1,0,2,3]
a = 1 
b = 2
c = 1

print("x: ",x)
print("a: ",a)
print("b: ",b)
print("c: ",c)
print("Case 1: When a is positive: ",sorting(x,a,b,c))

x = [-5,-3,-1,0,2,3]
a = -1 
b = 2
c = 1

print("x: ",x)
print("a: ",a)
print("b: ",b)
print("c: ",c)
print("Case 2: When a is negative: ",sorting(x,a,b,c))


