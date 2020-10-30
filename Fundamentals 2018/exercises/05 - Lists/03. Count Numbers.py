# 03. Count Numbers
# Read a list of integers in range [0…1000] and print them in ascending order along with
# their number of occurrences.
# Input	            Output
# 8 2 2 8 2 2 3 7	2 -> 4
#                   3 -> 1
#                   7 -> 1
#                   8 -> 2
#
# 10 8 8 10 10	    8 -> 2
#                  10 -> 3

# import array

def read_int_line():
    striped_line = ""
    #  striped_line = "8 2 2 8 2 2 3 7"
    if len(striped_line) == 0:
        striped_line = input().strip()
    line = map(int, striped_line.split(" "))
    return list(line)


occurrences = []
counter = []
matrix = []
line = read_int_line()

for _ in line:
    if _ not in occurrences:
        occurrences.append(_)
        counter.append(1)
    else:
        ind = occurrences.index(_)
        counter[ind] += 1

for _ in occurrences:
    ind = occurrences.index(_)
    matrix.append([occurrences[ind], counter[ind]])

matrix.sort()
for _ in range(len(matrix)):
    print(f"{matrix[_][0]} -> {matrix[_][1]}")
