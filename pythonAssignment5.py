#TASK THREE: DATA STRUCTURES 

#1. Create a list of the 10 elements of four different types of Data Type like int, string, complex and float. 

newList = [1, 2, 2, 4, "Sam", "James", 2.45, 5+2j, 8.55, 10]
print(newList)    ##prints list with four different types of data type(int, string, complex and float)

#2. Create a list of size 5 and execute the slicing structure.  

newList = [1, 2, 3, 4, 5] ##create a list of size 5
##below are some ways of slicing a list
print(newList[:])  ##prints the whole list
print(newList[1:5]) ##prints the elements from index 1 to index (5-1)
print(newList[3:])   ##prints the elements from index 3 onwards
print(newList[:3])   ##prints the elements from index 0 to index (3-1)
print(newList[1:4:2])   ##prints the elements from index 1 to index (4-1) after skipping an index

#3. Write a program to get the sum and multiply of all the items in a given list. 

theList = [2, 4, 6, 8, 10]
print(sum(theList))   ##sum() adds all the elements in the list together

def multiply(theList):  ##create function to multiply the elements
    multiplyTotal = 1  ##initial at 1 since it's a multiplication, multiplied value gets stored in the variable multiplyTotal as the loop iterates
    for i in theList:
        multiplyTotal *= i 
    return multiplyTotal
    
print(multiply(theList)) ##to get overall mulitplication value of the elements in the list

#4.  Find the largest and smallest number from a given list. 

theList = [2, 4, 6, 8, 10]
print(min(theList))  ##prints the lowest value in the list
print(max(theList))  ##prints the highest value in the list

#5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.  

theList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in theList:
    if i%2 == 0:  #To find out if the value is an even number
        theList.remove(i)  ##Remove element from the list if it is even number
print(theList)  ##rints the altered list without even values

#6. Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

firstList = list(range(1, 31))  ##range(1, 31) inorder to include 30
for i in range(len(firstList)):
    firstList[i] = firstList[i] ** 2  ##squares all elements in the list firstList

newList = firstList[:5] + firstList[-5:]   ##create new list using first 5 and last 5 elements in the new squared values in the list
print(newList)

#7. Write a program to replace the last element in a list with another list. 
#Sample data: [[1,3,5,7,9,10],[2,4,6,8]] 
#Expected output: [1,3,5,7,9,2,4,6,8] 

firstList = [1, 3, 5, 7, 9, 10]
secondList = [2, 4, 6, 8]
newList = firstList[0:-1] + secondList  ##adds firstList without the last element with the secondList
print(newList)

