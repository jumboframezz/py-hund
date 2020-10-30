# 07. Sort List Using Bubble Sort*
# Read a list of integers on the first line of the console. After that, sort the list,
# using the Bubble Sort algorithm.
# Input	                    Output
# 5 3 4 1 2	                1 2 3 4 5


def read_int_line():
    import os
    striped_line = ""
    if os.environ["USERNAME"] == "lachezarg":
        striped_line = "1 2 3 4 5"
        striped_line = "11 52 43 12 1 6"
    else:
        striped_line = input().strip()
    fline = map(int, striped_line.split(" "))
    return list(fline)


line = read_int_line()
line_len = len(line)
for i in range(line_len - 1):
    for ii in range(0, line_len - i - 1):
        if line[ii] > line[ii + 1]:
            line[ii], line[ii + 1] = line[ii + 1], line[ii]

for _ in line:
    print(f"{_}", end=" ")