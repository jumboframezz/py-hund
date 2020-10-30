# 05. Smallest Element in List
# Read a list of integers on the first line of the console. After that, find the smallest
# item in the list and print it on the console.
# Input	        Output
# 1 2 3 4 5	         1

import sys
import  os

def read_int_line():
    striped_line = ""
    if os.environ["USERNAME"] == "lachezarg":
        striped_line = "1 2 3 4 5"
    else:
        striped_line = input().strip()
    line = map(int, striped_line.split(" "))
    return list(line)


line = read_int_line()
min_value = sys.maxsize
for _ in line:
    if _ < min_value:
        min_value = _

print(min_value)
