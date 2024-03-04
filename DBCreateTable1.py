from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox

i1 = 5
i2 = 2
i3 = 7

ls = []

def click1(event):
    table = txt1.get()
    con = sqlite3.connect("database1.db")
    q = "create table " + table + " ("
    i = 1
    while True:
        q = q + ls[i-1] + " " + ls[i] + "(" + ls[i+1] + ")"
        if i == len(ls) - 2:
            break
        q = q + ", "
        i = i + 3

    q = q + ")"
    print(q)
    con.execute(q)
    con.commit()
    con.close()
    messagebox.showinfo("Table Created Successfully...", q)
    base.mainloop()

def click2(event):
    global i1, i2, i3
    #count = count + 1
    def click3(event):
        val1 = txt2.get()
        val2 = choose.get()
        val3 = txt4.get()
        ls.append(val1)
        ls.append(val2)
        ls.append(val3)
        print(ls)

    i1 = i1 + 1
    txt2 = Entry(base, font=("Times New Roman", 15))
    txt2.grid(row=i1,  column=i2)
    i2 = i2 + 2

    n = StringVar()
    choose = ttk.Combobox(base, font=("Times New Roman", 15), textvariable=n)
    choose['values'] = ("BOOLEAN", "CHAR", "DATE", "DATETIME", "DECIMAL", "DOUBLE", "INTEGER", "NUMERIC", "STRING", "TEXT", "VARCHAR")
    choose.grid(row=i1, column=i2)

    i2 = i2 + 2

    txt4 = Entry(base, font=("Times New Roman", 15))
    txt4.grid(row=i1, column=i2)

    # ls.append(txt2.get())
    # ls.append(txt3.get())
    # ls.append(txt4.get())
    # print(ls)

    b2 = Button(base, text="Add Data", height=1, width=10, borderwidth=0, bg="cyan", fg="darkblue", font=("Times New Roman", 15))
    b2.grid(row=i1, column=i3)
    b2.bind("<Button-1>", click3)

    i2 = 2



base = Tk()
base.geometry("1500x800")
base.configure(bg="cyan")

l1 = Label(base, text="Enter Table Name : ", bg="cyan", font=("Comic Sans MS", 20))
l1.place(x=300, y=50)

txt1 = Entry(base, font=("Times New Roman", 15))
txt1.place(x=630, y=60)

b1 = Button(base, text="Create Table", height=1, width=10, borderwidth=0, bg="cyan", fg="darkblue", font=("Times New Roman", 15))
b1.place(x=850, y=60)
b1.bind("<Button-1>", click1)

l01 = Label(base, text="", width=10, bg="cyan", font=("Comic Sans MS", 20))
l01.grid(row=0, column=0)

l02 = Label(base, text="", width=5, bg="cyan", font=("Comic Sans MS", 20))
l02.grid(row=1, column=1)

l03 = Label(base, text="", width=10, bg="cyan", font=("Comic Sans MS", 20))
l03.grid(row=2, column=1)

l04 = Label(base, text="", width=10, bg="cyan", font=("Comic Sans MS", 20))
l04.grid(row=3, column=3)

l05 = Label(base, text="", width=10, bg="cyan", font=("Comic Sans MS", 20))
l05.grid(row=3, column=5)

l2 = Label(base, text="Column Name", bg="cyan", font=("Comic Sans MS", 20))
l2.grid(row=3, column=2)
# l2.place(x=300, y=150)

l3 = Label(base, text="Datatype", bg="cyan", font=("Comic Sans MS", 20))
l3.grid(row=3, column=4)
# l3.place(x=400, y=150)

l4 = Label(base, text="Length", bg="cyan", font=("Comic Sans MS", 20))
l4.grid(row=3, column=6)
# l4.place(x=500, y=150)

# txt2 = Entry(base, font=("Times New Roman", 15))
# txt2.grid(row=5, column=2)
#
# txt3 = Entry(base, font=("Times New Roman", 15))
# txt3.grid(row=5, column=4)
#
# txt4 = Entry(base, font=("Times New Roman", 15))
# txt4.grid(row=5, column=6)

b2 = Button(base, text="Add Column", height=1, width=10, borderwidth=0, bg="cyan", fg="darkblue", font=("Times New Roman", 15))
b2.place(x=1000, y=60)
b2.bind("<Button-1>", click2)

base.mainloop()
