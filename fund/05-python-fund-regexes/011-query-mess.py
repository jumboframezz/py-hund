"""
Problem 11. *Query Mess

This problem is originally from the JavaScript Basics Exam (22 November 2014). You may check your solution here.
Ivancho participates in a team project with colleagues at SoftUni.  They have to develop an application, but something
mysterious happened – at the last moment all team members… disappeared!  And guess what? He is left alone to finish
the project.  All that is left to do is to parse the input data and store it in a special way, but Ivancho has no idea
how to do that! Can you help him?

Input
The input comes from the console on a variable number of lines and ends when the keyword "END" is received.
For each row of the input, the query string contains pairs field=value. Within each pair, the field name and value are
separated by an equals sign, '='. The series of pairs are separated by an ampersand, '&'. The question mark is
used as a separator and is not part of the query string. A URL query string may contain another URL as value.
The input data will always be valid and in the format described. There is no need to check it explicitly.

Output
For each input line, print on the console a line containing the processed string as
follows:  key=[value]nextkey=[another  value] … etc.
Multiple whitespace characters should be reduced to one inside value/key names, but there shouldn't be any
whitespaces before/after extracted keys and values. If a key already exists, the value is added with comma and space
after other values of the existing key in the current string.  See the examples below.

Constraints
SPACE is encoded as '+' or "%20". Letters (A-Z and a-z), numbers (0-9), the characters '*', '-', '.', '_' and other
non-special symbols are left as-is.
Allowed working time: 0.2 seconds. Allowed memory: 16 MB.

Examples:
Input                                                   Output
login=student&password=student                      login=[student]password=[student]
END

field=value1&field=value2&field=value3              field=[value1, value2, value3]
http://example.com/over/there?name=ferret           name=[ferret]
END

field=value1&field=value2&field=value3
http://example.com/over/there?name=ferret
END


foo=%20foo&value=+val&foo+=5+%20+203                                          foo=[foo, 5 203]value=[val]
foo=poo%20&value=valley&dog=wow+                                              foo=[poo]value=[valley]dog=[wow]
url=https://softuni.bg/trainings/coursesinstances/details/1070                url=[https://softuni.bg/trainings/coursesinstances/details/1070]
https://softuni.bg/trainings.asp?trainer=nakov&course=oop&course=php          trainer=[nakov]course=[oop, php]

END




foo=%20foo&value=+val&foo+=5+%20+203
foo=poo%20&value=valley&dog=wow+
url=https://softuni.bg/trainings/coursesinstances/details/1070
https://softuni.bg/trainings.asp?trainer=nakov&course=oop&course=php
END


Key-value regex:
(?P<key>\w+)=(?P<value>\w+)&*
"""

import re


class Pair:
    def __init__(self, key, value):
        self.value = []
        self.key = key.strip(" ")
        self.value.append(value.strip(" "))

    def append_val(self, value):
        self.value.append(value.strip(" "))

    def display(self):
        line = ""
        print(f"{self.key}=", end="")
        for i in range(0,len(self.value)):
            line += f"{self.value[i]}, "
        line = line.strip(", ")
        print(f"[{line}]")

def find_key(key, p):
    if (len(p) == 0):
        return -1
    for i in range (0, len(p)):
        if p[i].key == key:
            return i
    return -1



pairs = []
processed_line = ""
keyval_re = r"(?P<key>\w+)=(?P<value>\w+)&*"
in_line = input()
while in_line != "END":
    processed_line = re.sub(r"(?P<space>(%20)+)", " ", in_line)
    processed_line = re.sub(r"\+", " ", processed_line)
    processed_line = re.sub(r" +", " ", processed_line)

    print(f"F: {processed_line}")

    m = re.finditer(keyval_re, processed_line)
    for i in m:
        key = i.group("key")
        value = i.group("value")
        if len(pairs) >= 1:
            key_index = find_key(key, pairs)
        else:
            pairs.append(Pair(key, value))
            continue
        if key_index == -1:
            pairs.append(Pair(key, value))
        else:
            pairs[key_index].append_val(value)
    in_line = input()


for i in pairs:
    i.display()



print(pairs)