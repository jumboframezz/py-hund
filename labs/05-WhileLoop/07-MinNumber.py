# 7.	Най-малко число
# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя, и намира
# най-малкото измежду тях. Въвежда се по едно число на ред.



import sys
min_number = sys.maxsize
in_text = input()

while in_text != "Stop":
    num = int(in_text)
    if num < min_number:
        min_number = num
    in_text = input()

print(min_number)


