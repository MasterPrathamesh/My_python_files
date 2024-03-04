from tkinter import *
from tkinter import messagebox
import mysql.connector as mq

def save1():
    sr = txt1.get()
    nm = txt2.get()
    city = txt3.get()
    mob = txt4.get()

    q = "insert into student_info values(" + sr + ",'" + nm + "','" + city + "'," + mob + ")"

    con = mq.connect(host="db4free.net", user="gaurav_123", password="gaurav_123", database="gaurav_db", port=3306)
    cur = con.cursor()
    cur.execute(q)
    con.commit()
    con.close()

    messagebox.showinfo("Success", "Data Saved...")
    txt1.delete(0, END)
    txt2.delete(0, END)
    txt3.delete(0, END)
    txt4.delete(0, END)
    txt1.focus()

def reset2():
    txt1.delete(0, END)
    txt2.delete(0, END)
    txt3.delete(0, END)
    txt4.delete(0, END)
    txt1.focus()

base = Tk()
base.geometry("1400x800")
base.configure(bg="cyan")
ft = ("Times New Roman", 16)

lb1 = Label(base, text="Enter Enrollment No. ", font=ft, bg="cyan")
lb1.place(x=400, y=200)

lb2 = Label(base, text="Enter Student Name ", font=ft, bg="cyan")
lb2.place(x=400, y=300)

lb3 = Label(base, text="Enter Student City ", font=ft, bg="cyan")
lb3.place(x=400, y=400)

lb4 = Label(base, text="Enter Contact No. ", font=ft, bg="cyan")
lb4.place(x=400, y=500)

txt1 = Entry(base, font=ft)
txt1.place(x=600, y=200)

txt2 = Entry(base, font=ft)
txt2.place(x=600, y=300)

txt3 = Entry(base, font=ft)
txt3.place(x=600, y=400)

txt4 = Entry(base, font=ft)
txt4.place(x=600, y=500)

b1 = Button(base, text="Save", font=ft, bg="white", command=save1)
b1.place(x=500, y=600)

b2 = Button(base, text="Reset", font=ft, bg="white", command=reset2)
b2.place(x=650, y=600)

base.mainloop()