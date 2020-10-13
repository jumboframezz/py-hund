'''
Mixed Phones

You will be given several phone entries, in the form of strings in format:
{firstElement} : {secondElement}

The first element is usually the person’s name, and the second one – his phone number. The phone number consists
ONLY of digits, while the person’s name can consist of any ASCII characters.  Sometimes the phone operator gets
distracted by the Minesweeper she plays all day, and gives you first the phone, and then
the name. e.g. : 0888888888 : Pesho. You must store them correctly, even in those cases.

When you receive the command “Over”, you are to print all names you’ve stored with their phones.
The names must be printed in alphabetical order.

Examples

Input                           Output

14284124 : Alex                 Alex -> 14284124
Gosho : 088423123               Gosho -> 88423123
Ivan : 412048192                Ivan -> 412048192
123123123 : Nanyo               Nanyo -> 123123123
Pesho : 150925812               Pesho -> 150925812
Over


14284124 : Alex
Gosho : 088423123
Ivan : 412048192
123123123 : Nanyo
Pesho : 150925812
Over

'''



in_line=input()
dict = {}
print_dict = {}
while in_line != "Over":
    params = in_line.split(" : ")

    if params[1].isdigit():
        name = params[0]
        value = params[1]
    else:
        name = params[1]
        value = params[0]
    dict[name] = value
    in_line = input()

for i in sorted(dict.keys()):
    print(f"{i} -> {dict[i]}")



