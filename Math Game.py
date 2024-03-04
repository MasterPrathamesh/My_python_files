import random
import time
name=[]
win=[]
t=[]

num=int(input("Enter How Many Players Wants to play :- "))

print("Enter Player Names :- ")
i=0
while i<num:
    print("Player ",i+1," :- ",end="")
    name.append(input())
    i=i+1

n=[0,1,2,3,4,5,6,7,8,9]
o=["+","-","*","<",">","^"]

i=0
while i<num:
    left = random.choice(n)
    opr = random.choice(o)
    right = random.choice(n)
    print()
    print(name[i],"'s Turn...")

    if ord(opr)==43:
        ans1=left+right
    elif ord(opr)==45:
        ans1=left-right
    elif ord(opr)==42:
        ans1=left*right
    elif ord(opr)==60:
        ans1=int(left<right)
    elif ord(opr)==62:
        ans1=int(left>right)
    elif ord(opr)==94:
        ans1=left**right
    else:
        print("Integer Division")
        ans1=left/right

    a=time.perf_counter_ns()
    print("Question :- ",left,opr,right)
    ans=int(input("Enter Correct Answer :- "))
    b=time.perf_counter_ns()

    x=b-a

    if ans==ans1:
        win.append(name[i])
        t.append(x)
    else:
        print("Wrong answer... You Lost...")

    i=i+1

print()
i=0
while i<len(win):
    print(win[i],"has taken",t[i],"nano seconds")
    i=i+1
if len(win)!=0:
    m=min(t)
    won=t.index(m)
    print()
    print(win[won],"Won the Game!!!")
else:
    print("Game Over")

