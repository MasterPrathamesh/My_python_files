from tkinter import *

int1 = 0
ls = [0,0,0]

ls1 = [""]

def undo1():
    global int1
    int1 = int1 + 1
    if int1 % 2 == 1:
        l1.configure(text="2nd Player Turn")
    elif int1 % 2 == 0:
        l1.configure(text="1st Player Turn")

    if ls1[0] == ".b1" and b1.cget("text") != "":
        b1.configure(text="")
    elif ls1[0] == ".b2" and b2.cget("text") != "":
        b2.configure(text="")
    elif ls1[0] == ".b3" and b3.cget("text") != "":
        b3.configure(text="")
    elif ls1[0] == ".b4" and b4.cget("text") != "":
        b4.configure(text="")
    elif ls1[0] == ".b5" and b5.cget("text") != "":
        b5.configure(text="")
    elif ls1[0] == ".b6" and b6.cget("text") != "":
        b6.configure(text="")
    elif ls1[0] == ".b7" and b7.cget("text") != "":
        b7.configure(text="")
    elif ls1[0] == ".b8" and b8.cget("text") != "":
        b8.configure(text="")
    elif ls1[0] == ".b9" and b9.cget("text") != "":
        b9.configure(text="")

def reset1():
    b1.bind("<Button>", press1); b2.bind("<Button>", press1); b3.bind("<Button>", press1); b4.bind("<Button>", press1); b5.bind("<Button>", press1); b6.bind("<Button>", press1); b7.bind("<Button>", press1); b8.bind("<Button>", press1); b9.bind("<Button>", press1)
    b1.configure(bg="white"); b2.configure(bg="white"); b3.configure(bg="white"); b4.configure(bg="white"); b5.configure(bg="white"); b6.configure(bg="white"); b7.configure(bg="white"); b8.configure(bg="white"); b9.configure(bg="white")
    global int1
    int1 = 0
    l1.configure(text="1st Player Turn")
    b1.configure(text="")
    b2.configure(text="")
    b3.configure(text="")
    b4.configure(text="")
    b5.configure(text="")
    b6.configure(text="")
    b7.configure(text="")
    b8.configure(text="")
    b9.configure(text="")
    l6.configure(text="")

def reset2():
    b1.bind("<Button>", press1); b2.bind("<Button>", press1); b3.bind("<Button>", press1); b4.bind("<Button>", press1); b5.bind("<Button>", press1); b6.bind("<Button>", press1); b7.bind("<Button>", press1); b8.bind("<Button>", press1); b9.bind("<Button>", press1)
    b1.configure(bg="white"); b2.configure(bg="white"); b3.configure(bg="white"); b4.configure(bg="white"); b5.configure(bg="white"); b6.configure(bg="white"); b7.configure(bg="white"); b8.configure(bg="white"); b9.configure(bg="white")
    global int1
    int1 = 0
    l1.configure(text="1st Player Turn")
    b1.configure(text="")
    b2.configure(text="")
    b3.configure(text="")
    b4.configure(text="")
    b5.configure(text="")
    b6.configure(text="")
    b7.configure(text="")
    b8.configure(text="")
    b9.configure(text="")
    l6.configure(text="")
    txt1.delete(0.0, END)
    txt2.delete(0.0, END)
    txt3.delete(0.0, END)


