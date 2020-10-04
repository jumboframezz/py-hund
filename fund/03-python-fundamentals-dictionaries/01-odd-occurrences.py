'''
Odd Occurrences

Write a program that extracts from a given sequence of words all elements that present in it odd number of times
(case-insensitive).

Words are given in a single line, space separated.
Print the result elements in lowercase, in their order of appearance.

Examples

Input                                   Output
Java C# PHP PHP JAVA C java             java, c#, c
3 5 5 hi pi HO Hi 5 ho 3 hi pi          5, hi
a a A SQL xx a xx a A a XX c            a, SQL, xx, c

Hints

Use a dictionary (string  int) to count the occurrences of each word (just like in the previous problem).
Pass through all key-value pairs in the dictionary and append to the results list all keys that have odd value.

Print the results list.


'''





data=input().split(" ")
dict={}
out_string=""

for item in data:
   if item.lower() in dict:
       dict[item.lower()] += 1
   else:
       dict[item.lower()] = 1


for i in dict:
        if dict[i] & 1 == 1:
            out_string += i + ", "

print (out_string.strip(", "))