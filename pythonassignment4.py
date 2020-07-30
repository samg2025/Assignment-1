#3. Write a program in Python to implement the given flowchart:

a = 10
b = 20
c = 30
avg = (a + b + c)/3
print("avg =", avg)
if avg > a and avg > b and avg > c:
    print("avg is higher than a, b, ,c")
elif avg > a and avg >b:
    print("avg is higher than a, b")
elif avg > a and avg > c:
    print("avg is higher than a, c")
elif avg > b and avg > c:
    print("avg is higher than b, c")
elif avg > a:
    print("avg is just higher than a")
elif avg > b:
    print("avg is just higher than b")
elif avg > c:
    print("avg is just higher than c")

#4. Write a program in Python to break and continue if the following cases occurs:
#●	If user enters a negative number just break the loop and print “It’s Over”
#●	If user enters a positive number just continue in the loop and print “Good Going”

while True:
    x = int(input("Enter a number: "))
    if x > 0:
        print("Good Going")
        continue
    else:
        print("It's Over")
        break

#5. Write a program in Python which will find all such numbers which are divisible  by 7 but are not a multiple of 5, between 2000 and 3200.

for i in range(2000, 3200):
    if i % 7 == 0 and i % 5 != 0:
        print(i)
        
#6. What is the output of the following code examples?
	   x=123 
      for i in x:
    print(i)    
  #Answer: Error will occur. for loop will not be able to iternate int.

	i = 0
while i < 5: # Condition is while i is lower than 5
    print(i) 
    i += 1   # i goes up by value of 1 after every iteration
    if i == 3:  # stops the loop when value of i is 3
        break
else:
    print(“error”) # the program will print "error" as long as i is not equal to 3
# Answer: 0, Error, 1, Error, 2       

	count = 0
while True:
    print(count) # starts from 0
    count += 1   # count goes up by value of 1 after every iteration
    if count >= 5:  # when count is equal to 5 or higher it stops the loop/iteration 
        Break
#Answer: 0,1,2,3,4,5

#7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
   #    Expected output: 0 1 2 4 5
#Note: Use ‘continue’ statement

for i in range(0, 6):
    if i != 3 and i != 6:
        print(i)
        continue

#8. Write a program that accepts a string as an input from user and calculate the number off digits and letters.
    # Expected output: consul12
    # Letters 6
    # Digits 2

output = input("Enter your output: ")
digits = 0
letters = 0
for i in output:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        letters += 1
print(output)
print("Letters:", letters)
print("Digits:", digits)

#9. Read the two parts of the question below: 
# Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever. 

luckyNum = 7
while True:
    guess = int(input("Guess the lucky number: "))
    if guess == luckyNum:
        break
        
# Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want to continue guessing. The program stops if the user guesses the correct number or answers “no”. ( The program continues as long as a user has not answered “no” and has not guessed the correct number)

luckyNum = 7
while True:
    number = int(input("Guess the lucky number: "))
    if number == luckyNum:
        break
    if number != luckyNum:
        answer = input("Do you want to continue guessing: ")
        if answer == "no":
            break
            
#10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
    #        counter=1
#While counter <= 5:
#print(“Type in the”, counter, “number”
#counter=counter+1
#The program asks for five guesses (no matter whether the correct number was guessed or not). If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. After the fifth guess it stops and prints “Game over!”.

luckyNum = 7
counter = 1
while counter <= 5:
    guess = int(input("Guess the number: "))
    if guess != luckyNum and counter != 5:
        print("Try again!")
    if guess == luckyNum:
        print("Good guess!")
    if counter == 5:
        print("Game Over!")
    counter = counter + 1

#11. In the previous question, insert “break” after the “Good guess!” print statement. “break” will terminate the while loop so that users do not have to continue guessing after they found the number. If the user does not guess the number at all, print “Sorry but that was not very successful”.

luckyNum = 7
counter = 1
while counter <= 5:
    guess = int(input("Guess the number: "))
    if guess != luckyNum and counter != 5:
        print("Try again!")
    if guess == luckyNum:
        print("Good guess!")
        break
    if counter == 5:
        print("Game Over!")
        print("Sorry but that was not very successful")
    counter = counter + 1
