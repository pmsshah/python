#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")

conn = sqlite3.connect('chinook.db') # connect to database

EmpCol=[]
query = conn.execute("pragma table_info('employees')") # This line performs query and returns json result
for row in query:
	print ("\t", row[1], "\n")
	EmpCol.append(row[1])

query = conn.execute("select * from employees") # This line performs query and returns json result
for row in query:
	print("\n")
	for i, val in enumerate(row): 
	    print ("\t", EmpCol[i], " : ", val) 