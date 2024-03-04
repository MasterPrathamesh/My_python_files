ob = open("Issued_Book.txt", "r")
count = 0
str1 = 0
flag = 0
while True:
    str1 = ob.readline()
    if count == 2:
        flag = 1
        print(str1)
        str2 = str1.replace("N","Y")
        #str1 = str(ls)
        #ls1 = ob.readlines()
        #print(ls1)
        #ls1.insert()
        #print(ls1)
        #ob = open("Issued_Book.txt", "w")
        #ob.writelines(str2)
        break

    count = count + 1



ob = open("Issued_Book.txt", "r")
ls1 = ob.readlines()
print(ls1)
ls1[2] = str2

print(ls1)

ob = open("Issued_Book.txt", "w")
ob.writelines(ls1)

#ob = open("Issued_Book.txt", "w")
#ob.write(str1)

ob.close()