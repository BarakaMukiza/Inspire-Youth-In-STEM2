#!/usr/bin/env python3
#This is a single line comment
#Python program to 
#Name : Baraka Mukiza
# Email : barakakinyua2@gmail.com
# 17th Feb,2023
# File : condition.py

#If ........ else
age = 17
gender = "male"

if (age < 18):
    print("You are still young")
else:
    print("You should get an ID")


#compound/multiple conditions

if ((age > 30) & (gender == "male")):
    print("You qualify for a loan")
else:
    print("No loan for you")

fav_colour = "green"
age = 22
if((fav_colour == "green") | (age <= 20)): 
    print("happy birthday")
else:
    print("No happy birthday present for you")

#it still works since it acceps only one of the conditions


