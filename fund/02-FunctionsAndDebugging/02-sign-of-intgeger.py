
# Sign of Integer Number
#
# Create a function that prints the sign of an integer number n.
#
# Examples
#
# Input   Output
#
# 2       The number 2 is positive.
#
# -5      The number -5 is negative.
#
# 0       The number 0 is zero.


def check_num(a):
    if a == 0:
        return f"The number {a} is zero."
    elif a < 0:
        return f"The number {a} is negative."
    elif a > 0:
        return f"The number {a} is positive."


x = int(input())
print(check_num(x))
