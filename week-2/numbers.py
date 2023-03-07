#!/usr/bin/env python3
#This is a single line comment
#Assignment 10 : Get the average of numbers in a list by first entering them as input
#Name : Baraka Mukiza
# Email : barakakinyua2@gmail.com
# 16th Feb,2023
# File : numbers.py

numbers = [] 
n = int(input("Enter the number of elements: ")) 
for i in range(0, n): 
    elem = int(input("Enter the elements: ")) 
    numbers.append(elem) 
avg = sum(numbers)/n
print("The created list: ",numbers)
print("The average = ",avg) 