# Write a program to append several lists of numbers.
#   	Lists are separated by ‘|’.
#   	Values are separated by spaces (‘ ’, one or several)
#   	Order the lists from the last to the first, and their values from left to right.

# Input                             Output
# 1 2 3 |4 5 6 |  7  8              7 8 4 5 6 1 2 3
# 7 | 4  5|1 0| 2 5 |3              3 2 5 1 0 4 5 7
# 1| 4 5 6 7  |  8 9                8 9 4 5 6 7 1


in_line = input()
lst = in_line.split("|")
rez = ""
for item in range(len(lst) - 1, -1, -1):
    for _ in lst[item].split(" "):
        if _ != "":
            rez += _ + " "
print(rez)
