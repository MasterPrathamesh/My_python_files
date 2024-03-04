from tkinter import *

base3 = Tk()
base3.geometry("1500x800")
base3.configure(bg="cyan")

l1 = Label(base3, text="Enrollment No. :", bg="cyan", font=("Comic Sans MS", 20))
l1.place(x=400, y=100)

txt1 = Entry(base3, font=("Times New Roman", 15))
txt1.place(x=700, y=110)

l2 = Label(base3, text="Name :", bg="cyan", font=("Comic Sans MS", 20))
l2.place(x=400, y=200)

txt2 = Entry(base3, font=("Times New Roman", 15))
txt2.place(x=700, y=210)

l3 = Label(base3, text="Contact No. :", bg="cyan", font=("Comic Sans MS", 20))
l3.place(x=400, y=300)

txt3 = Entry(base3, font=("Times New Roman", 15))
txt3.place(x=700, y=310)

l4 = Label(base3, text="City :", bg="cyan", font=("Comic Sans MS", 20))
l4.place(x=400, y=400)

txt4 = Entry(base3, font=("Times New Roman", 15))
txt4.place(x=700, y=410)

b1 = Button(base3, text="Save", height=1, width=10, font=("Times New Roman", 15))
b1.place(x=500, y=550)

b2 = Button(base3, text="Reset", height=1, width=10, font=("Times New Roman", 15))
b2.place(x=700, y=550)

base3.mainloop()
