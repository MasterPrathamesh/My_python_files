import sqlite3

con = sqlite3.connect("database1.db")
q = "insert into student_info values(33110,'Gaurav',89.67)"
con.execute(q)
con.commit()
con.close()