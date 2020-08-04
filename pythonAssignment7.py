# 8. Create a new dictionary by concatenating the following two dictionaries:
# a={1:10,2:20}
# b={3:30,4:40}
# Expected Result: {1:10,2:20,3:30,4:40}

a = {1: 10, 2: 20}
b = {3: 30, 4: 40}
a.update(b)   ##adds the elements in the dictionary b to a
print(a)

# 9. Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
# Sample data (n=5)
# Expected Output: {1:1,2:4,3:9,4:16,5:25}

squares = {}
for i in range(1, 6):
    squares[i] = i * i
print(squares)

#10. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#The output should be:
#[‘34’,’67’,’55’,’33’,’12’,’98’]
#(‘34’,’67’,’55’,’33’,’12’,’98’)


x = input("Enter some comma-separated numbers: ")
list = x.split(",")
tuple = tuple(list)
print(list)
print(tuple)
