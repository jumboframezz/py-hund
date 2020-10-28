# 6. Най-голямо число
# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя, и намира
# най-голямото измежду тях. Въвежда се по едно число на ред.

import sys
max_number = -sys.maxsize
in_text = input()

while in_text != "Stop":
    num = int(in_text)
    if num > max_number:
        max_number = num
    in_text = input()

print(max_number)


