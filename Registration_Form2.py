from tkinter import*

base = Tk()
base.title("Registration Form")
base.geometry("800x1000")

var1 = StringVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

ft = ("Comic Sans MS", 16)
ft1 = ("Comic Sans MS", 20)

l0 = Label(base, text="Registration Form", font=ft1)
l0.place(x=300, y=20)

l1 = Label(base, text="Student Name : ", font=ft)
l1.place(x=200, y=100)

l2 = Label(base, text="Student College : ", font=ft)
l2.place(x=200, y=200)

l3 = Label(base, text="Student Contact : ", font=ft)
l3.place(x=200, y=300)

l4 = Label(base, text="Student Address : ", font=ft)
l4.place(x=200, y=400)

l5 = Label(base, text="Student Gender : ", font=ft)
l5.place(x=200, y=550)

l6 = Label(base, text="Meal-Plan : ", font=ft)
l6.place(x=200, y=650)


t1 = Entry(base, font=ft)
t1.place(x=400, y=100)

t2 = Entry(base, font=ft)
t2.place(x=400, y=200)

t3 = Entry(base, font=ft)
t3.place(x=400, y=300)

t4 = Text(base, height=3, width=25, font=ft)
t4.place(x=400, y=400)

t5 = Radiobutton(base, text="Male", variable=var1, value="Male", font=ft)
t5.select()
t5.place(x=400, y=550)

t6 = Radiobutton(base, text="Female", variable=var1, value="Female", font=ft)
t6.place(x=500, y=550)

t7 = Checkbutton(base, text="Breakfast", variable=var2, onvalue=1, offvalue=2, font=ft)
t7.place(x=400, y=650)

t8 = Checkbutton(base, text="Lunch", variable=var3, onvalue=1, offvalue=2, font=ft)
t8.place(x=550, y=650)

t9 = Checkbutton(base, text="Dinner", variable=var4, onvalue=1, offvalue=2, font=ft)
t9.place(x=650, y=650)

b1 = Button(base, text="Submit", font=ft, bg="cyan", width=10, height=1)
b1.place(x=250, y=740)

b2 = Button(base, text="Reset", font=ft, bg="cyan", width=10, height=1)
b2.place(x=450, y=740)

base.mainloop()