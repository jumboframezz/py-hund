'''
Sort Numbers

	Read a list of integers and sort them in ascending order. Print the output as shown in the examples below.

Examples
Input                   Output

8 2 7 3                 2 <= 3 <= 7 <= 8

2 4 -9                  -9 <= 2 <= 4

Hints
Use the built-in method list.sort().
'''
def read_int_line():
    input_line=""
    input_line=input()
    striped_line=input_line.strip()

    line = map(int, striped_line.split(" "))
    return list(line)

arr=[]
l=""
arr=read_int_line()
arr.sort()

for i in arr:
    l+=str(i) +  " <= "

print (l. strip(" <="))



