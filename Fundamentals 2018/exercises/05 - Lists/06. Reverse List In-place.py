# 06. Reverse List In-place
# Read a list of integers on the first line of the console. After that, reverse the list
# in-place (as in, don’t create a new collection to hold the result, reverse it using only the
# original list). After you are done, print the reversed list on the console.
# Note: You are not allowed to iterate over the list backwards and just print it,
#
# Input	            Output
# 1 2 3 4 5	        5 4 3 2 1
# 1 4 2 7 6 1 1	    1 1 6 7 2 4 1
# Hints
# •	Iterate over half of the list (0…length / 2) and swap each item with its opposite
# index like so:
#   o	Index 0 gets swapped with -1
#   o	Index 1 gets swapped with -2,
#   o	Index 2 gets swapped with -3,
#   o	and so on…
# •	When you reach the middle of the list, it means you are done swapping items and are
# ready to print them.


def read_int_line():
    import os
    striped_line = ""
    if os.environ["USERNAME"] == "lachezarg":
        striped_line = "1 2 3 4 5"
        striped_line = "11 52 43 12 1 6"
    else:
        striped_line = input().strip()
    line = map(int, striped_line.split(" "))
    return list(line)

line = read_int_line()
line_len = int(len(line)/2)
for i in range(line_len):
    line[i], line[(0-i)-1] = line[(0-i)-1], line[i]
    #print( i, (0-i)-1)


for _ in line:
    print(f"{_}", end=" ")
