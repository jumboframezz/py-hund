# 06. Odd Numbers at Odd Positions
# Write a program to read a list of integers and find how many odd numbers at odd positions the
# list holds. If there are no numbers, which match this criterion, do not print anything
# Input: 2 3 5 2 7 9 -1 -7  Output: Index 1 -> 3
#                                   Index 5 -> 9
#                                   Index 7 -> -7

def read_int_line():

    striped_line = input().strip()
    line = map(int, striped_line.split(" "))
    return list(line)


in_arr = read_int_line()

arr_index = 0
for _ in range(len(in_arr)):
    if arr_index % 2 != 0 and in_arr[arr_index] % 2 != 0:
        print(f"Index {arr_index } -> {in_arr[arr_index]}")
    arr_index += 1
