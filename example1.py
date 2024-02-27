# we can also give the whole path of the file to the open function. and if the file is not present then it creates a
# new file automatically . In the output we'll see the print statement is in upper case , because in the nextfile
# which is example2.py we have taken this testfile2.txt  which will convert the file's data to upper case .

ls = [1,2,3,4,5,6,7,8,9,10]
ob = open("C:/Users/Home/PycharmProjects/python_practice3/testfile2.txt","w")
for ele in ls:
    ob.write("value of ele is : " + str(ele) + "\n" )
ob.close()

