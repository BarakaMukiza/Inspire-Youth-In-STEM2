#!/usr/bin/env python3
#This is a single line comment
# do while 
#Name : Baraka Mukiza
# Email : barakakinyua2@gmail.com
# 22th Feb,2023
# # File : advanced_data_types.py

#mutable vs immutable
#mutable are data types that can be edited during pogram life cycle(you can del / remove elements)
#Immutable are data types that cannot be edited during program life cycle
'''
#1.lists
friends = ["Matthew","Michael","Brian"]
# or friends []for empty lists
# to add elements you can use append / extend

students = ["Rooney","Steve"]
friends.extend(students)
print(friends)
 
#reverse

#2.Tuples are type of lists that are immutable
# you use normal brackets
stationaries = ("pens","sharpener","pencil","scarpel")
#you can replace the whole tuple
stationaries = ("ruler","rubber","books")
for stationary in stationaries :
    print(stationary)


numbers = (1,2,3,4)

#3.Dictionaties uses key and value pair to store data
# uses curly brackets
students = { "name" : "Baraka" , "age" : 18, "gender":"male" , "is tall" :"true"}
print(students["name"])
print(students["age"])
print(students["gender"])
print(students["is tall"])
'''
#create a dictionary 
#name it friend 
# it should have fav_colour,hobby,course,weight,height

friend = {"fav_colour":"pink","hobby":"traveling","course":"pharmacy","weight":60 ,"height":125}
print(friend["fav_colour"])
print(friend["hobby"])
print(friend["course"])
print(friend["weight"])
print(friend["height"])

print(friend.keys())
print(friend.values())

#4.sets used to store multiple items in a single variable
my_fruits = {"mangoes","banana","peaches","tomoko"}
for fruit in my_fruits:
    print(fruit)

print(type(my_fruits))








