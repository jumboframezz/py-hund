'''
Sum Adjacent Equal Numbers

	Write a program to sum all adjacent equal numbers in a list of decimal numbers, starting from left to right.
	After two numbers are summed, the obtained result could be equal to some of its neighbors and should be summed
	as well (see the examples below).
	Always sum the leftmost two equal neighbors (if several couples of equal neighbors are available).

Examples

Input                       Output                          Explanation

3 3 6 1                     12 1                            3 3 6 1  6 6 1  12 1
8 2 2 4 8 16                16 8 16                         8 2 2 4 8 16  8 4 4 8 16  8 8 8 16  16 8 16
5 4 2 1 1 4                 5 8 4                           5 4 2 1 1 4  5 4 2 2 4  5 4 4 4  5 8 4

Hints

Read the input and parse it to list of numbers.
Find the leftmost two adjacent equal cells.
Replace them with their sum.
Repeat (1) and (2) until no two equal adjacent cells survive.
Print the processed list of numbers.

'''



def read_float_line():
    input_line=""
    input_line=input()
    striped_line=input_line.strip()

    line = map(float, striped_line.split(" "))
    return list(line)

#8 2 2 4 8 16
#arr = read_float_line()
arr =  list(map(float, input().split()))
found =1
if len (arr) >= 3:
    while found == 1:
        for i in range(0, len(arr)-1):
            found = 0
            if arr[i] == arr[i+1]:
                arr[i] *= 2
                found = 1
                del(arr[i+1])
                break

    for i in arr:
        print(f"{i} ", end="")
elif len(arr) == 2:
    print(arr[0] + arr[1])
else:
    print(arr[0])

