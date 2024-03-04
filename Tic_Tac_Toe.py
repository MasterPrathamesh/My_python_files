ls=[1,2,3,4,5,6,7,8,9]
pl=[]

print("\n\t\t\t\t\t\t\t---WELCOME TO TIC TAC TOE GAME---")
print("\n---RULES---")
print("1. Player Should Enter A Number From 1-9 To Place Their Character At That Number.")
print("2. When A Similar Characters Arrives 3 Times In A Same Row/Column/Diagonal Then That Player Will Won The Game.")

flag=0
win=0

print()
print("Enter Player Names :-")
pl.append(input("Player 1 :- "))
pl.append(input("Player 2 :- "))
print()
print(pl[0], "'s Character is :- X", sep="")
print(pl[1], "'s Character is :- O", sep="")

i=0
j=0
print()
while i<3:
    while j<len(ls):
        print("|",ls[j]," ",end="")
        j=j+1
        if j%3==0:
            break
    print("|")
    print("----------------",end="")
    print()
    i=i+1

k=0
while True:
    print()
    print(pl[k],"'s Turn :- ",sep="",end="")
    num = int(input())

    l=0
    while l<len(ls):
        if ls[l]==num:
            flag=1
            if k==0:
                ls[l] = "X"
            else:
                ls[l] = "O"
        l=l+1

    if flag==0:
        print("Invalid Input")
        continue

    print()
    i=0
    j=0
    while i < 3:
        while j < len(ls):
            print("|", ls[j], " ", end="")
            j = j + 1
            if j % 3 == 0:
                break
        print("|")
        print("----------------", end="")
        print()
        i = i + 1

    if (ls[0]==ls[1] and ls[1]==ls[2]) or (ls[3]==ls[4] and ls[4]==ls[5]) or (ls[6]==ls[7] and ls[7]==ls[8]) or (ls[0]==ls[3] and ls[3]==ls[6]) or  (ls[1]==ls[4] and ls[4]==ls[7]) or (ls[2]==ls[5] and ls[5]==ls[8]) or (ls[0]==ls[4] and ls[4]==ls[8]) or (ls[2]==ls[4] and ls[4]==ls[6]):
        win=1
        break

    a=0
    m=1
    while m<=9:
        if  ls.count(m) == 1:
            a=a+1
        m=m+1
    if a==0:
        break

    if k==1:
        k=-1

    flag=0
    k=k+1

print()
if win==1:
    print(pl[k], "Won!!!")
    print("Congratulations ",pl[k], "!!!", sep="")
else:
    print("Well Played !!! No One Won...")