
# Same example5.py but with different output .
ob = open("testfile6.txt","w")
i = 1
while i <=5 :
    num = int(input("Enter a number"))
    s = num * num
    c = num ** 3

    ob.write("The number is : " + str(num)  +" , " + "The square is :" + str(s) + " , " + "The cube is : " + str(c) + "\n")
    i = i + 1
ob.close()