def press1(event):
    global int1
    if int1 % 2 == 0 and event.widget.cget("text") == "":
        int1 = int1 + 1
        str1 = "X"
        l1.configure(text="2nd Player Turn")
    elif int1 % 2 == 1 and event.widget.cget("text") == "":
        int1 = int1 + 1
        str1 = "O"
        l1.configure(text="1st Player Turn")

    a = str(event.widget)
    print(event.widget)
    if a == ".b1" and b1.cget("text") == "":
        b1.configure(text=str1)
        ls1[0] = str(event.widget)
        print(ls1[0])
    elif a == ".b2" and b2.cget("text") == "":
        b2.configure(text=str1)
        ls1[0] = str(event.widget)
    elif a == ".b3" and b3.cget("text") == "":
        b3.configure(text=str1)
        ls1[0] = str(event.widget)
    elif a == ".b4" and b4.cget("text") == "":
        b4.configure(text=str1)
        ls1[0] = str(event.widget)
    elif a == ".b5" and b5.cget("text") == "":
        b5.configure(text=str1)
        ls1[0] = str(event.widget)
    elif a == ".b6" and b6.cget("text") == "":
        b6.configure(text=str1)
        ls1[0] = str(event.widget)
    elif a == ".b7" and b7.cget("text") == "":
        b7.configure(text=str1)
        ls1[0] = str(event.widget)
    elif a == ".b8" and b8.cget("text") == "":
        b8.configure(text=str1)
        ls1[0] = str(event.widget)
    elif a == ".b9" and b9.cget("text") == "":
        b9.configure(text=str1)
        ls1[0] = str(event.widget)

    if b1.cget("text") == b2.cget("text") and b2.cget("text") == b3.cget("text") and str(b3.cget("text")) == "X":
        l6.configure(text="Player 1 Won")
        txt1.delete(0.0, END)
        a = ls[0]
        a = a + 1
        ls[0] = a
        txt1.insert(0.0, str(ls[0]))
        b1.configure(bg="darkviolet")
        b2.configure(bg="darkviolet")
        b3.configure(bg="darkviolet")
        b1.unbind("<Button>"); b2.unbind("<Button>"); b3.unbind("<Button>"); b4.unbind("<Button>"); b5.unbind("<Button>"); b6.unbind("<Button>"); b7.unbind("<Button>"); b8.unbind("<Button>"); b9.unbind("<Button>")

    elif b1.cget("text") == b2.cget("text") and b2.cget("text") == b3.cget("text") and str(b3.cget("text")) == "O":
        l6.configure(text="Player 2 Won")
        txt2.delete(0.0, END)
        a = ls[1]
        a = a + 1
        ls[1] = a
        txt2.insert(0.0, str(ls[1]))
        b1.configure(bg="blue")
        b2.configure(bg="blue")
        b3.configure(bg="blue")
        b1.unbind("<Button>"); b2.unbind("<Button>"); b3.unbind("<Button>"); b4.unbind("<Button>"); b5.unbind("<Button>"); b6.unbind("<Button>"); b7.unbind("<Button>"); b8.unbind("<Button>"); b9.unbind("<Button>")

    elif b4.cget("text") == b5.cget("text") and b5.cget("text") == b6.cget("text") and str(b6.cget("text")) == "X":
        l6.configure(text="Player 1 Won")
        txt1.delete(0.0, END)
        a = ls[0]
        a = a + 1
        ls[0] = a
        txt1.insert(0.0, str(ls[0]))
        b4.configure(bg="darkviolet")
        b5.configure(bg="darkviolet")
        b6.configure(bg="darkviolet")
        b1.unbind("<Button>"); b2.unbind("<Button>"); b3.unbind("<Button>"); b4.unbind("<Button>"); b5.unbind("<Button>"); b6.unbind("<Button>"); b7.unbind("<Button>"); b8.unbind("<Button>"); b9.unbind("<Button>")

    elif b4.cget("text") == b5.cget("text") and b5.cget("text") == b6.cget("text") and str(b6.cget("text")) == "O":
        l6.configure(text="Player 2 Won")
        txt2.delete(0.0, END)
        a = ls[1]
        a = a + 1
        ls[1] = a
        txt2.insert(0.0, str(ls[1]))
        b4.configure(bg="blue")
        b5.configure(bg="blue")
        b6.configure(bg="blue")
        b1.unbind("<Button>"); b2.unbind("<Button>"); b3.unbind("<Button>"); b4.unbind("<Button>"); b5.unbind("<Button>"); b6.unbind("<Button>"); b7.unbind("<Button>"); b8.unbind("<Button>"); b9.unbind("<Button>")

    elif b7.cget("text") == b8.cget("text") and b8.cget("text") == b9.cget("text") and str(b9.cget("text")) == "X":
        l6.configure(text="Player 1 Won")
        txt1.delete(0.0, END)
        a = ls[0]
        a = a + 1
        ls[0] = a
        txt1.insert(0.0, str(ls[0]))
        b7.configure(bg="darkviolet")
        b8.configure(bg="darkviolet")
        b9.configure(bg="darkviolet")
        b1.unbind("<Button>"); b2.unbind("<Button>"); b3.unbind("<Button>"); b4.unbind("<Button>"); b5.unbind("<Button>"); b6.unbind("<Button>"); b7.unbind("<Button>"); b8.unbind("<Button>"); b9.unbind("<Button>")

    elif b7.cget("text") == b8.cget("text") and b8.cget("text") == b9.cget("text") and str(b9.cget("text")) == "O":
        l6.configure(text="Player 2 Won")
        txt2.delete(0.0, END)
        a = ls[1]
        a = a + 1
        ls[1] = a
        txt2.insert(0.0, str(ls[1]))
        b7.configure(bg="blue")
        b8.configure(bg="blue")
        b9.configure(bg="blue")
        b1.unbind("<Button>"); b2.unbind("<Button>"); b3.unbind("<Button>"); b4.unbind("<Button>"); b5.unbind("<Button>"); b6.unbind("<Button>"); b7.unbind("<Button>"); b8.unbind("<Button>"); b9.unbind("<Button>")

    elif b1.cget("text") == b4.cget("text") and b4.cget("text") == b7.cget("text") and str(b7.cget("text")) == "X":
        l6.configure(text="Player 1 Won")
        txt1.delete(0.0, END)
        a = ls[0]
        a = a + 1
        ls[0] = a
        txt1.insert(0.0, str(ls[0]))
        b1.configure(bg="darkviolet")
        b4.configure(bg="darkviolet")
        b7.configure(bg="darkviolet")
        b1.unbind("<Button>"); b2.unbind("<Button>"); b3.unbind("<Button>"); b4.unbind("<Button>"); b5.unbind("<Button>"); b6.unbind("<Button>"); b7.unbind("<Button>"); b8.unbind("<Button>"); b9.unbind("<Button>")

    elif b1.cget("text") == b4.cget("text") and b4.cget("text") == b7.cget("text") and str(b7.cget("text")) == "O":
        l6.configure(text="Player 2 Won")
        txt2.delete(0.0, END)
        a = ls[1]
        a = a + 1
        ls[1] = a
        txt2.insert(0.0, str(ls[1]))
        b1.configure(bg="blue")
        b4.configure(bg="blue")
        b7.configure(bg="blue")
        b1.unbind("<Button>"); b2.unbind("<Button>"); b3.unbind("<Button>"); b4.unbind("<Button>"); b5.unbind("<Button>"); b6.unbind("<Button>"); b7.unbind("<Button>"); b8.unbind("<Button>"); b9.unbind("<Button>")

    elif b2.cget("text") == b5.cget("text") and b5.cget("text") == b8.cget("text") and str(b8.cget("text")) == "X":
        l6.configure(text="Player 1 Won")
        txt1.delete(0.0, END)
        a = ls[0]
        a = a + 1
        ls[0] = a
        txt1.insert(0.0, str(ls[0]))
        b2.configure(bg="darkviolet")
        b5.configure(bg="darkviolet")
        b8.configure(bg="darkviolet")
        b1.unbind("<Button>"); b2.unbind("<Button>"); b3.unbind("<Button>"); b4.unbind("<Button>"); b5.unbind("<Button>"); b6.unbind("<Button>"); b7.unbind("<Button>"); b8.unbind("<Button>"); b9.unbind("<Button>")

    elif b2.cget("text") == b5.cget("text") and b5.cget("text") == b8.cget("text") and str(b8.cget("text")) == "O":
        l6.configure(text="Player 2 Won")
        txt2.delete(0.0, END)
        a = ls[1]
        a = a + 1
        ls[1] = a
        txt2.insert(0.0, str(ls[1]))
        b2.configure(bg="blue")
        b5.configure(bg="blue")
        b8.configure(bg="blue")
        b1.unbind("<Button>"); b2.unbind("<Button>"); b3.unbind("<Button>"); b4.unbind("<Button>"); b5.unbind("<Button>"); b6.unbind("<Button>"); b7.unbind("<Button>"); b8.unbind("<Button>"); b9.unbind("<Button>")

    elif b3.cget("text") == b6.cget("text") and b6.cget("text") == b9.cget("text") and str(b9.cget("text")) == "X":
        l6.configure(text="Player 1 Won")
        txt1.delete(0.0, END)
        a = ls[0]
        a = a + 1
        ls[0] = a
        txt1.insert(0.0, str(ls[0]))
        b3.configure(bg="darkviolet")
        b6.configure(bg="darkviolet")
        b9.configure(bg="darkviolet")
        b1.unbind("<Button>"); b2.unbind("<Button>"); b3.unbind("<Button>"); b4.unbind("<Button>"); b5.unbind("<Button>"); b6.unbind("<Button>"); b7.unbind("<Button>"); b8.unbind("<Button>"); b9.unbind("<Button>")

    elif b3.cget("text") == b6.cget("text") and b6.cget("text") == b9.cget("text") and str(b9.cget("text")) == "O":
        l6.configure(text="Player 2 Won")
        txt2.delete(0.0, END)
        a = ls[1]
        a = a + 1
        ls[1] = a
        txt2.insert(0.0, str(ls[1]))
        b3.configure(bg="blue")
        b6.configure(bg="blue")
        b9.configure(bg="blue")
        b1.unbind("<Button>"); b2.unbind("<Button>"); b3.unbind("<Button>"); b4.unbind("<Button>"); b5.unbind("<Button>"); b6.unbind("<Button>"); b7.unbind("<Button>"); b8.unbind("<Button>"); b9.unbind("<Button>")

    elif b1.cget("text") == b5.cget("text") and b5.cget("text") == b9.cget("text") and str(b9.cget("text")) == "X":
        l6.configure(text="Player 1 Won")
        txt1.delete(0.0, END)
        a = ls[0]
        a = a + 1
        ls[0] = a
        txt1.insert(0.0, str(ls[0]))
        b1.configure(bg="darkviolet")
        b5.configure(bg="darkviolet")
        b9.configure(bg="darkviolet")
        b1.unbind("<Button>"); b2.unbind("<Button>"); b3.unbind("<Button>"); b4.unbind("<Button>"); b5.unbind("<Button>"); b6.unbind("<Button>"); b7.unbind("<Button>"); b8.unbind("<Button>"); b9.unbind("<Button>")

    elif b1.cget("text") == b5.cget("text") and b5.cget("text") == b9.cget("text") and str(b9.cget("text")) == "O":
        l6.configure(text="Player 2 Won")
        txt2.delete(0.0, END)
        a = ls[1]
        a = a + 1
        ls[1] = a
        txt2.insert(0.0, str(ls[1]))
        b1.configure(bg="blue")
        b5.configure(bg="blue")
        b9.configure(bg="blue")
        b1.unbind("<Button>"); b2.unbind("<Button>"); b3.unbind("<Button>"); b4.unbind("<Button>"); b5.unbind("<Button>"); b6.unbind("<Button>"); b7.unbind("<Button>"); b8.unbind("<Button>"); b9.unbind("<Button>")

    elif b3.cget("text") == b5.cget("text") and b5.cget("text") == b7.cget("text") and str(b7.cget("text")) == "X":
        l6.configure(text="Player 1 Won")
        txt1.delete(0.0, END)
        a = ls[0]
        a = a + 1
        ls[0] = a
        txt1.insert(0.0, str(ls[0]))
        b3.configure(bg="darkviolet")
        b5.configure(bg="darkviolet")
        b7.configure(bg="darkviolet")
        b1.unbind("<Button>"); b2.unbind("<Button>"); b3.unbind("<Button>"); b4.unbind("<Button>"); b5.unbind("<Button>"); b6.unbind("<Button>"); b7.unbind("<Button>"); b8.unbind("<Button>"); b9.unbind("<Button>")

    elif b3.cget("text") == b5.cget("text") and b5.cget("text") == b7.cget("text") and str(b7.cget("text")) == "O":
        l6.configure(text="Player 2 Won")
        txt2.delete(0.0, END)
        a = ls[1]
        a = a + 1
        ls[1] = a
        txt2.insert(0.0, str(ls[1]))
        b3.configure(bg="blue")
        b5.configure(bg="blue")
        b7.configure(bg="blue")
        b1.unbind("<Button>"); b2.unbind("<Button>"); b3.unbind("<Button>"); b4.unbind("<Button>"); b5.unbind("<Button>"); b6.unbind("<Button>"); b7.unbind("<Button>"); b8.unbind("<Button>"); b9.unbind("<Button>")

    elif b1.cget("text") != "" and b2.cget("text") != "" and b3.cget("text") != "" and b4.cget("text") != "" and b5.cget("text") != "" and b6.cget("text") != "" and b7.cget("text") != "" and b8.cget("text") != "" and b9.cget("text") != "" :
        l6.configure(text="Match Draw")
        txt3.delete(0.0, END)
        a = ls[2]
        a = a + 1
        ls[2] = a
        txt3.insert(0.0, str(ls[2]))
        b1.unbind("<Button>"); b2.unbind("<Button>"); b3.unbind("<Button>"); b4.unbind("<Button>"); b5.unbind("<Button>"); b6.unbind("<Button>"); b7.unbind("<Button>"); b8.unbind("<Button>"); b9.unbind("<Button>")
        b1.configure(bg="black"); b2.configure(bg="black"); b3.configure(bg="black"); b4.configure(bg="black"); b5.configure(bg="black"); b6.configure(bg="black"); b7.configure(bg="black"); b8.configure(bg="black"); b9.configure(bg="black")


