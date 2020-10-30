# 05. Count of Odd Numbers in List
# Write a program to read a list of integers and find how many odd items it holds.
# input: 1 -2 3 4	    Output: 2


def read_int_line():

    striped_line = input().strip()
    line = map(int, striped_line.split(" "))
    return list(line)


in_arr = read_int_line()
counter = 0

for _ in in_arr:
    if _ % 2 != 0:
        counter += 1

print(counter)