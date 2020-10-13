
# Multiply Evens by Odds
# Create a program that reads an integer number and multiplies the sum of all its even digits by the sum of all
# its odd digits:
#
# Hints
# Create a function with a name describing its purpose. The function should have a single parameter and will
# return value. Also the function will call two other functions.
# Create two other functions each of which will sum either even or odd digits.
# Implement the logic for summing odd digits.
# Do the same for the function that will sum even digits.
# As you test your solution you may notice that it doesn't work for negative numbers. Following the program execution
# line by line, find and fix the bug.


def sum_even(a):
    rez = 0
    for j in a:
        if int(j) % 2 == 0:
            rez += int(j)
    return rez


def sum_odd(a):
    rez = 0
    for j in a:
        if int(j) % 2 != 0:
            rez += int(j)
    return rez


n = input()
if n[0] == "-":
    line = n[1:]
else:
    line = n

result = sum_odd(line) * sum_even(line)
print(result)
