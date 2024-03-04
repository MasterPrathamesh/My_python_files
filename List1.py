ls=[]
i=0
num=int(input("Enter any Number :-"))

while i<num:
    ls.append([])
    j=0
    while j<=i:
        ls[i].append(i+1)
        j=j+1
    i=i+1

print(ls)