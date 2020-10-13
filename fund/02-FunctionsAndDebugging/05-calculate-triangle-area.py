
# Calculate Triangle Area
#
# Create a function that calculates and returns the area of a triangle by given base and height.
# Use a general formatting with 12 digits after the decimal point (e.g. {area:.12g})
#
# Examples
#
# Input       Output
#
# 3
# 4           6


def triangle_area(b, h_triag):
    rez = b * h_triag / 2
    return rez


a = float(input())
h = float(input())

area = triangle_area(a, h)
print(f"{area: .12g}")
