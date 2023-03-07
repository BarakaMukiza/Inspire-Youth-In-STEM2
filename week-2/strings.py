#!/usr/bin/env python3
#This is a single line comment
#Strings operations in python
#Name : Baraka Mukiza
# Email : barakakinyua2@gmail.com
# 17th Feb,2023
# File : strings.py

poem = """This is a poem about nothing
        it is funny how people laugh about nothing
        """

print(poem)
print(len(poem))

name1 = "Baraka"
name2 = "Mukiza"
full_name = name1 +" "+name2
age = 17

print("My name is",full_name ,"and my age is",str(age),("years old"))

#Format the string
print("my name is {} and I am {} years old".format(full_name,age)) #best method

#Escape characters
#\t -->tab(spacing)
#\n -->a new line
print("Hello from Baraka \n How are you \n I am fine")

print("Hello from Baraka \t How are you \t I am fine")