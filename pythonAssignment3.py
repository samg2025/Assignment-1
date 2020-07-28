#TASK TWO: OPERATORS AND DECISION MAKING STATEMENTS

#1. Write a program in Python to perform the following operation:

#● If a number is divisible by 3 it should print “Consultadd” as a string

#● If a number is divisible by 5 it should print “c” as a string

#● If a number is divisible by both 3 and 5 its should print “Consultadd Python Training” as a string.

x = int(input("Enter a number: "))
if x%3 == 0 and not (x%3 == 0 and x%5 == 0):
    print("Consultadd")
if x%5 == 0 and not (x%3 == 0 and x%5 == 0):
    print("c")
if x%3 == 0 and x%5 == 0:
    print("Consultadd Python Training"
    
    
#2. Write a program in Python to perform the following operator based task:

#● Ask the user to choose the following option first:

#○ If User Enter 1 - Addition

#○ If User Enter 2 - Subtraction

#○ If User Enter 3 - Division

#○ If USer Enter 4 - Multiplication

#○ If User Enter 5 - Average

#● Ask the user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.

#● Ask the user to enter two more numbers as first1 and second2 for calculating the average as soon as the user chooses an option 5.

#● In the end, if the answer of any operation is Negative print a statement saying “Zsa”

#● NOTE: At a time users can perform one action at a time. 


x = int(input("1-Addition \n2-Subtraction \n3-Division \n4-Multiplication \n5-Average \nChoose from the list above and enter a number: "))

if x == 1 or x == 2 or x == 3 or x == 4:
    first = int(input("Enter a number: "))
    second = int(input("Enter a second number: "))
    if x == 1:
        addition = first + second
        print(addition)
        if addition < 0:
            print("Zsa")
    if x == 2:
        subtraction = first - second
        print(subtraction)
        if subtraction < 0:
            print("Zsa")
    if x == 3:
        division = first/second
        print(division)
        if division < 0:
            print("Zsa")
    if x == 4:
        multiplication = first*second
        print(multiplication)
        if multiplication < 0:
            print("Zsa")

if x == 5:
    first1 = int(input("Enter a number: "))
    second2 = int(input("Enter a second number: "))
    average = (first1+second2)/2
    print(average)
    if average < 0:
        print("Zsa")
