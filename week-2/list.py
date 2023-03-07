#!/usr/bin/env python3
#This is a single line comment
#program to write lists
#Name : Baraka Mukiza
# Email : barakakinyua2@gmail.com
# 15th Feb,2023
# File : list.py
#list of names
names=["James","John","Peter","Gloria","Alex"]

#accessing items in a list
print(names)
print(names[0])
print(names[-1])
print(names[2])
print(names[0:3])

#list of fruits
fruits=["Mango","apple","passion","banana","pawpaw","oranges","pineapple"]
print(fruits)
print(fruits[3])
print("my favourite fruit is:",fruits[1])
print(fruits[1].upper())

#adding two lists
vegetables=["kales","spinach","pigweed","carrots","onions","brocholli"]
stationary=["pens","rubber","sharpener","ruler","scissors","stapler","glue"]
shoppings=vegetables+stationary
print(shoppings)
print(shoppings[5])

#fol-looping until it is stopped-listing items individually
for vegetable in vegetables:
    print(vegetable)

for shopping in shoppings:
    print(shopping)

#using items in a list to make a sentence.
print("my name is " + names[3] + " and my favourite fruit is " + fruits [1] ) 