base = Tk()
base.geometry("1500x800")
base.configure(bg="aqua")

b1 = Button(base, text="", name="b1", bg="white", borderwidth=3, height=3, width=6, font=("Times New Roman", 10, "bold"))
b1.place(x=100, y=200)
b1.bind("<Button>", press1)

b2 = Button(base, text="", name="b2", bg="white", borderwidth=3, height=3, width=6, font=("Times New Roman", 10, "bold"))
b2.place(x=200, y=200)
b2.bind("<Button>", press1)

b3 = Button(base, text="", name="b3", bg="white", borderwidth=3, height=3, width=6, font=("Times New Roman", 10, "bold"))
b3.place(x=300, y=200)
b3.bind("<Button>", press1)

b4 = Button(base, text="", name="b4", bg="white", borderwidth=3, height=3, width=6, font=("Times New Roman", 10, "bold"))
b4.place(x=100, y=300)
b4.bind("<Button>", press1)

b5 = Button(base, text="", name="b5", bg="white", borderwidth=3, height=3, width=6, font=("Times New Roman", 10, "bold"))
b5.place(x=200, y=300)
b5.bind("<Button>", press1)

b6 = Button(base, text="", name="b6", bg="white", borderwidth=3, height=3, width=6, font=("Times New Roman", 10, "bold"))
b6.place(x=300, y=300)
b6.bind("<Button>", press1)

