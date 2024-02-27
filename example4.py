"""
- Write a program to accept details of 5 students from the user and write those details into file with a proper
message .

- Step 1 : Open file in 'w' or 'a' mode .
- step 2 : prepare while loop for 5 iterations and accept details of students in it .
- step 3 : after accepting details , write those values into file with proper message .
- step 4 : close the file when loop stops .

"""

ob = open("testfile4.txt","w")
i = 1
while i <= 5 :
    roll = input("Enter Roll number : ")
    name = input("Enter name : ")
    avg = input("Enter average : ")
    ob.write("Roll number is : " + roll + "\n")
    ob.write("Name is : " + name + "\n")
    ob.write("Average is : " + avg + "\n" + "\n")
    i = i + 1
ob.close()




