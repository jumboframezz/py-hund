'''
Draw a Filled Square

Draw at the console a filled square of size n like in the example:

Examples

Input       Output

4           --------
            -\/\/\/-
            -\/\/\/-
            --------
'''


def draw_edge(len):
    line="-"*len
    print(line)

def draw_body(len):
    line = "\\/"*len
    print(f"-{line}-")


n = int(input())

draw_edge(n*2)
for i in range(0,n-2):
    draw_body(n-1)
draw_edge(n*2)

