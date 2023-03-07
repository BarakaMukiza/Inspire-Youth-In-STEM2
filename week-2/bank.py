#!/usr/bin/env python3
#This is a single line comment
#write a program that calculates 16 % tax on income
#Name : Baraka Mukiza
# Email : barakakinyua2@gmail.com
# 17th Feb,2023
# File : bank.py

#16%tax on income ranging btwn 100k to 150k

#19% tax income btwn 150k - 300k
#30% tax income above 300k
# 5% tax income less than 100k

#print gross income and net income
gross_income = int(input("Enter your  income :"))
if(gross_income <=100000):
    net = gross_income - (gross_income*0.05)
elif((gross_income > 100000) & (gross_income <= 150000)):
    net = gross_income - (gross_income*0.16)
elif((gross_income > 150000) & (gross_income <= 300000)):
    net = gross_income - (gross_income*0.19)
elif(gross_income >300000):
    net = gross_income - (gross_income*0.3)

print(gross_income)
print(net)

