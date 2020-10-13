'''
Filter Base

You have been tasked to sort out a database full of information about employees. You will be given several input lines
containing information in one of the following formats:

{name} -> {age}
{name} -> {salary}
{name} -> {position}

As you see you have 2 parameters. There can be only 3 cases of input:
If the second parameter is an integer, you must store it as name and age.
If the second parameter is a floating-point number, you must store it as name and salary.
If the second parameter is a string, you must store it as name and position.

You must read input lines, then parse and store the information from them, until you receive the command
“filter base”. When you receive that command, the input sequence of employee information should end.

On the last line of input you will receive a string, which can either be “Age”, “Salary” or “Position”. Depending on
the case, you must print all entries which have been stored as
name and age, name and salary, or name and position.

In case, the given last line is “Age”, you must print every employee, stored with its age in the following format:

Name: {name1}
Age: {age1}
====================
Name: {name2}
. . .

In case, the given last line is “Salary”, you must print every employee, stored with its salary in the following format:

Name: {name1}
Salary: {salary1}
====================
Name: {name2}
. . .

In case, the given last line is “Position”, you must print every employee, stored with its position in the following
format:

Name: {name1}
Position: {position1}
====================
Name: {name2}
. . .

NOTE: Every entry is separated with the other, with a string of 20 character ‘=’.

There is NO particular order of printing – the data must be printed in order of input.

Examples
Input
Output
Isacc -> 34
Peter -> CEO
Isacc -> 4500.054321
George -> Cleaner
John -> Security
Nina -> Secretary
filter base
Age

Position
Name: Peter
Position: CEO
====================
Name: George
Position: Cleaner
====================
Name: John
Position: Security
====================
Name: Nina
Position: Secretary
====================
Ivan -> Chistach
Pesho -> Ohrana
Pesho -> 1323.0456
Ivan -> 732.404
Georgi -> 21
Georgi -> 21.02
filter base
Salary
Name: Pesho
Salary: 1323.0456
====================
Name: Ivan
Salary: 732.404
====================
Name: Georgi
Salary: 21.02

====================

Hints:

Use int(), float() and try-except structure to find out in which case are you and where to store the data.

Ivan -> Chistach
Pesho -> Ohrana
Pesho -> 1323.0456
Ivan -> 732.404
Georgi -> 21
Georgi -> 21.02
filter base
Salary


Peter -> CEO
Isacc -> 4500.054321
Isacc -> 34
George -> Cleaner
John -> Security
Nina -> Secretary
Error -> 34.0
filter base
Age

'''


def is_float_try(str):

    try:
        if (float(str) - int(float(str)) == 0):
            return False
        float(str)
        return True
    except ValueError:
        return False

def is_int_try(str):
    try:
        if (float(str) - int(float(str)) == 0):
            return True
        int(str)
        return True
    except ValueError:
        return False

in_line=input().strip(" ")
dict = {}
age={}
salary={}
position={}

while in_line != "filter base":
    params = in_line.split(" -> ")
    in_name = params[0].strip(" ")
    in_param = params[1].strip("")

    if is_int_try(in_param):
        age[in_name] = int(float(in_param))
    elif is_float_try(in_param):
        salary[in_name] = float(in_param)
    else:
        position[in_name] = in_param

    in_line = input()

## Read sort coloumn
sort_criteria=input().strip(" ")

if sort_criteria.lower() == "age":
    for i in age:
        if len(i) == 0:
            continue
        print(f"Name: {i}")
        print(f"Age: {age[i]}")
        print("====================")
elif sort_criteria.lower() == "salary":
    for i in salary:
        if len(i) == 0:
            continue
        print(f"Name: {i}")
        print(f"Salary: {salary[i]}")
        print("====================")
elif sort_criteria.lower() == "position":
    for i in position:
        if len(i) == 0:
            continue
        print(f"Name: {i}")
        print(f"Position: {position[i]}")
        print("====================")

