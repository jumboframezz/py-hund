'''
Append Lists

	Write a program to append several lists of numbers.
	Lists are separated by ‘|’.
	Values are separated by spaces (‘ ’, one or several)
    Order the lists from the last to the first, and their values from left to right.

Examples

Input                                           Output

1 2 3 |4 5 6 |  7  8                            7 8 4 5 6 1 2 3
7 | 4  5|1 0| 2 5 |3                            3 2 5 1 0 4 5 7
1| 4 5 6 7  |  8 9                              8 9 4 5 6 7 1

Hints

Create a new empty list for the results.
Split the input by ‘|’ into list of tokens.
Pass through each of the obtained tokens from tight to left.
For each token, split it by space and append all non-empty tokens to the results.

Print the results.

'''


input_line = input()
arr=input_line.split("|")
slice_cnt = 0
slices = []

for i in arr:
    clean_slice = " ".join(i.split())
    if len(clean_slice) >= 1:
        slices.append(clean_slice)
        slice_cnt += 1

for j in range (slice_cnt-1, -1, -1):
        print (slices[j], end=" ")

