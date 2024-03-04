from tkinter import *
from tkinter import messagebox
import sqlite3

def insert1():

    def insert2():
        enr = txt1.get()
        nm = txt2.get()
        contact = txt3.get()
        city = txt4.get()

        con = sqlite3.connect("database1.db")
        q = "insert into student_info1 values(" + enr + ",'" + nm + "'," + contact + ",'" + city + "')"
        con.execute(q)
        con.commit()
        con.close()

        txt1.delete(0, END)
        txt2.delete(0, END)
        txt3.delete(0, END)
        txt4.delete(0, END)
        txt1.focus_get()
        messagebox.showinfo("Data Inserted Successfully", q)


    base2 = Tk()
    base2.geometry("1500x800")
    base2.configure(bg="cyan")

    l1 = Label(base2, text="Enrollment No. :", bg="cyan", font=("Comic Sans MS", 20))
    l1.place(x=400, y=100)

    txt1 = Entry(base2, font=("Times New Roman", 15))
    txt1.place(x=700, y=110)

    l2 = Label(base2, text="Name :", bg="cyan", font=("Comic Sans MS", 20))
    l2.place(x=400, y=200)

    txt2 = Entry(base2, font=("Times New Roman", 15))
    txt2.place(x=700, y=210)

    l3 = Label(base2, text="Contact No. :", bg="cyan", font=("Comic Sans MS", 20))
    l3.place(x=400, y=300)

    txt3 = Entry(base2, font=("Times New Roman", 15))
    txt3.place(x=700, y=310)

    l4 = Label(base2, text="City :", bg="cyan", font=("Comic Sans MS", 20))
    l4.place(x=400, y=400)

    txt4 = Entry(base2, font=("Times New Roman", 15))
    txt4.place(x=700, y=410)

    b1 = Button(base2, text="Insert", height=1, width=10, font=("Times New Roman", 15), command=insert2)
    b1.place(x=500, y=550)

    b2 = Button(base2, text="Reset", height=1, width=10, font=("Times New Roman", 15))
    b2.place(x=700, y=550)

    base2.mainloop()

def update1():

    def update2():
        enr = txt11.get()
        nm = txt22.get()
        contact = txt33.get()
        city = txt44.get()

        con = sqlite3.connect("database1.db")
        q = "update student_info1 set name = '" + nm + "', contact = " + contact + ", city = '" + city + "' where enr = " + enr
        con.execute(q)
        con.commit()
        con.close()

        txt11.delete(0, END)
        txt22.delete(0, END)
        txt33.delete(0, END)
        txt44.delete(0, END)
        txt11.focus
        messagebox.showinfo("Data Updated Successfully", q)


    base3 = Tk()
    base3.geometry("1500x800")
    base3.configure(bg="cyan")

    l1 = Label(base3, text="Enrollment No. :", bg="cyan", font=("Comic Sans MS", 20))
    l1.place(x=400, y=100)

    txt11 = Entry(base3, font=("Times New Roman", 15))
    txt11.place(x=700, y=110)

    l2 = Label(base3, text="Name :", bg="cyan", font=("Comic Sans MS", 20))
    l2.place(x=400, y=200)

    txt22 = Entry(base3, font=("Times New Roman", 15))
    txt22.place(x=700, y=210)

    l3 = Label(base3, text="Contact No. :", bg="cyan", font=("Comic Sans MS", 20))
    l3.place(x=400, y=300)

    txt33 = Entry(base3, font=("Times New Roman", 15))
    txt33.place(x=700, y=310)

    l4 = Label(base3, text="City :", bg="cyan", font=("Comic Sans MS", 20))
    l4.place(x=400, y=400)

    txt44 = Entry(base3, font=("Times New Roman", 15))
    txt44.place(x=700, y=410)

    b1 = Button(base3, text="Update", height=1, width=10, font=("Times New Roman", 15), command=update2)
    b1.place(x=500, y=550)

    b2 = Button(base3, text="Reset", height=1, width=10, font=("Times New Roman", 15))
    b2.place(x=700, y=550)

    base3.mainloop()

def delete1():

    def delete2():
        ans = val1.get()

        if ans == 1:
            enr = txt1.get()
            con = sqlite3.connect("database1.db")
            q = "delete from student_info1 where enr = " + enr
            con.execute(q)
            con.commit()
            con.close()
            messagebox.showinfo("Row Deleted By Enrollment No.", q)
        elif ans == 2:
            contact = txt1.get()
            con = sqlite3.connect("database1.db")
            q = "delete from student_info1 where contact = " + contact
            con.execute(q)
            con.commit()
            con.close()
            messagebox.showinfo("Data Deleted By Contact No.", q)


    base4 = Tk()
    base4.geometry("1500x800")
    base4.configure(bg="cyan")

    val1 = IntVar()
    val1.set(1)

    r1 = Radiobutton(base4, text="By Enrollment Number", variable=val1, value=1, bg="cyan", font=("Times New Roman", 15))
    r1.place(x=600, y=200)
    r1.select()

    r2 = Radiobutton(base4, text="By Contact Number", variable=val1, value=2, bg="cyan", font=("Times New Roman", 15))
    r2.place(x=600, y=300)

    txt1 = Entry(base4, font=("Times New Roman", 15))
    txt1.place(x=600, y=400)

    b1 = Button(base4, text="Delete", height=1, width=10, font=("Times New Roman", 15), command=delete2)
    b1.place(x=640, y=550)

    base.mainloop()

base = Tk()
base.geometry("1500x800")
base.configure(bg="black")

mb = Menu(base,)

opr = Menu(mb, tearoff=False)
opr.add_command(label="Insert       ctrl+I", command=insert1)
opr.add_command(label="Update       ctrl+U", command=update1)
opr.add_command(label="Delete       ctrl+D", command=delete1)
mb.add_cascade(menu=opr, label="Operations")

base.bind("<Ctrl->")
base.configure(menu=mb)
base.mainloop()