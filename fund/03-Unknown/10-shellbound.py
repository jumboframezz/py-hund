'''
Shellbound

Vladi is a crab. Crabs are scared of almost anything, which is why they usually hide in their shells. Vladi is a rich
crab though. He has acquired many outer shells, in different regions, in which he can hide – each with a different size.
However, it is really annoying to look after all your shells when they are so spread out. That is why Vladi decided to
merge all shells in each region, so that he has one big shell for every region. He needs your help to do that.

You will be given several input lines containing a string and an integer, separated by a space. The string will
represent the region’s name, and the integer – the shell in the given region, size.
You must store all shells in their corresponding regions.
If the region already exists, add the new shell to it. Make sure you have NO duplicate shells (shells with same size).
Vladi doesn’t like shells to have the same size.

When you receive the command “Aggregate”, you must stop reading input lines, and you must print every region, all of
the shells in that region, and the size of the giant shell after you’ve merged them in the following format:

{regionName} -> {shell 1, shell 2…, shell n…} ({giantShell})

The giant shell size is calculated when you subtract the average of the shells from the sum of the shells.
Or in other words: (sum of shells) – ((sum of shells) / (count of shells)).

Constraints
All numeric data will be represented with integer variables in range [0…1.000.000.000].

Examples

Input                       Output

Sofia 50                    Sofia -> 50, 20, 30 (67)
Sofia 20                    Varna - 10, 20 (15)
Sofia 30
Varna 10
Varna 20
Aggregate

Sofia 2                     Sofia -> 2, 1 (2)
Sofia 1                     Plovdiv -> 100, 50 (75)
Plovdiv 100
Plovdiv 50
Aggregate

Sofia 50
Sofia 20
Sofia 20
Sofia 30
Varna 10
Varna 20
Aggregate

'''
import math
region_name=""
shell_size=0


regions={}
region_id=0

in_line=input()
while in_line != "Aggregate":
    in_data=in_line.split(" ")
    region_name = in_data[0]
    shell_size = int(in_data[1])

    if not region_name in regions:
        regions[region_name]=[]
    if not regions[region_name].count(shell_size):
        regions[region_name].append(shell_size)
    in_line = input()


for i in regions :
    shell_count = 0
    shell_sum = 0
    giant = 0
    line = ""
    print (f"{i} -> ", end ="")
    for ii in regions[i]:
        if regions[i].count(ii) > 1:
            continue
        line += f"{ii}, "
        shell_count +=1
        shell_sum += int(ii)
    print(line.strip(", "), end="")
    giant = math.ceil ( shell_sum - shell_sum / shell_count)
    print(f" ({giant})")

























