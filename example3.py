"""
* Remember :
- Use of "\n" , "\t" , "\b" ... are valid in file handling .

-In Python, \n, \t, and \b are escape sequences that represent special characters in strings. When used in file
handling or any string manipulation, they have specific meanings:

1  . \n: Represents a newline character. When used in a string, it creates a new line, causing the text that follows
it to start on a new line.

Example 1:
        with open("example.txt", "w") as file:
         file.write("Line 1\nLine 2\nLine 3")

Output :
        Line 1
        Line 2
        Line 3


2  . \t: Represents a tab character. When used in a string, it inserts a horizontal tab.

Example 2:
            with open("example.txt", "w") as file:
            file.write("Name\tAge\tCity")

Output:
            Name    Age    City

3 . \b: Represents a backspace character. When used in a string, it moves the cursor back one position.

Example:
            with open("example.txt", "w") as file:
            file.write("Hello\bWorld")

Output :
            HellWorld

"""

a = 15
ob = open("testfile3.txt","w")

ob.write("Hello all.. \n")
ob.write("Hi all..\n")
ob.write("value of a is " + str(a) + "\n")
ob.write("Good day..\n")

ob.close()
print("Data is written into file...")

