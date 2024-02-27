# This is the example of writelines() function .
# This function writes the elements of specified sequence / iterable directly into file .
# Strictly the parameter of this function must be a sequence / iterable .
# for ex :
ob = open("testfile9.txt","w")
ls = ["Hello-1\n","Hello-2\n","Hello-3\n","Hello-4\n"]
ob.writelines(ls)
ob.close()