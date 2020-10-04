'''
losest Two Points
	Write a program to read n points and find the closest two of them.

Input
	The input holds the number of points n and n lines, each holding a point {X and Y coordinate}.

Output
	The output holds the shortest distance and the closest two points.
	If several pairs of points are equally close, print the first of them (from top to bottom).

4
3 4
6 8
2 5
-1 3

'''


import  math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Entry:
    def __init__(self, po1, po2):
        self.x1 = po1.x
        self.y1 = po1.y
        self.x2 = po2.x
        self.y2 = po2.y
        self.side_a = abs (self.x1 - self.x2)
        self.side_b = abs (self.y1 - self.y2)
        self.distance = math.sqrt(self.side_a ** 2 + self.side_b ** 2 )

n = int(input())
points = []
entries = []
for i in range(0, n):
    line = list(map(int, input().split()))
    points.append(Point(x=line[0], y = line[1]))

for i in range(0, n-1):
    for ii in range(i+1, n):
        entries.append(Entry(points[i], points[ii]))

mm = min(entries, key = lambda  e: e.distance)

min_d = mm.distance
print (f"{min_d:.3f}")
cnt = 0
for i in range(0, len(entries)):
    if min_d == entries[i].distance:
        if cnt == 0:
            min_first = entries[i]
        cnt += 1

print(f"({min_first.x1}, {min_first.y1})")
print(f"({min_first.x2}, {min_first.y2})")