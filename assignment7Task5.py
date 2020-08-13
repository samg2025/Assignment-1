# TASK FIVE: HIGHER ORDER FUNCTIONS, GENERATORS, COMPREHENSION

# 1. Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7.
# Make sure to use only higher order function.

theList = [3, 6, 7, 49,  21, 42, 63] ## Using a sample list of values
result = filter(lambda x: (x%3 != 0 and x%7 == 0), theList)
print(list(result))

# 2. Write a program in Python to  multiple the element of list by itself using a traditional function and pass the
# function to map to complete the operation.

theList = [3, 6, 7, 49, 21, 42, 63] ## Using a sample list of values to test the operation

def mul(l):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    return l

result = map(lambda x: x, mul(theList))
print(list(result))

# 3. Write a program to Python find out the character in a string which is uppercase using list comprehension.

p_letters = [i for i in 'pYthonPROjectS' if i.isupper()]
print(p_letters)

# 4. Write a program to construct a dictionary from the two lists containing the names of students and their
# corresponding subjects. The dictionary should maps the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension. HINT-Use Zip function also
# -Student = ['Smit', 'Jaya', 'Rayyan']
# -capital = ['CSE', 'Networking', 'Operating System']
Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']

# Using for loop and dictionary comprehension
mapped = {Student[i]: capital[i] for i in range(len(Student))}
print(mapped)

# Using zip function
mapped = zip(Student, capital)
mapped = dict(mapped)
print(mapped)

# 5. Learn More about Yield, next and Generators

# Generators are a special kind of function that return a lazy iterator. These are objects that you can loop
# over like a lost. However, lazy iterators do not store their contents in memory.
# Generator functions look and act just like regular functions, however, they use Python yield keyword
# instead of return.
# Yield keyword is used in generators instead of return like in regular functions.
# Unlike, return, yield does not exit the function afterwards. Instead the state of the function is remembered.
# Next(), is called on a generator object.

# 6. Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”

def reverse():
    word ='Consultadd Training'[::-1]
    yield(word)

res = reverse()
print(next(res))

# 7. Write any example on decorators.

def decofunc(func):
    def innerfunc():
        print("This is before the function execution.")
        func()
        print("This is after the function execution.")
    return innerfunc

def func_used():
    print("This is inside the function.")

func_used = decofunc(func_used)
func_used()

# 8. Learn about What is FRONT END and its Technologies and Tools
# Make sure to mention at least 5 top notch technologies of Frontend.
# Also mentioned the name of companies using those 5 technologies individually

# Front end refers to the user interface. It is everything with which the user interacts with in a software program
# or website. Therefore, creating this visual part is called front-end development.
# Three main front-end coding languages are HTML(for basic page structure and content), CSS (for visual editing),
# Javascript(for making websites interactive). It is a combination of these three languages that
# creates the front end. The same set of tools is used to create progressive web apps (mobile apps that look and feel
# like a native one but are created with the use of front-end technologies)
# Some of the 5 top notch technologies of Frontend are Vue.js, angular, ionic , npm (node package manager) and grunt.
# vue.js = Google, Nintendo, Trivago
# Angular = Microsoft, MacDonlad's, Apple
# Ionic = Diesel, Mclaren Automotive, Marketwatch
# npm = instacart, reddit, stack
# grunt = Twitter, Mozilla, Opera, Walmart