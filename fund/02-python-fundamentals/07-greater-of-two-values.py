'''
Greater of Two Values
You are given two values of the same type as input. The values can be of type int, char of string. Create a function that returns the greater of the two values:

Examples

Input           Output

int
2
16              16

char
a
z               Z

string
Ivan
Todor           Todor

Hints

For this function you need to create three functions with the same name and different signatures
Create a function which will compare integers.
Lastly you need to create a function to compare the other types.
The last step is to read the input, use appropriate variables and call the function you’ve just written.
'''


def compare_int(a,b):
    if int(a) > int (b):
        return (a)
    else:
        return (b)

def compare_char(a,b):

    if ord(a) > ord(b):
        return(a)
    else:
        return(b)

def compare_string(a,b):
    if a > b:
        return(a)
    else:
        return(b)


in_type = input()
first = input()
second = input()


if in_type == "int":
    print(compare_int(first,second))
elif in_type == "char":
    print(compare_char(first,second))
elif in_type == "string":
    print(compare_string(first,second))


