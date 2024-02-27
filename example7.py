"""
We can also ask User to give the name to the file . ( with extension )
"""

print("Enter the file name , you want to create ( with extension ):")
fname = input()
ob = open(fname,"w")

print("File created ..")
print("Start writing into file..")
data = input()

ob.write(data)
ob.close()

print("Data written successfully..")







