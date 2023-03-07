#!/usr/bin/env python3
#This is a single line comment
#Name : Baraka Mukiza
# Email : barakakinyua2@gmail.com
# 23th Feb,2023
# File : functions.py

#functions are block of code that are executes together
#functions use 
def print_name():
    print("My name is Baraka")
    print("I am from Meru")
    print("I am 18 yrs old")
    print("I don't have a specific hobby")

#calling/invoking the functions
print_name()


def add_num(num1,num2):
    sum_num = num1+num2
    print(sum_num)

add_num(30,20)
add_num(5,4)
add_num(2,6)

def mult_num(num1,num2):
    reslt = num1*num2
    print(reslt)
mult_num(2,4)
mult_num(4,7)

def sub_num(num1,num2):
    diff_num = num1-num2
    print(diff_num)
sub_num(5,2)
sub_num(9,7)

def div_num(num1,num2):
    quotient = num1/num2
    print(quotient)
div_num(6,2)
div_num(9,3)