'''
Multiply a List of Integers
Write a program to read a list of integers, an integer p, multiply each item by p and print the resulting list.

Examples

Input               Output

1 3 12 4            4 12 48 16
4

'''


def read_int_line():
    input_line=""
    input_line=input()
    striped_line=input_line.strip()

    line = map(int, striped_line.split(" "))
    return list(line)


arr=[]
result=""

arr=read_int_line()
multiplyer = int(input())


for i in arr:
    result = result + str(i*multiplyer) + " "

print(result)


