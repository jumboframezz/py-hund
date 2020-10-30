# 08. Sort List Using Insertion Sort*
# Read a list of integers on the first line of the console. After that, sort the list, using the
# Insertion Sort algorithm.
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


# Algorithm
# To sort an array of size n in ascending order:
# 1: Iterate from arr[1] to arr[n] over the array.
# 2: Compare the current element (key) to its predecessor.
# 3: If the key element is smaller than its predecessor, compare it to the elements
# before. Move the greater elements one position up to make space for the swapped element.
line = read_int_line()
for i in range(1, len(line)):
    curr = line[i]
    ii = i - 1
    while ii >= 0 and curr < line[ii]:
        line[ii + 1] = line[ii]
        ii -= 1
    line[ii + 1] = curr

for _ in line:
    print(f"{_}", end=" ")