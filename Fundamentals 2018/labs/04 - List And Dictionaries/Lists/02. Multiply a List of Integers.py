# 02. Multiply a List of Integers
# Write a program to read a list of integers, an integer p, multiply
# each item by p and print the resulting list.

def read_int_line():

    striped_line = input().strip()
    line = map(int, striped_line.split(" "))
    return list(line)


result = ""

arr = read_int_line()
multiplayer = int(input())

for i in arr:
    result = result + str(i * multiplayer) + " "

print(result)
