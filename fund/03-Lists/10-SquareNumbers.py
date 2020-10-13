'''
Square Numbers

	Read a list of integers and extract all square numbers from it and print them in descending order.
A square number is an integer which is the square of any integer. For example, 1, 4, 9, 16 are square numbers.

Examples

Input                               Output
3 16 4 5 6 8 9                      16 9 4

12 1 9 4 16 8 25 49 16              49 25 16 16 9 4 1

Hints

To find out whether an integer is “square number”, check whether its square root is integer number (has no fractional part):

if (√num == (int)√num) …

To order the results list in descending order use sorting with reverse

'''


import math

def read_int_line():
    input_line=""
    input_line=input()
    striped_line=input_line.strip()

    line = map(int, striped_line.split(" "))
    return list(line)



arr=[]
arr=read_int_line()

arr.sort(reverse=True)
for i in arr:
    if (int(i) >= 0) and (math.sqrt(i) == int(math.sqrt(i)) ):
        print (i, end=" ")



