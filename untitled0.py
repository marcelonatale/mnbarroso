#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 09:37:15 2019

@author: marcelonatale
"""

import json
with open('/Users/marcelonatale/Desktop/ECON611/ECON611/database/nber.json') as f:
    data = json.load(f)
 
# Warm-up questions
# #1
inp = [1,2,3,4] # variable with 3 elements which is the half of the original list in the question
inp[:3] = inp[:3][::-1] # reversing the first two elements
print (inp)
print(len(inp))
inp += [5,6,7] # appending the remaining numbers in the list
print (inp)

# #2
inp1 = [1,2,3,4]
inp2 = ['a', 'b', 'c', 'd']
output = [(x,y) for x in inp1 for y in inp2] # combination of both in a single list
print (output)
inp3 = []
for i in inp1:             # loop
    for j in inp2:
        inp3.append(tuple((i,j)))
print(inp3)

# #3
inp1 = [1, 3, 6]
inp2 = [1, 2, 5, 14]
inp3 = inp1 + inp2 # adding both variables to create a new variable
print (inp3)
inp3.sort() # sorting from the lowest to the highest
print (inp3)
inp1 = [1, 3, 6]
inp2 = [1, 2, 5, 14]
inp3 =[]
i, j = 0,0       # while loop command
while i < len(inp1):   
    while j < len(inp2):
        if i < j :
            inp3.append(inp1[i])
            i += 1
        else:
            inp3.append(inp2[j])
            j += 1
print(inp3)

# Questions
with open('/Users/marcelonatale/Desktop/ECON611/ECON611/database/hw_2.json') as f:
    data = json.load(f)
    print (data)
item,stock,price,value,minimum,list1,products_50,budget = [],[],[],[],[],[],[],[] # empty list
for i in data:        # i is the first list
    item.append(i[0])   # 0 is the first list position
    stock.append(i[1])  
    price.append(i[2])
    value.append(i[3])
print(item)
print(price)
print(stock)
print(value)
print(max(price))
print(min(price))
i = 0
while i < 3:
    minimum.append(min(price))
    price.remove(min(price))
    i += 1
print(minimum)
for i in stock:    
    for j in price:
        val = i * j
        list1.append(val)
        
        
print(sum(list1))
for i in products_50:  #it will again do the same procedure in the loop
    item.append(i[0])
    stock.append(i[1])
    price.append(i[2])
    value.append(i[3])
for i in stock:  #it will create a new value of the price and stock
    for j in price:   
        val = i * j
        list1.append(val)
        
        
print(sum(list1))


