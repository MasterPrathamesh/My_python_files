"""
Write a program to accept 5 different numbers from the user and calculate their square and cube . Write this data
in file with proper message .

"""
ob = open("testfile5.txt","w")
i = 1
while i <=5 :
    num = int(input("Enter a number"))
    s = num * num
    c = num * num * num

    ob.write("Number is :" + str(num) + "\n")
    ob.write("Square is :" + str(s) + "\n")
    ob.write("cube is : " + str(c) + "\n" + "\n")
    i = i + 1
ob.close()
