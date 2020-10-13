'''
Dict-Ref

You have been tasked to create a referenced dictionary, or in other words a dictionary, which knows how to reference itself.
You will be given several input lines, in one of the following formats:

{name} = {value}
{name} = {secondName}

The names will always be strings, and the values will always be integers.
In case you are given a name and a value, you must store the given name and its value. If the name already EXISTS, you must CHANGE its value with the given one.
In case you are given a name and a second name, you must store the given name with the same value as the value of the second name. If the given second name DOES NOT exist, you must IGNORE that input.
When you receive the command “end”, you must print all entries with their value, by order of input, in the following format:

{entry} === {value}

Examples

Input                           Output
Cash = 500
Johny = 5
Cash = 200
Johnny = 200
Car = 150
Plane = 2000000

end

'''

in_line=input()
dict = {}
while in_line != "end":
    params = in_line.split(" = ")
    name = params[0]
    value = params[1]
    if value.isdigit():
        dict[name] = int(value)
    else:
        if dict.get(value):
            dict[name] = dict[value]
    in_line = input()
for key in dict:
    print(f"{key} === {dict[key]}")
