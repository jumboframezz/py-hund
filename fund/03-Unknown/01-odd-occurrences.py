# Odd Occurrences
#
# Write a program that extracts from a given sequence of words all elements that present in it odd number of times
# (case-insensitive).
#
# Words are given in a single line, space separated.
# Print the result elements in lowercase, in their order of appearance.
#
# Hints
#
# Use a dictionary (string  int) to count the occurrences of each word (just like in the previous problem).
# Pass through all key-value pairs in the dictionary and append to the results list all keys that have odd value.
#
# Print the results list.


data = input().split(" ")
mydict={}
out_string = ""

for item in data:
    if item.lower() in mydict:
        mydict[item.lower()] += 1
    else:
        mydict[item.lower()] = 1

for i in mydict:
    if mydict[i] & 1 == 1:
        out_string += i + ", "

print(out_string.strip(", "))
