import random;
ls=[]
num=int(input("Enter No. of Players Wants to play :-  "))

print("Enter Player Names :-")
i=0
while i<num:
    print("Player ",i+1,":- ",end="")
    s=input()
    ls.append(s)
    i=i+1

print()
print("Game Starts Here...")
print("---Play Now---")

count=0
while 1:
    i=0
    print()
    count=0
    while i<len(ls):
        print(ls[i],"'s Turn",sep="")
        num=input("Press Enter To Play :-")
        a = random.randrange(1, 7)
        print(a)
        print()
        if a==6:
            count=count+1
            print()
            i=i-1
        if count==1 and a==6:
            print(ls[i+1], " Got One More Chance!")
        if count==2:
            i=i-1
            i=i-1
            break
        i = i + 1

    if count == 2:
        break


if count==2:
    print(ls[i]," Won The Game!")
    print("Congratulations",ls[i],"!!!!!!")