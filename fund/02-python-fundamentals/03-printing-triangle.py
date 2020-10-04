'''
Printing Triangle

Create a function for printing triangles as shown below:
Examples
Input   Output

3       1
        1 2
        1 2 3
        1 2
        1

4       1
        1 2
        1 2 3
        1 2 3 4
        1 2 3
        1 2
        1

'''


def print_line(high):
        for i in range(1, high + 1):
            print(f"{i} ", end="")
        print("")

x = int(input())

for j in range (1, x+1):
    print_line(j)

for jj in range (j-1,0,-1 ):
    print_line(jj)






