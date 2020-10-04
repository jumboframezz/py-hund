'''
Rectangle Position

	Write a program to read two rectangles {left, top, width, height} and print whether the first is inside
	the second.
	The input is given as two lines, each holding a rectangle, described by 4 integers:
	left, top, width and height.

Examples

Input               Output              Visualization           Comments

4 -3 6 4            Inside                                      The first rectangle stays inside the second.
2 -3 10 6

2 -3 10 6           Not inside                                  The rectangles intersect, no the first is
4 -5 6 10                                                       not inside the second.

Hints

	Create a class Rectangle holding properties Top, Left, Width and Height.
	Define calculated properties Right and Bottom.
	Define a method is_inside(rectangle). A rectangle r1 is inside another rectangle r2 when:
r1.left ≥ r2.left
r1.right ≤ r2.right
r1.top ≤ r2.top
r1.bottom ≤ r2.bottom
	Create a method to read a Rectangle.
	Combine all methods into a single program.

'''


class Rectangle:
    def __init__(self, line):
        self.left = line[0]
        self.top = line[1]
        self.width = line[2]
        self.height = line[3]
        self.bottom = self.top + self.height
        self.right = self.left + self.width

def is_inside(r1, r2):
    if r1.left >= r2.left and r1.right <= r2.right and r1.top <= r2.top and r1.bottom <= r2.bottom:
        return True
    else:
        return False

data_r1 = list(map(int,input().split(" ")))
data_r2 = list(map(int,input().split(" ")))

r1 = Rectangle(data_r1)
r2 = Rectangle(data_r2)

if is_inside(r1, r2):
    print("Inside")
else:
    print("Not inside")

print(f"r1: left: {r1.left} right: {r1.right}")
print(f"r2: bottom: {r2.bottom} right: {r2.right}")