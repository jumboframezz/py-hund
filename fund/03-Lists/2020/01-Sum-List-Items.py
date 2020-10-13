# 01. Sum List Items
# Write a program, which reads a list of integers, calculates its sum and prints it.
# The input consists of a number n (the number of items) + n integers, each as a separate line.


n = int(input())
arr = []
rez = 0
for i in range(0, n):
    arr.append(int(input()))

for i in arr:
    rez += i

print(rez)