b7 = Button(base, text="", name="b7", bg="white", borderwidth=3, height=3, width=6, font=("Times New Roman", 10, "bold"))
b7.place(x=100, y=400)
b7.bind("<Button>", press1)

b8 = Button(base, text="", name="b8", bg="white", borderwidth=3, height=3, width=6, font=("Times New Roman", 10, "bold"))
b8.place(x=200, y=400)
b8.bind("<Button>", press1)

b9 = Button(base, text="", name="b9", bg="white", borderwidth=3, height=3, width=6, font=("Times New Roman", 10, "bold"))
b9.place(x=300, y=400)
b9.bind("<Button>", press1)

b10 = Button(base, text="Reset Match", bg="white", height=1, width=15, font=("Times New Roman", 12), command=reset1)
b10.place(x=800, y=600)

b11 = Button(base, text="Reset Game", bg="white", height=1, width=15, font=("Times New Roman", 12), command=reset2)
b11.place(x=1050, y=600)

b12 = Button(base, text="Undo", bg="white", height=1, width=15, font=("Times New Roman", 12), command=undo1)
b12.place(x=150, y=600)

l0 = Label(base, text=" Tic Tac Toe ", borderwidth=2, relief="solid", bg="aqua", fg="black", font=("Forte", 25))
l0.place(x=630, y=20)

