'''
Count of Odd Numbers in List

	Write a program to read a list of integers and find how many odd items it holds.

Examples

Input               Output

1 -2 3 4            2

3 9 -9 -6 1 -2      4
'''


def read_int_line():
    input_line=""
    input_line=input()
    striped_line=input_line.strip()

    line = map(int, striped_line.split(" "))
    return list(line)

cnt=0
arr=read_int_line()


for i in arr:
    if i & 1 == 1:
            cnt +=1
print(cnt)