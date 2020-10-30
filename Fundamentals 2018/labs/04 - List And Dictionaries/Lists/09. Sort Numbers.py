# 09. Sort Numbers
# Read a list of integers and sort them in ascending order. Print the output as shown in the
# examples below.
# Input         Output
# 8 2 7 3	     2 <= 3 <= 7 <= 8
# 2 4 -9	    -9 <= 2 <= 4

def read_int_line():

    striped_line = input().strip()
    # striped_line = "8 2 7 3"
    line = map(int, striped_line.split(" "))
    return list(line)


in_arr = read_int_line()
rez = ""
in_arr.sort()
for _ in in_arr:
    rez += f"{_} <= "

print(rez[0:-3])