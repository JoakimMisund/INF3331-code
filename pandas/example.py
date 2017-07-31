#!/usr/bin/python3

#Example file for pandas in python 3.5


import pandas as pd # Convention to import as pd
import numpy as np  # Numpy + pandas = <3
import matplotlib.pyplot as plt

datafile = 'data/kodetime.csv'

# We will go though an example of using pandas for data analysis of open data.
# The data used can be found here: https://data.norge.no/data/bouvet-asa/skoler-og-klasser-som-har-meldt-seg-p%C3%A5-kodetimen
# Part of Lær Kidsa Koding

# Please consult https://pandas.pydata.org/pandas-docs/stable/missing_data.html for more.

data = pd.read_csv(datafile)

print("Welcome. This small example shows how you can deal with faulty entries in a dataset.")
print("We have the following dataset of signups for Lær Kidsa Koding:")
print(data.head())
print("I would like to know which county has the most students signed up\n\n")

print("I start by groupby county and aggregate the sum of student")
# The data is loaded, lets see if we can see which county (fylke) has the most students.
# Looking at the output reveals that there is something wrong..
print(data.groupby('county')['students'].aggregate(sum).head())
print("Something is wrong here! The data type of the 'students' column is object.\nInstead of adding the entries as numbers pandas treat them as strings\n\n")
data['students'].dtypes

# The solution is to convert the column students to numeric, however it is not straightforward.
# One of the column values is "corrupted"
print("Trying to convert the student column to numeric using pd.to_numeric")
try:
    data['students'] = pd.to_numeric(data['students'])

except Exception as e:
    print("Oppps, The student column could not be converted to numeric!")
    print("The cause: ")
    print(e)
    print("One or more of the entries contains more than it should..")


# As of now deal with the issue by replacing the entries with NaN.
print("Dealing with the problem by ignoring the entries. Another approach would be to parse the entries and do something smart, but I am lazy.\n\n")
data['students'] = pd.to_numeric(data['students'], 'coerce', downcast='signed')


#We can finaly see which county has the most students
print("With the column converted to numeric we can see which county has the most students signed up for LKK.")
print(data.groupby('county')['students'].aggregate(sum).head().sort_values(ascending=False))


data.groupby('county')['students'].aggregate(sum).head().sort_values(ascending=False).plot(kind="bar")

plt.show()
