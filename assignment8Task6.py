# TASK SIX: FILE HANDLING AND EXCEPTION HANDLING

# 1. Write a program in Python to allow the error of syntax to go in exception.
# HINT: use SyntaxError

try:
    a = 10
    b = 2
    print(a+b))
except SyntaxError:
    print("You have a Syntax error.")

# SyntaxError is not exactly a exception error. It is more of an incorrect statement in the code, for example
# there were one bracket too many hence prompting a syntaxError when you try to run it. As shown in the example above.
# Exception errors are the type of error whenever syntactically correct Python code results in an error.
# Therefore, we cannot pass syntaxError to go in exception.

# 2. Write a program in Python to allow user to open a file by using argv module. If the entered name is incorrect
# throw an exception and ask them to enter the name again. Make sure to use read only mode.
from sys import argv
NameOfProgram, NameOfFile = argv

print('Name of Program is: ', NameOfProgram)
print('Name of file is: ', NameOfFile)
while True:
    try:
        fh=open(NameOfFile)
        content=fh.read()
        print(content)
        fh.close()
        break
    except:
        print('The name of file is incorrect.')
        NameOfFile = input('Enter the correct name of your file again: ')

print('File name is correct!')

# 3. Write a program to handle an error if the user entered the number more than four digits it should return “Please
# length is too short/long !!! Please provide only four digits”

while True:
    try:
        num = input("Enter a number: ")
        if len(num) != 4:
            raise ValueError
        else:
            print("Perfect!")
            break
    except ValueError:
        if len(num) < 4:
            print("Please length is too short!!! Please provide only four digits.")
        if len(num) > 4:
            print("Please length is too long!!! Please provide only four digits.")

# 4. Create a login page backend to ask user to enter the UserEmail and password. Make sure to ask Re-Type Password
# and if the password is incorrect give chance to enter it again but it should not be more than 3 times.

# For this question we will only be checking for correct password as per the question requirement.
userEmail = "johnsmith@gmail.com" #using sample email
password = "rocknroll" #using a sample password to test the login process

inputid = input("Enter your UserEmail: ")
inputpw = input("Enter your password: ")
count = 0
while True:
    try:
        if inputpw != password:
            raise ValueError
        else:
            print("Log in success!")
            break
    except ValueError:
        count += 1
        inputpw = input("Incorrect password. Please re-type your password: ")

    if count == 3:
        print("Your account has been locked due to multiple incorrect passwords.")
        break

# 5. https://www.programiz.com/python-programming/exception-handling
# Go through this link to understand Finally and Raise concept.
# Finally concept: This clause is executed no matter what, and is generally used to release external resources.
# Finally clause guarantees the execution of closing a file, GUI or disconnecting from network.
# Raise concept: We can manually raise exceptions using the raise keyword.
# This raise concept allows us to pass values to the exception to clarify why that exception was raised.

# 6. Read any file using Python File handling concept and return only the even length string from the doc.txt file.
# Consider the content as:
# Hello I am a file
# Where you need to return the data string
# Which is of even length
# Make sure you return the content in
# The same link as it is present.

x = open('doc.txt')  # open doc file
wordList = (x.read().split())  # this line separate each word and stores it into the wordList list
print(wordList)

# Method 1 for printing
# This prints the even length strings in a list
newList = [i for i in wordList if len(i)%2 == 0] # newList store the even length strings
print(newList)  

# Method 2 for printing
# This prints the even length strings individually
for i in newList:
    print(i)
