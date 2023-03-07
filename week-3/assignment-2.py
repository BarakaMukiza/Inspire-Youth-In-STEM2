#!/usr/bin/env python3
#This is a single line comment
# do while 
#Name : Baraka Mukiza
# Email : barakakinyua2@gmail.com
# 21th Feb,2023
# File : .py

#write a program that solves a quadratric equation
#using for loop draw a diamond
#draw a triangle
#draw pascals triangle

import cmath

a = int(input("enter the value of a :"))
b = int(input("enter the value of b :"))
c = int(input("enter the value of c :"))

d = (b**2)-(4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("The solution of the equation are {} and {}".format(sol1,sol2))

print("--------------------------------------------------------------------------------")



h = eval(input("enter the height of the diamond :"))

for x in range (h) :
    print(" "* (h - x), "*" * (2*x + 1))
for x in range (h - 2, -1, -1) :
    print(" " * (h - x), "*" * (2*x +1))

print("----------------------------------------------")


h = eval(input("enter the height of the triangle :"))

for x in range (h) :
    print(" "* (h - x), "*" * (2*x + 1))

print("----------------------------------------------")

for i in range ( 1,h+1):
    for j in range (0,h-i+1):
        print('',end='')

        c = 1
        for j in range (1, i+1):
            print('',c,sep='', end='')
            c=c*(i-j) // j
        print()



