from tkinter import *

def event1(getevent):
    a = 0
    n1 = txt1.get()
    n2 = txt2.get()

    ans = "See Addition Here"
    if len(n1) > 0 and len(n2) > 0 and txt1.get() != "Enter First Number" and txt2.get() != "Enter Second Number":
        n1 = int(n1)
        n2 = int(n2)
        ans = n1 + n2

    txt3.delete(0, END)
    txt3.insert(0, ans)

def event2(getevent):
    txt1.delete(0, END)
    txt2.delete(0, END)
    txt3.delete(0, END)
    txt1.insert(0, "Enter First Number")
    txt2.insert(0, "Enter Second Number")
    txt3.insert(0, "See Addition Here")

def event3(getevent):
    txt1.delete(0, END)

def event4(getevent):
    if len(txt1.get()) == 0:
      txt1.insert(0, "Enter First Number")

def event5(getevent):
    txt2.delete(0, END)

def event6(getevent):
    if len(txt2.get()) == 0:
      txt2.insert(0, "Enter Second Number")

def event7(getevent):
    txt3.delete(0, END)

def event8(getevent):
    if len(txt3.get()) == 0:
      txt3.insert(0, "See Addition Here")

base = Tk()
base.geometry("500x300")

txt1 = Entry(base)
txt1.insert(0, "Enter First Number")
txt1.pack()
txt1.bind("<FocusIn>", event3)
txt1.bind("<FocusOut>", event4)

txt2 = Entry(base)
txt2.insert(0, "Enter Second Number")
txt2.pack()
txt2.bind("<FocusIn>", event5)
txt2.bind("<FocusOut>", event6)

bt1 = Button(base, text="Add")
bt1.pack()
bt1.bind("<Enter>", event1)
bt1.bind("<Leave>", event2)

txt3 = Entry(base)
txt3.insert(0, "See Addition Here")
txt3.pack()
txt3.bind("<FocusIn>", event7)
txt3.bind("<FocusOut>", event8)

base.mainloop()
