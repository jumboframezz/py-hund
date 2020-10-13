
# Math Power
#
# Create a function that calculates and returns the value of a number raised to a given power:
# Examples
#
# Input       Output
#
# 2
# 8           256.0
#
# 1.5
# 3           3.375
#
# Hints
# As usual, read the input
# Create a function which will have two parameters - the number and the power, and will return a result
# Print the result with no specific formatting.


def math_power(a, b):
    return a ** b


base = float(input())
power = float(input())

print(math_power(base, power))
