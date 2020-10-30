# Read a list of integers, remove all negative numbers from it and print the remaining
# items in reversed order. In case of no items left in the list, print “empty”.
# Input                     Output
# 10 -5 7 9 -33 50          50 9 7 10


def read_int_line():

    striped_line = input().strip()
    line = map(int, striped_line.split(" "))
    return list(line)


in_arr = read_int_line()
out_arr = []
for item in in_arr:
    if item > 0:
        out_arr.insert(0, item)

if len(out_arr) == 0:
    print("empty")
else:
    for item in out_arr:
        print(f"{item}", end=" ")
