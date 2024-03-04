ls1=[]
s=input("Enter Any String :- ")
print()
ls1.append(s)

num=int(input("How Many Times You Wants to Multiply the String :- "))
print()

i=1
while i<num:
    ls1.append(s)
    i=i+1

print(ls1)