l1 = Label(base, text="1st Player Turn", bg="aqua", fg="black", font=("Arial", 18, "bold"))
l1.place(x=140, y=500)

l2 = Label(base, text="Score Board", bg="aqua", fg="black", font=("Arial", 18, "bold"))
l2.place(x=900, y=100)

l3 = Label(base, text="Player 1 Score", bg="aqua", fg="darkviolet", font=("Arial", 18, "bold"))
l3.place(x=800, y=200)

l4 = Label(base, text="Player 2 Score", bg="aqua", fg="blue", font=("Arial", 18, "bold"))
l4.place(x=800, y=300)

l5 = Label(base, text="Draw", bg="aqua", fg="black", font=("Arial", 18, "bold"))
l5.place(x=800, y=400)

l5 = Label(base, text="Best of 5", bg="aqua", fg="black", font=("Arial", 18, "bold"))
l5.place(x=180, y=100)

l6 = Label(base, text="", bg="aqua", fg="darkblue", font=("Times New Roman", 20, "bold"))
l6.place(x=500, y=300)

l7 = Label(base, text="Player 1 :", bg="aqua", fg="darkviolet", font=("Comic Sans MS", 18, "bold"))
#l7.place(x=500, y=200)

l8 = Label(base, text="Player 2 :", bg="aqua", fg="blue", font=("Arial", 18, "bold"))
#l8.place(x=500, y=300)

txt1 = Text(base, height=1, width=15, font=("Times New Roman", 20, "bold"))
txt1.place(x=1000, y=200)

txt2 = Text(base, height=1, width=15, font=("Times New Roman", 20, "bold"))
txt2.place(x=1000, y=300)

txt3 = Text(base, height=1, width=15, font=("Times New Roman", 20, "bold"))
txt3.place(x=1000, y=400)

base.mainloop()
