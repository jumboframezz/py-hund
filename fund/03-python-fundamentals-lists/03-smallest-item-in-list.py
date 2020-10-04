'''
Smallest Item in List

	Write a program to read a list of integers, find the smallest item and print it.

Examples

Input           Output
1 2 3 4         1
'''


def read_int_line():
    input_line=""
    input_line=input()
    striped_line=input_line.strip()

    line = map(int, striped_line.split(" "))
    return list(line)

arr=[]
arr=read_int_line()

arr.sort()
print (arr[0])
