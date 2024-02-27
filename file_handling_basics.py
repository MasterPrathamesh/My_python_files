"""
This is the 3rd file of python_practice of Data Science and Machine Learning program .
- We will going to learn file handling in this file .

Step 1 : Open file in required mode .
step 2 : perform operations.
step 3 : close that file .

- There are two types of files :
        - Plain text file : no text formatting
        - Rich text file : allows text formatting

- To open a file  ,we have open() function .
- This function requires two parameters :
            - file name with extension .
            - file opening mode (default 'r' mode ).

- This function returns an object which we can use to work with that file .
 # For ex :
    ob = open("testfile.txt","w")
    print(type(ob))

- This object 'ob' is totally responsible to do any operations on 'testfile.txt' .

# For ex :
    ob1 = open("testfile1.txt","w")
    ob2 = open("file2.txt","w")

- To do any operation on 'testfile1.txt' we have to use 'ob1'
- To do any operation on 'file2.txt' we have to use ob2 .


*** File opening modes:
1 . 'r' --> read mode
- if we open a file in read mode , then we can only perform read operations from it .
- if we open a file in read mode , then that file must exist .
- if that file is not present then shows error .

2. 'w' --> write mode - if we open a file in write mode , then we can only perform write operation in it. - if we
open a file in write mode and that file does not exists , then automatically creates new blank file with that name.
- if we open a file in write mode and that file already exists then it gets truncated . (old data gets deleted)

3. 'a' --> append mode - if we open a file in append mode , then we can only perform write operation . - if we open a
file in append mode, and that file does not exists , then automatically creates new blank file with that name. - if
we open a file in append mode , and that file already exists then simply that file gets opened to write . old data
remains .

# "+" is string-concatenation operator  . if you don't convert each element to a string before writing it to the file,
you may encounter a TypeError because the write method expects a string as an argument. In your case, the elements in
the list ls are integers, so you need to convert them to strings using str(). """


# Ex 1 :
ls = [1,2,3,4,5,6,7,8,9,10]
ob = open("testfile1.txt","w")
for ele in ls:
    ob.write(str(ele) + "\n")
ob.close()

