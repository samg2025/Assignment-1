

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

