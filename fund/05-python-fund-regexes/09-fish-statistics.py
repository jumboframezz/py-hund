'''
Problem 09. Fish Statistics

You are a marine biologist tasked with researching various types of fish. You will receive a single line on the
console as input. From this line, you must extract all the fish you find and print statistics about each one.
Fish are categorized by three criteria: tail length, body length and status. A standard fish looks like this:

><(((('>


This fish has a tail length of 1, a body length of 4 and has the status "Awake", since its eye is open.
One ASCII character represents 2 centimeters in real life. By those standards, this fish has a tail length of 2 cm
and a body length of 8 cm. There are various types of tails, bodies and statuses, which are described below:

Tail types:

Tail longer than 5 "<" characters  Long
Tail longer than 1 "<" characters  Medium
Tail, which is 1 "<" character long  Short
Nonexistent tail  None

Body types:
Body longer than 10 "(" characters  Long
Body longer than 5 "(" characters  Medium
Any other length  Short

Statuses:

'  Awake
-  Asleep
x  Dead

The input will contain a variable amount of fish, separated by any sequence of ASCII characters. There's a
possibility you might receive input, which has no fish – in this case, just print "No fish found.", and end the program.

Examples
Input                                                           Output:
><(((('> >>>><((((((((('>~~~~~<((->~~~  o o >>>><((x>           Fish 1: ><(((('>
                                                                    Tail type: Short (2 cm)
                                                                    Body type: Short (8 cm)
                                                                    Status: Awake

                                                                Fish 2: >>>><((((((((('>
                                                                    Tail type: Medium (8 cm)
                                                                    Body type: Medium (18 cm)
                                                                    Status: Awake

                                                                Fish 3: <((->
                                                                    Tail type: None
                                                                    Body type: Short (4 cm)
                                                                    Status: Asleep

                                                                Fish 4: >>>><((x>
                                                                    Tail type: Medium (8 cm)
                                                                    Body type: Short (4 cm)
                                                                    Status: Dead

'''
import re

class Fish:
    def get_tail_len(self):
        if self.tail == 0:
            r_tail_len = "None"
        elif self.tail == 1:
            r_tail_len = "Short"
        elif self.tail >= 2 and self.tail < 5:
            r_tail_len = "Medium"
        else:
            r_tail_len = "Long"

        return (r_tail_len)

    def get_body_len(self):
        if self.body >= 10:
                return "Long"
        elif self.body <= 9 and self.body >= 5:
                return "Medium"
        else:
                return "Short"

    def get_status(self):
        if self.status == "'":
                return "Awake"
        elif self.status == "-":
                return "Asleep"
        else:
                return "Dead"

    def __init__(self, tail, body, status):
        self.tail = len(tail)
        self.body = len(body) - 1
        self.status = status
        self.tail_len=""
        self.body_len=""
        self.tail_status=""
        self.tail_len = self.get_tail_len()
        self.body_len = self.get_body_len()
        self.status_name = self.get_status()
        self.fish_icon = f"{tail}{body}{status}>"


pattern=r"(?P<tail>\>*)?(?P<body>\<\(+)(?P<status>[\'\-x])\>"
in_line=input()
fishtank = []

matches = re.finditer(pattern, in_line)
for m in matches:
    #m = re.finditer(pattern, in_line)
    if m.group("tail") == None:
        tail = ""
    else:
        tail = m.group("tail")
    fishtank.append(Fish(tail, m.group("body") , m.group("status")))

if len(fishtank) == 0:
    print("No fish found.")
    exit(0)

cnt = 1
for i in fishtank:
    print(f"Fish {cnt}: {i.fish_icon}")
    if i.tail >= 1:
        print(f"  Tail type: {i.tail_len} ({i.tail*2} cm)")
    else:
        print(f"  Tail type: None")
    print(f"  Body type: {i.body_len} ({i.body*2} cm)")
    print(f"  Status: {i.status_name}")
    cnt +=1

