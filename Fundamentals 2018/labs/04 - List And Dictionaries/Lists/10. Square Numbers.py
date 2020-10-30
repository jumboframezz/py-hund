# 10. Square Numbers
# Read a list of integers and extract all square numbers from it and print them in descending
# order. A square number is an integer which is the square of any integer.
# For example, 1, 4, 9, 16 are square numbers.
# Input                     Output
# 3 16 4 5 6 8 9	        16 9 4
# 12 1 9 4 16 8 25 49 16	49 25 16 16 9 4 1
# •	To find out whether an integer is “square number”, check whether its square
#   root is integer number (has no fractional part):
#   o	if (√num == (int)√num)
import math


def read_int_line():
    striped_line = ""
    # striped_line = "-1 2 -5 100 121 81 49 36 25 24 169 -169"
    #  striped_line = "3 16 4 5 6 8 9"
    if len(striped_line) == 0:
        striped_line = input().strip()

    line = map(int, striped_line.split(" "))
    return list(line)


in_arr = read_int_line()
in_arr.sort(reverse=True)

for item in in_arr:
    if item >= 0 and math.sqrt(item) == int(math.sqrt(item)):
        print(f"{item}", end=" ")
