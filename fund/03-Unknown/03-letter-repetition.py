'''
Letter Repetition

You will be given a single string, containing random ASCII character. Your task is to print every character, and how many times it has been used in the string.

Examples

Input                       Output
aaabbaaabbbccc              a -> 6
                            b -> 5
                            c -> 3

'''


in_line = input()
dict = {}

for i in in_line:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1


for item in dict:
    print(f"{item} -> {dict[item]}")