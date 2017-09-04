#!/usr/bin/python3

# Install openpyxl using pip3
# Documentation: openpyxl.readthedocks.io


from openpyxl import Workbook

wb = Workbook()

ws = wb.active

ws.append(["Name", "Age"])

num_persons = int(input("Please enter number of persons:"))

for i in range(num_persons):
    name = input("Please enter your name:")
    age = input("Please enter you age:")

    ws.append([name, age])

wb.save('sample.xlsx')
