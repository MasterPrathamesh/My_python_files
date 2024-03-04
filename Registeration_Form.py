from tkinter import *

def printt():
    print("Data Inserted Successfully...")

def resett():
    txt1.delete(0,END)
    txt2.delete(0,END)
    txt3.delete(0,END)
    txt4.delete(0,END)
    txt5.delete(0,END)
    txt6.delete(0,END)
    txt7.delete(0,END)
    txt8.delete(0,END)
    txt9.delete(0.0,END)
    txt10.delete(0,END)
    txt11.delete(0,END)
    txt12.delete(0,END)
    txt13.delete(0,END)
    txt1.focus()


base = Tk()
base.title("Registration Form")
base.geometry("1500x820")
base.configure(bg="cyan")

ft = ("TimesRoman", 16)
ft1 = ("TimesRoman", 20)

l1 = Label(base, text="Registration Form", font=ft1, bg="cyan", fg="black")
l1.place(x=650, y=20)

l2 = Label(base, text="First Name : ", font=ft, bg="cyan", fg="black")
l2.place(x=300, y=100)

l3 = Label(base, text="Last Name : ", font=ft, bg="cyan", fg="black")
l3.place(x=700, y=100)

l4 = Label(base, text="Contact No. : ", font=ft, bg="cyan", fg="black")
l4.place(x=300, y=170)

l5 = Label(base, text="Email : ", font=ft, bg="cyan", fg="black")
l5.place(x=700, y=170)

l6 = Label(base, text="Age : ", font=ft, bg="cyan", fg="black")
l6.place(x=300, y=240)

l10 = Label(base, text="DOB : ", font=ft, bg="cyan", fg="black")
l10.place(x=700, y=240)

l12 = Label(base, text="Address : ", font=ft, bg="cyan", fg="black")
l12.place(x=300, y=320)

l7 = Label(base, text="City : ", font=ft, bg="cyan", fg="black")
l7.place(x=300, y=440)

l8 = Label(base, text="Postal/Zip : ", font=ft, bg="cyan", fg="black")
l8.place(x=700, y=440)

l9 = Label(base, text="State : ", font=ft, bg="cyan", fg="black")
l9.place(x=300, y=510)

l11 = Label(base, text="Country : ", font=ft, bg="cyan", fg="black")
l11.place(x=700, y=510)

l13 = Label(base, text="Hobby : ", font=ft, bg="cyan", fg="black")
l13.place(x=300, y=580)

l14 = Label(base, text="Occupation : ", font=ft, bg="cyan", fg="black")
l14.place(x=700, y=580)



txt1 = Entry(base, font = ft, bg = "light cyan2")
txt1.place(x=430, y=100)

txt2 = Entry(base, font=ft, bg = "light cyan2")
txt2.place(x=830, y=100)

txt3 = Entry(base, font=ft, bg = "light cyan2")
txt3.place(x=430, y=170)

txt4 = Entry(base, font=ft, bg = "light cyan2")
txt4.place(x=830, y=170)

txt5 = Entry(base, font=ft, bg = "light cyan2")
txt5.place(x=430, y=240)

txt6 = Entry(base, font=ft, bg = "light cyan2")
txt6.place(x=830, y=240)

txt9 = Text(base, height = 3, width = 53, font=ft, bg = "light cyan2")
txt9.place(x=430, y=320)

txt7 = Entry(base, font=ft, bg = "light cyan2")
txt7.place(x=430, y=440)

txt8 = Entry(base, font=ft, bg = "light cyan2")
txt8.place(x=830, y=440)

txt10 = Entry(base, font=ft, bg = "light cyan2")
txt10.place(x=430, y=510)

txt11 = Entry(base, font=ft, bg = "light cyan2")
txt11.place(x=830, y=510)

txt12 = Entry(base, font=ft, bg = "light cyan2")
txt12.place(x=430, y=580)

txt13 = Entry(base, font=ft, bg = "light cyan2")
txt13.place(x=830, y=580)

b1 = Button(base, text="Submit", font=ft, bg="white", fg = "black", command=printt)
b1.place(x=500, y=700)

b2 = Button(base, text="Reset", font=ft, bg="white", fg = "black", command=resett)
b2.place(x=900, y=700)

base.mainloop()