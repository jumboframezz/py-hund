'''
Exercises

Exercises are fun … Especially when they represent a problem from your exercises.
Implement a class Exercise, which has a topic (string), a course_name (string),
a judge_contest_link (string), and problems (collection of strings).

You will receive several input lines containing information about a single exercise in the following format:
{topic} -> {course_name} -> {judge_contest_link} -> {problem1}, {problem2}. . .

You need to store every exercise in a Collection of Exercises. When you receive the command “go go go”, you end the input sequence.
You must print every exercise, in the following format:

“Exercises: {topic}
 Problems for exercises and homework for the "{course_name}" course @ SoftUni.
 Check your solutions here: {judge_contest_link}

 1. {problem1}
 2. {problem2}
 . . .”

Examples

Input
ObjectsAndSimpleClasses -> ProgrammingFundamentalsExtended -> https://judge.softuni.bg/Contests/439 -> \
Exercises, OptimizedBankingSystem, Animals, Websites, Boxes, BoxIntersection, Messages
go go go

Output
Exercises: ObjectsAndSimpleClasses
Problems for exercises and homework for the "ProgrammingFundamentalsExtended" course @ SoftUni.
Check your solutions here: https://judge.softuni.bg/Contests/439
1. Exercises
2. OptimizedBankingSystem
3. Animals
4. Websites
5. Boxes
6. BoxIntersection
7. Messages

'''


class Exsercise:
    def __init__(self, line):
        fields = list(line.split(" -> "))
        self.topic = fields[0]
        self.course_name = fields[1]
        self.judge_URL = fields[2]
        self.problems = []
        problems = list(fields[3].split(", "))
        for i in problems:
            self.problems.append(i)


    def display(self):
        print(f"Exercises: {self.topic}")
        print(f"Problems for exercises and homework for the \"{self.course_name}\" course @ SoftUni.")
        print(f"Check your solutions here: {self.judge_URL}")
        for cnt in range (0, len(self.problems)):
            print(f"{cnt+1}. {self.problems[cnt]}")


in_line = input()
exercises=[]
while in_line != "go go go":
    exercises.append(Exsercise(in_line))
    in_line = input()


for e in exercises:
    e.display()