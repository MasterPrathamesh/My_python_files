from tkinter import *

ft = ('Times New Roman',16)

base = Tk()
base.title("Login Form")
base.geometry("800x500")
base.configure(bg='cyan')

lb0=Label(base, text="Login Form", bg='cyan', font=ft)
lb0.place(x=680, y=80)

lb1=Label(base, text="Enter the Username : ",bg='cyan', font=ft)
lb1.place(x=500, y=200)
t1=Entry(base, font=ft)
t1.place(x=700, y=200)

lb2=Label(base, text="Enter the Password : ",bg='cyan', font=ft)
lb2.place(x=500, y=250)
t2=Entry(base, font=ft, show='*')
t2.place(x=700, y=250)

btn1=Button(base, text='Login', bg='white', font=ft)
btn1.place(x=680, y=330)

base.mainloop()