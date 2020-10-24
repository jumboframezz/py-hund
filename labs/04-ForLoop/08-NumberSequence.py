
# ￼Редица цели числа
# Напишете програма, която чете n на брой цели числа. Принтирайте най-голямото и най-малкото число сред въведените.
import sys
n = int(input())

maxnum = -sys.maxsize
minnum = sys.maxsize

for i in range(0, n):
    num = int(input())
    if num < minnum:
        minnum = num
    if num > maxnum:
        maxnum = num

print(f"Max number: {maxnum}")
print(f"Min number: {minnum}")