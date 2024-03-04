ls=[]
ls1=[]
n=input("Enter String :- ")
a=len(n)
i=0
while i<a:
    ls.append([])
    ls[i].extend(n)
    i=i+1

i=0
while i<a:
    i=i+1

b=a-1
i=0
j=int(0)
while i<b:
    j=i+1
    while j<a:
        ls[i].pop(0)
        j=j+2
    i=i+1

print(ls)
