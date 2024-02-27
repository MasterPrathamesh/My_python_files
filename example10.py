"""
* Functions related to read operations:
1 . read() :
- This function reads and returns entire data of file as single string value .

2 . readline() :
- This function reads single line (where READ cursor is pointing ) and drops the READ cursor to the next line .

3 . readlines() :
- This function reads and returns file data as list where each line becomes elements of list .
"""
# example of read():
ob = open("testfile7.txt","r")
a = ob.read()
print(a)
ob.close()





