"""
-----   Read - Write functions in file handling -------

* functions related to write operation :
1 . Write() :
* This function writes specified string into related file through invoking object .
* This function strictly requires string parameter .
* If we are writing any variable , then we must convert it into string .

2 . writelines() :
* This function writes the element of specified sequence / iterable directly into file .
* Strictly the parameter of this function must be a sequence / iterable .

"""
# ex : of write function , and in the next file we'll do example of writelines() function .
a = 15
ob = open("testfile8.txt","w")
ob.write("Hello World..")
ob.write("Hi all ..")
ob.write("Value of a : " + str(a) + "\n")
ob.write("Good day ..")
ob.close()
print("Data Written into file ..")