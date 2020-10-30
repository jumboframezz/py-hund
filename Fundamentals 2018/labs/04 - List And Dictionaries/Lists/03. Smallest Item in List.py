# 03. Smallest Item in List
# Write a program to read a list of integers, find the smallest item and print it.


def read_int_line():

    striped_line = input().strip()
    line = map(int, striped_line.split(" "))
    return list(line)


in_arr = read_int_line()
print(min(in_arr))