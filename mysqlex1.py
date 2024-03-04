import mysql.connector as ms
sr = input("Enter Student Enrollment No. : ")
nm = input("Enter Student Name : ")
city = input("Enter Student City : ")
mob = input("Enter Student Mobile No. : ")

q = "insert into student_info values(" + sr + ",'" + nm + "','" + city + "'," + mob + ")"

con = ms.connect(host="localhost", user="root", password="", database="database1")
cur = con.cursor()
cur.execute(q)
con.commit()
con.close()

print("Data Saved...")