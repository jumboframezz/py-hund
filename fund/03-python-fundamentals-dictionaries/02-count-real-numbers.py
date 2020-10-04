'''
Count Real Numbers
Read a list of real numbers and print them in ascending order along with their number of occurrences.

Examples
Input                   Output
8 2.5 2.5 8 2.5         2.5 -> 3 times
                        8 -> 2 times

1.5 5 1.5 3             1.5 -> 2 times
                        3 -> 1 times
                        5 -> 1 times

-2 0.33 0.33 2          -2 -> 1 times
                        0.33 -> 2 times
                        2 -> 1 times

Hints

Use dictionary (key=nums, value=count) named counts.
Pass through each input number num and increase counts[num] (when num exists in the dictionary) or assign counts[num] = 1 (when num does not exist in the dictionary).
Pass through all numbers num in the dictionary (counts.keys()) and print the number num and its count of occurrences counts[num].
'''

def read_float_line():
    input_line=""
    input_line=input()
    striped_line=input_line.strip()

    line = map(float, striped_line.split(" "))
    return list(line)

arr = read_float_line()

data_dict={}

for i in arr:
    if i in data_dict:
        data_dict[i] += 1
    else:
        data_dict[i] = 1

for item in sorted(data_dict.keys()):
    print(f"{item} -> {data_dict[item]} times")
