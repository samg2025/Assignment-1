#EXTRA ACTIVITIY ON DATA STRUCTURES

#Question 1 and 2 were repeats from previous exercise Task Three

# 3. Create a list of given structure and run

x = [100, 200, 300, 400, 500, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 600, 700, 800]
print(x[5][0:5])
print(x[-3:-1])
print([x[0], x[2], x[4], x[6], x[8]])
y = x[::-1] ##reveres the list x
print([x[::-1][:3], x[5], x[::-1][-5:]])
print(x[5][5][0])
print(x[]) ##syntaxError

# 4. Create a list of thousand number using range and xrange and see the difference between each other.

x = range(0, 1000)
print(x)
print(type(x)) ## return type of range() will be type 'list'
import sys
print(sys.getsizeof(x)) ## returns size of 8064

y = xrange(0, 1000)
print(y)
print(type(y)) ## return type of xrange() will be type 'xrange'
print(sys.getsizeof(y)) ## returns size of 32
# As we can see the range() takes more memory compared to xrange(). This is also due to the reason than the return type
# of range() is list and xrange() is xrange() object.

# 5. How Tuple is beneficial as compare to the list?

# It is useful if you do not want to change the elements in your data structure.
# Creating a list is slower because two memory blocks need to be accessed.
# Also, since tuples are immutable, iterating through a tuple is faster than with a list.


# 6. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is divisible by 3 and a multiple of 2.

x = list(range(1100))
for i in x:
    if i%3 == 0 and i%2 == 0:
        print(i)

# 7. Write a program in Python to reverse a string and print only the vowel alphabet if exist in the string with their index.

# vowels =['a', 'e', 'i', 'o','u']
word = input("Enter a word: ")
reverseWord = word[::-1]
print("The reverse the word is", reverseWord)
for i in reverseWord:
    if i in 'aeiou':
        print("The vowel is", i, "and the position of the vowel is", reverseWord.index(i))

# 8. Write a program in Python to iterate through the string “hello my name is abcde” and print the string which has even length of word.

sentence = "hello my name is abcde"

firstList = list(sentence.split(' '))
for i in firstList:
    if len(i)%2 == 0:
        print("The string with even length of word is", i)

# 9. Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1] #create another list with the same elements to run a double fo loop
result = 8
for i in x:
    for j in y:
        if (i + j) == result:
            print("The pairs are", i, "and", j)

# 10. Write a program in Python to complete the following task:
# Create two different list as in even_list and odd_list
even_list = []
odd_list = []
countEven = 0
countOdd = 0

while True:
    userInput = int(input("Enter a number in the range of 1 to 50: "))
    if userInput%2 == 0:
        even_list.append(userInput)
        countEven += 1
        if countEven == 5:
            print("The sum of the even list is", sum(even_list))
            print("The maximum out of the even list is", max(even_list))
            break
    if userInput%2 != 0:
        odd_list.append(userInput)
        countOdd += 1
        if countOdd == 5:
            print("The sum of the odd list is", sum(odd_list))
            print("The maximum out of the odd list is", max(odd_list))
            break

# 11. Write a program to find out the occurrence of a specific word from an alphanumeric statement.
# Example: 12abcbacbaba344ab
# Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic

count ={}
x = input("Enter a alphanumeric statement: ")
for i in x:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
for key in count:
    if count[key] >= 1 and key.isalpha():
        print(key, "=", count[key])


# 12. Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuple2 = ()
for i in tuple1:
    if i % 2 == 0:
        tuple2 += (i,)
print(tuple2)
