from tkinter import *

def event1():
    n1 = int(txt1.get())
    n2 = int(txt2.get())

    n3 = n1 + n2

    txt3.delete(0, END)
    txt3.insert(0, str(n3))

def event2():
    n1 = int(txt1.get())
    n2 = int(txt2.get())

    n3 = n1 - n2

    txt3.delete(0, END)
    txt3.insert(0, str(n3))

def event3():
    n1 = int(txt1.get())
    n2 = int(txt2.get())

    n3 = n1 * n2

    txt3.delete(0, END)
    txt3.insert(0, str(n3))

def event4():
    n1 = int(txt1.get())
    n2 = int(txt2.get())

    n3 = n1 / n2

    txt3.delete(0, END)
    txt3.insert(0, str(n3))


base = Tk()
base.title("Calculator")
base.geometry("1500x820")
base.configure(bg="cyan")

ft = ("TimesRoman", 16)
ft1 = ("TimesRoman", 20)

txt1 = Entry(base, font = ft, bg = "light cyan2")
txt1.pack()

txt2 = Entry(base, font=ft, bg = "light cyan2")
txt2.pack()

b1 = Button(base, text="Addition", font=ft, bg="white", fg = "black", command=event1)
b1.pack()

b2 = Button(base, text="Subtraction", font=ft, bg="white", fg = "black", command=event2)
b2.pack()

b1 = Button(base, text="Multiplication", font=ft, bg="white", fg = "black", command=event3)
b1.pack()

b2 = Button(base, text="Division", font=ft, bg="white", fg = "black", command=event4)
b2.pack()

txt3 = Entry(base, font=ft, bg = "light cyan2")
txt3.pack()

base.mainloop()