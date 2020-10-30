# 04. List Contains Item
# Read a list of integers on the first line of the console and an integer N from the second
# line of the console and print whether the item is contained in the list. If it is, print “yes”,
# otherwise print “no”.
# Examples
# Input	            Output
# 1 2 3 4 5         yes
# 5
#
# 8 7 7 9 6 2 2     no
# 11
# 99 7 8 6 2314 2   yes
# 2314
#
# Hints
# •	Read a text line from the console, split it by space, parse the obtained items as integers
# and convert them to list of integers.
# •	Scan through the whole list, item by item, until you either find the item, or reach
# the end of the list.
#   •	Keep the result of the operation in a Boolean variable such as “isFound”.
#   •	Finally, if the item is found (checking by the variable), print “yes” or “no”.

def read_int_line():
    striped_line = ""
    # striped_line = "1 2 3 4 5"
    if len(striped_line) == 0:
        striped_line = input().strip()
    line = map(int, striped_line.split(" "))
    return list(line)


line = read_int_line()
n = int(input())
found = False
'''
if n in line:
    print("yes")
else:
    print("no")
'''
for _ in line:
    if _ == n:
        found = True

if found:
    print("yes")
else:
    print("no")
