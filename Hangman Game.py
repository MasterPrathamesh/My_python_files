import random
print("Welcome to Hangman Game")
ls=["java", "python", "android", "programming", "database"]
s=[]
flag=1
count=0
r=random.choice(ls)

a=len(r)

j=0
i=1
while i<=a:
    print(" _ ", end="")
    s.append("_")
    j==j+1
    i=i+1

print("\nGuess the word")

print("Enter 1 to guess letter by letter")
print("Enter 2 to guess the whole word")
ch=int(input("Enter Your Choice :- "))

if ch == 1:
    k=1
    l=0
    while k<=10:
        print("\nChance ", k, " :-")
        print("Enter Letter :-", end="")
        ch = input()
        i=1
        j=0
        while i<=a:
            if r[j]==ch:
                s[j]=ch
                flag=2
            i=i+1
            j=j+1
        print(s)
        if flag==1:
            print("Not Match!")
        print()
        k=k+1
        c=0
        m=1
        while m<=a:
            if s[m-1]!='_':
                c=c+1
            m = m + 1
        if c == a:
            break

    x="_"
    l=len(s)
    k=1
    while k <= l:
        if s[k-1]!=x:
            count=count+1
        k=k+1
    if count == a:
        print("You Win!")
    else:
        print("You Lost...")

if ch == 2:
    print("Enter a whole Word :-", end="")
    word=input()
    l1=len(word)

    if word == r:
        print("You Win!")
    else:
        print("You Lost...")

