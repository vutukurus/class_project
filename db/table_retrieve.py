import sqlite3

#u should open database..
conn = sqlite3.connect("C:\Users\siv\Desktop\db_class.db")
print "database connected sucesfully.."

data = conn.execute("""SELECT SALARY,AGE from student_1""")

for each in data:
	print each



