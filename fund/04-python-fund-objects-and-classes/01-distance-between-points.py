'''
Check your solutions here:https://judge.softuni.bg/Contests/950.

Distance Between Points

	Write a method to calculate the distance between two points p1 {x1, y1} and p2 {x2, y2}.
	Write a program to read two points (given as two integers) and print the Euclidean distance between them.
'''


import math


class point:
    def __init__(self, x, y):
        self.x=float(x)
        self.y=float(y)


class sides:
    def __init__(self, point_a, point_b):
        self.side_a = abs(point_a.x - point_b.x)
        self.side_b = abs(point_a.y - point_b.y)
        self.side_c = math.sqrt(self.side_a ** 2 + self.side_b ** 2)

p1 = input().split(" ")
p2 = input().split(" ")


point1 = point(p1[0], p1[1])
point2 = point(p2[0], p2[1])

triangle = sides(point1, point2)


print(f"{triangle.side_c:.3f}")