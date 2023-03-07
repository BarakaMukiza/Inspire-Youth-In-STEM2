#!/usr/bin/env python3
#This is a single line comment
#Name : Baraka Mukiza
# Email : barakakinyua2@gmail.com
# 20th Feb,2023
# File : assignment-1.py

#create an empty list of favourite musicians
#using for loop add 5+ new musicians
#copy to a new list called celebs
#sort the list
#pop out  two celebs from the list 
#count the remaining celebrities

musicians = []
n = int(input("enter number of names required:")) 
for i in range (0,n):
    elem = (input("Enter the names of the musicians :"))
    musicians.append(elem)
print("the created list of names:",musicians)
celebs = musicians.copy()
print(celebs)
celebs.sort()
print(celebs)
celebs.pop(2) 
print(celebs)
celebs.pop(5)
print(celebs)
print(len(celebs))




