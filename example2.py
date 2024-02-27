"""
- firstly we wil open a file in read mode , then read the data and put the readed data to another file .
- Then we apply the upper() method to convert the readable data to uppercase and store it in another variable / object .
- Then we close that file .
- Then we open the same file in write mode , and pass the  'ndata' variable to the write function and close that file . 
"""
ob = open("C:/Users/Home/PycharmProjects/python_practice3/testfile2.txt","r")
fdata = ob.read()
ndata = fdata.upper()
ob.close()
ob2 = open("C:/Users/Home/PycharmProjects/python_practice3/testfile2.txt","w")
ob2.write(ndata)
ob2.close()