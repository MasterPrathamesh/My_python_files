ls1=[]
s=input("Enter Any String :- ")
print()
ls1.extend(s)

num=int(input("How Many Times You Wants to Multiply the String :- "))
print()



i=0
while i<len(ls1):
   j = 0
   while j<(num-1):
       ls1.insert(i+1,ls1[i])
       j=j+1
   i=i+num

print(ls1)