# TASK FOUR: FUNCTION

# 1. Write a program using function to reverse a string.
# Sample data: “1234abcd”
# Expected Output: “dcba4321”

def reverse(a):
    reverseWord = a[::-1]
    return reverseWord
print(reverse('1234abcd'))

# 2. Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
# Expected Output:
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def cases(a):
    upperCount = 0
    lowerCount = 0
    for i in a:
        if i.isupper():
            upperCount += 1
        else:
            lowerCount += 1
    print("No. of upper case characters: ", upperCount)
    print("No. of lower case characters: ", lowerCount)

(cases("SamIr")) ## to check if the function works

# 3. Create a function that takes a list and returns a new list with unique elements of the first list.
def uniquelist(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b

x = [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5] ## created sample list
print(uniquelist(x))  ## to check if the function works

# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

def sorting(a):
    words = [i for i in a.split('-')]
    words.sort()
    print('-'.join(words))

(sorting('zam-lam-ab'))

#5. Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#Sample input:
#Hello world
#Practice makes perfect
#Expected Output:
#HELLO WORLD
#PRACTICE MAKES PERFECT

def uppercap():
    sentence = ["hello world", "practice makes perfect"]
    capList = [x.upper() for x in sentence]
    for i in capList:
        print(i)

uppercap() ##to check if the function works

#6. Define a function that can receive two integral numbers in string form and compute their sum and print it in console.

def calSum(a, b):
    total = int(a)+int(b) # converts a and b into int for addition
    return total

print(calSum('10', '20')) # to test if the function works

#7. Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

def twostr(a, b):
    if len(a) > len(b):
        print("The string with the maximum length is", a)
    if len(b) > len(a):
        print("The string with the maximum length is", b)
    if len(a) == len(b):
        print("Both the strings have the same length. First string is", a)
        print("The second string is", b)

twostr('sssssam','jam') ## to test the function

#8. Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.

def squaretup():
    x = list() ## we will use list since they mutable unlike tuples
    for i in range(1, 20): 
        x.append(i**2)   ## squares the elements
    print(tuple(x)) ## this converts the list to tuple

squaretup() ## to test if the function works

#9. Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.  
#Example: If the limit is 3 , it should print: 
#0 EVEN 
#1 ODD 
#2 EVEN 
#3 ODD 

def showNumbers(limit):
    for i in range(0,(limit+1)):
        if i%2 == 0:
            print(i, "EVEN")
        else:
            print(i, "ODD")

showNumbers(3) ## to check if the function works properly

#10. Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)

theList = list(range(1,21))
result = filter(lambda x: (x%2 == 0), theList)
print(list(result))

#11. Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
#Hints: Use map() to generate a list.
#Use filter() to filter elements of a list
#Use lambda to define anonymous functions

theList = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
squareList = map(lambda x: x*x, theList)
evenNumList = filter(lambda x: (x%2 == 0), squareList)
print(list(evenNumList))

#12. Write a function to compute 5/0 and use try/except to catch the exceptions

try:
    division = 5/0
    print(division)
except:
    print("You cannot divide by zero.")

# 13. Flatten the list [[1,2,3],[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
# Goal : Turn [1,2,3,4,5,6,7] to 1234567

import functools

initialList = [[1, 2, 3], [4, 5], [6, 7, 8]]
result = functools.reduce(lambda x, y: x + y, initialList)  ##this will get rid of the inside lists
delimiter = ''        ##this will remove the space between the values
result1 = functools.reduce(lambda x, y: str(x) + delimiter + str(y), result)
print(result1)

# 14(i)
def foo():
    try:        ##we will try to check the given condition and if there are any error it should allow me to move into another block
        return 1
    finally:    ##will send the user of the program to another loop
        return 2
k = foo()
print(k)  ##therefore k returns 2

# (ii)
def a():
    try:      ##this will try to check if the given function works, which in this case the function f() has not been defined which will cause an error
        f(x, 4)
    finally:      ##prints the following two sentence if an error occurs
        print('after f')
        print('after f?')
a() ##initiates the function
