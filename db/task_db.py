import sqlite3
#import pdb

#u should open database..
conn = sqlite3.connect("db_task.db")
print "database connected sucesfully.."

#create a table with columnbs..
f=open(r"C:\Users\siv\Desktop\db\dummy.txt","r")
b = f.readlines()
a= b[0].split(" ")


'''
conn.execute("""
CREATE TABLE task (
	%s	INTEGER,
	%s	INTEGER,
	%s	TEXT
)""" %(a[0],a[1],a[2])
)
'''

#insert data from text file to this database..
#remove first line beacause its a header
#pdb.set_trace()
print b[1:]
for i in b[1:]:
	c=i.split(" ")
	#print """INSERT INTO task(sno,age,name) VALUES (%s,%s,%s)"""%(c[0],c[3],c[5].strip("\n"))
	conn.execute("""INSERT INTO task(sno,age,name) VALUES (%s,%s,"%s")"""%(c[0],c[3],c[5].strip("\n")))


conn.commit()

conn.close()
