'''
Rotate List of Strings

	Write a program to read a list of strings, rotate it to the right and print its rotated items.

Examples
Input                   Output
a b c d e               e a b c d
soft uni hi             hi soft uni

'''


def read_string_line():
    input_line=""
    input_line=input()
    striped_line=input_line.strip()

    line = striped_line.split(" ")
    return list(line)


arr=read_string_line()
last = arr.pop()
arr.insert(0, last)


for i in arr:
    print(i, end=" ")


