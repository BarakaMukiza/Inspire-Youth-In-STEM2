#!/usr/bin/env python3
#This is a single line comment
#Python program to makea table to solve quadratic equation
#Name : Baraka Mukiza
# Email : barakakinyua2@gmail.com
# 16th Feb,2023
# File : quadratic_table.py
#Make a table to solve quadratic equation
from prettytable import PrettyTable

#specify the column names while initializing the table
newTable = PrettyTable(["Variable","Value of x","Equation","Result"])

#add rows
newTable.add_row(["x","0","5x^3 +2 x^2 + 8x + 9  ","9"])
newTable.add_row(["x","1","5x^3 +2 x^2 + 8x + 9 ","26"])
newTable.add_row(["x","2","5x^3 +2 x^2 + 8x + 9 ","73"])
newTable.add_row(["x","3","5x^3 +2 x^2 + 8x + 9 ","180"])
newTable.add_row(["x","4","5x^3 +2 x^2 + 8x + 9 ","377"])
newTable.add_row(["x","5","5x^3 +2 x^2 + 8x + 9 ","694"])
newTable.add_row(["x","6","5x^3 +2 x^2 + 8x + 9 ","1161"])
newTable.add_row(["x","7","5x^3 +2 x^2 + 8x + 9 ","1808"])
newTable.add_row(["x","8","5x^3 +2 x^2 + 8x + 9 ","2665"])
newTable.add_row(["x","9","5x^3 +2 x^2 + 8x + 9 ","3762"])

print(newTable)