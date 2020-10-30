# 10. Largest N Items*
# Read a list of integers on the first line of the console. On the next line, you will
# receive an integer N. After that, find and print the largest N items the list, sorted
# in descending order.
# Examples
# Input	        Output
# 5 3 4 1 2       5 4 3
# 3

def read_int_line():
    import os
    striped_line = ""
    if os.environ["USERNAME"] == "lachezarg":
        striped_line = "5 3 4 1 2"
    else:
        striped_line = input().strip()
    fline = map(int, striped_line.split(" "))
    return list(fline)

line = read_int_line()
n = int(input())

line.sort(reverse=True)

for _ in range(0, n):
    print(f"{line[_]}", end=" ")
