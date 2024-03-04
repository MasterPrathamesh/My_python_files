from tkinter import *
from tkinter import messagebox

ob = open("Login_Info.txt","a")
ob.close()

def page2():
    pass

def login1():
    flag = 1
    flag1 = 1
    user2 = txt1.get()
    p3 = txt2.get()

    ob = open("Login_Info.txt", "r")
    ls = ob.readlines()
    ob.close()

    for val in ls:
        ls1 = val.split(",")
        if ls1[2] == user2:
            flag = 2
        if ls1[3] == p3:
            flag1 = 2

    if flag == 1:
        messagebox.showerror("invalid!", "Invalid Login Credentials...")
    elif flag == 2 and flag1 == 1:
        messagebox.showerror("invalid!", "Invalid Password...")
    elif flag == 2 and flag1 == 2:
        messagebox.showinfo("invalid!", "You Have Logged In Successfully...")


def reset1():
    txt1.delete(0, END)
    txt2.delete(0, END)

def signup1():
    base.destroy()

    def reset2():
        txt11.delete(0, END)
        txt22.delete(0, END)
        txt33.delete(0, END)
        txt55.delete(0, END)
        txt66.delete(0, END)

    def signup2():
        flag = 1
        ob = open("Login_Info.txt", "r")
        ls = ob.readlines()
        ob.close()

        first = str(txt11.get())
        last = str(txt22.get())
        user = str(txt33.get())
        p1 = str(txt55.get())
        p2 = str(txt66.get())
        user1 = user + "@gmail.com"

        for val in ls:
            ls1 = val.split(",")
            if ls1[2] == user1:
                flag = 2

        if first == "":
            messagebox.showwarning("Warning", "Please Enter First Name...")
        elif last == "":
            messagebox.showwarning("Warning", "Please Enter Last Name...")
        elif user == "":
            messagebox.showwarning("Warning", "Please Enter Username Name...")
        elif p1 == "":
            messagebox.showwarning("Warning", "Please Enter Password...")
        elif flag == 2:
            messagebox.showwarning("Warning", "Username Already Used...")
        else:
            if p1 == p2:
                ob = open("Login_Info.txt", "a")
                ob.write(first + "," + last + "," + user1 + "," + p1 + "," + "\n")
                ob.close()
                messagebox.showinfo("Success!", "Account Successfully Created...")
            else:
                messagebox.showerror("Invalid!", "Password and Confirm Password must be Similar...")

    def check1(getevent):
        val1 = int(var1.get())
        if val1 == 1:
            txt55.configure(show="")
            txt66.configure(show="")
        if val1 == 2:
            txt55.configure(show="*")
            txt66.configure(show="*")

    base1 = Tk()
    base1.geometry("1500x820")
    base1.configure(bg="white")

    var1 = IntVar()
    var1.set(1)

    l00 = Label(base1, text="Create Your Account", bg="white", font=ft2)
    l00.place(x=600, y=20)

    l11 = Label(base1, text="First Name : ", bg="white", font=ft)
    l11.place(x=320, y=150)

    l22 = Label(base1, text="Last Name : ", bg="white", font=ft)
    l22.place(x=720, y=150)

    l33 = Label(base1, text="Username : ", bg="white", font=ft)
    l33.place(x=320, y=250)

    l44 = Label(base1, text="Password : ", bg="white", font=ft)
    l44.place(x=320, y=350)

    l55 = Label(base1, text="Confirm : ", bg="white", font=ft)
    l55.place(x=720, y=350)

    l66 = Label(base1, text="Show Password", bg="white", font=ft)
    l66.place(x=450, y=450)

    txt11 = Entry(base1, font=ft, highlightbackground="blue", highlightthickness=1)
    txt11.place(x=450, y=150)

    txt22 = Entry(base1, font=ft, highlightbackground="blue", highlightthickness=1)
    txt22.place(x=850, y=150)

    txt33 = Entry(base1, width=40, font=ft, highlightbackground="blue", highlightthickness=1)
    txt33.place(x=450, y=250)

    txt44 = Entry(base1, width=11, font=ft, highlightbackground="blue", highlightthickness=1)
    txt44.place(x=850, y=250)
    txt44.insert(0, " @gmail.com")

    txt55 = Entry(base1, font=ft, show="*", highlightbackground="blue", highlightthickness=1)
    txt55.place(x=450, y=350)

    txt66 = Entry(base1, font=ft, show="*", highlightbackground="blue", highlightthickness=1)
    txt66.place(x=850, y=350)

    ch1 = Checkbutton(base1, variable=var1, bg="white", font=ft, offvalue=1, onvalue=2)
    ch1.bind("<Button>", check1)
    ch1.place(x=400, y=450)

    bt11 = Button(base1, text="Sign-Up", bg="white", font=ft, command=signup2)
    bt11.place(x=600, y=550)

    bt11 = Button(base1, text="Reset", bg="white", font=ft, command=reset2)
    bt11.place(x=800, y=550)

    base1.mainloop()


base = Tk()
base.geometry("1500x820")
base.configure(bg="white")

ft = ("Times New Roman", 18)
ft1 = ("Times New Roman", 16)
ft2 = ("Times New Roman", 28)

l0 = Label(base, text="Sign In", bg="white", font=ft2)
l0.place(x=650, y=20)

l1 = Label(base, text="Username : ", bg="white", font=ft)
l1.place(x=500, y=150)

l2 = Label(base, text="password : ", bg="white", font=ft)
l2.place(x=500, y=250)

l3 = Label(base, text="New User", font=ft, bg="white")
l3.place(x=580, y=450)

l4 = Label(base, text="here...", font=ft, bg="white")
l4.place(x=800, y=450)


txt1 = Entry(base, font=ft, highlightbackground="blue", highlightthickness=1)
txt1.place(x=650, y=150)

txt2 = Entry(base, show="*", font=ft, highlightbackground="blue", highlightthickness=1)
txt2.place(x=650, y=250)

bt1 = Button(base, text="Sign-In", bg="white", font=ft, command=login1)
bt1.place(x=600, y=350)

bt2 = Button(base, text="Reset", bg="white", font=ft, command=reset1)
bt2.place(x=750, y=350)

bt3 = Button(base, text="Sign-Up", bg="white", fg="blue", borderwidth=0, command=signup1, font=ft1)
bt3.place(x=700, y=450)

base.mainloop()