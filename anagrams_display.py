#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:38:18 2018

@author: snigdha
"""


import copy

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
dicty = {}

temp = copy.deepcopy(strs)
for i in range(0,len(temp)):
    st = ""
    for j in sorted(temp[i]):
        st = st + str(j)
        temp[i] = st
    if st not in dicty:
        dicty[st] = []
        dicty[st].append(i)  
    else:
        dicty[st].append(i)

m = []        
for k,v in dicty.items():
    
    l = []
    for p in v:
        l.append(strs[p])
    print("l",l)
    m.append(l)          

