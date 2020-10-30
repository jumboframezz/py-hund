# 04. Rotate List of Strings
# Write a program to read a list of strings, rotate it to the right and print its rotated items.

def read_string_line():

    striped_line = input().strip()
    line = striped_line.split(" ")
    return list(line)


in_arr = read_string_line()
processed_arr = []

x = in_arr.pop()
in_arr.insert(0, x)

for _ in in_arr:
    print(f"{_}", end=" ")
