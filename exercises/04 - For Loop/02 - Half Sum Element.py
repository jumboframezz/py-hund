#
#  Елемент, равен на сумата на останалите
# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя, и проверява дали сред тях съществува
#  число, което е равно на сумата на всички останали. Ако има такъв елемент, печата
#  "Yes", "Sum = "  + неговата стойност;
#  иначе печата "No", "Diff = " + разликата между най-големия елемент и сумата на останалите (по абсолютна стойност).

import sys

max_number = -sys.maxsize
total_sum = 0


n = int(input())
for i in range(n):
    number = int(input())
    if number > max_number:
        max_number = number
    total_sum += number

other_sum = total_sum - max_number

if max_number == other_sum:
    print(f"Yes\nSum = {other_sum}")
else:
    print(f"No\nDiff = {abs(max_number - other_sum)}")
