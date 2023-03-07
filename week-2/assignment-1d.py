#!/usr/bin/env python3
#This is a single line comment
#write a program to list all prime numbers from 1-100
#Name : Baraka Mukiza
# Email : barakakinyua2@gmail.com
# 15th Feb,2023
# File : assignment-1d.py

print("***The values below are prime numbers***")
for prime_numbers in range(1, 101):
   if prime_numbers > 1:
       for i in range(2, prime_numbers):
           if (prime_numbers % i) == 0:
                    break
       else:
           print(prime_numbers)