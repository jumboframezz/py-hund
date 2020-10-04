'''
Odd Numbers at Odd Positions

	Write a program to read a list of integers and find how many odd numbers at odd positions the list holds. If there are no numbers, which match this criterion,
	do not print anything

Examples

Input                       Output                  Explanation

2 3 5 2 7 9 -1 -7           Index 1 -> 3            Indexes: 0 1 2 3 4 5  6  7
                            Index 5 -> 9            Numbers: 2 3 5 2 7 9 -1 -7
                            Index 7 -> -7           Odd positions with odd numbers: 1, 5 and 7

'''



def read_int_line():
    input_line=""
    input_line=input()
    striped_line=input_line.strip()

    line = map(int, striped_line.split(" "))
    return list(line)

cnt=0
arr=read_int_line()


for i in arr:
    if (i & 1 == 1) and  (cnt & 1 == 1):
        print(f"Index {cnt} -> {i}")
    cnt +=1
