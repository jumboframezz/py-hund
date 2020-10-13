'''

Remove Negatives and Reverse

    Read a list of integers, remove all negative numbers from it and print the remaining items in reversed order. In case of no items left in the list, print “empty”.

Examples

Input                           Output

10 -5 7 9 -33 50                50 9 7 10

7 -2 -10 1                      1 7

-1 -2 -3                        empty

'''


def read_int_line():
    input_line=""
    input_line=input()
    striped_line=input_line.strip()

    line = map(int, striped_line.split(" "))
    return list(line)

arr=[]
rez=[]
arr=read_int_line()

for i in arr:
    if i >= 1:
        rez.append(i)

if len(rez) == 0:
    print("empty")
else:
    rez.reverse()
    for i in rez:
     print (f"{i}", end=" ")




