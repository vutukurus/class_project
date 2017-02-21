import sqlite3

#u should open database..
conn = sqlite3.connect("db_class.db")
print "database connected sucesfully.."

#I will create a table..

conn.execute("""
CREATE TABLE student_1 (
	ID	INTEGER,
	SALARY	INTEGER,
	ADDRESS	TEXT,
	AGE	INTEGER,
	NAME	TEXT
)""" 
)

conn.close()


