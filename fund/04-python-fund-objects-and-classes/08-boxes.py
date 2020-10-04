'''

Boxes

Create a class Box, which will represent a rectangular box. The Box should have UpperLeft (Point), UpperRight (Point), BottomLeft (Point), BottomRight (Point).
Create, or use from the Lab, the class Point which has X (int) and Y (int) – coordinates in 2D space. Move the CalculateDistance() method in the Point class,
exactly as it is. Then use “Point.CalculateDistance(point1, point2)” signature, to use the method.

Create 2 methods in the Box class:
CalculatePerimeter(width, height)
CalculateArea(width, height).

Make them return integers, representing the perimeter and area of the box.
The formulas are respectively – (2 * Width + 2 * Height) and (Width * Height).
The Width is the distance between the UpperLeft and the UpperRight Points, and ALSO – the Bottomleft and the BottomRight Points.
The Height is the distance between the UpperLeft and the BottomLeft Points, and ALSO – the UpperRight and the BottomRight Points.
You will receive several input lines in the following format:

{X1}:{Y1} | {X2}:{Y2} | {X3}:{Y3} | {X4}:{Y4}

Those will be the coordinates to UpperLeft, UpperRight, BottomLeft and BottomRight (IN THE SAME ORDER).
When you receive the command “end”. You must print all Boxes in the following format:

“Box: {width}, {height}
 Perimeter: {perimeter}
 Area: {area}”

0:2 | 2:2 | 0:0 | 2:0
-3:0 | 0:0 | -3:-3 | 0:-3
-2:2 | 2:2 | -2:-2 | 2:-2
end
'''


class Point:
    def __init__(self, x,y):
        self.x = int(x)
        self.y = int(y)

class Box:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.upper_left = Point(x1, y1)
        self.upper_right = Point(x2, y2)
        self.bottom_left = Point(x3, y3)
        self.bottom_right = Point(x4, y4)
        self.width = abs(self.upper_right.x - self.upper_left.x)
        self.height = abs(self.bottom_right.y - self.upper_right.y)

    def calculate_perimeter(self):
        return (2*self.height + 2*self.width)

    def calculate_area(self):
        return (self.height * self.width)

    def display(self):
        print(f"Box: {self.width}, {self.height}")
        print(f"Perimeter: {self.calculate_perimeter()}")
        print(f"Area: {int(self.calculate_area())}")


in_line = input()
boxes = []
while in_line != "end":
    coord = list(in_line.split(" | "))
    x1,y1 = map(int,coord[0].split(":"))
    x2,y2 = map(int,coord[1].split(":"))
    x3,y3 = map(int,coord[2].split(":"))
    x4,y4 = map(int,coord[3].split(":"))
    boxes.append(Box(x1, y1, x2, y2, x3, y3, x4, y4))
    in_line = input()


for i in boxes:
    i.display()

