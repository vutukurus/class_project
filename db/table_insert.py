import sqlite3

#u should open database..
conn = sqlite3.connect("C:\Users\siv\Desktop\db_class.db")
print "database connected sucesfully.."

conn.execute("""INSERT INTO student_1(ID,SALARY,ADDRESS,AGE,NAME) VALUES (2,5000,"hyd",65,"iuuuurus")""")
print "inserted values suecssfully"
conn.commit()
print "comited permanely"



conn.close()
print "connection closed.."