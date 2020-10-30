# 01. Sum List Items
# Write a program, which reads a list of integers, calculates its sum and prints it.
# The input consists of a number n (the number of items) + n integers, each as a separate line.
# URL: https://judge.softuni.bg/Contests/Practice/Index/924#0


n = int(input())
arr = []
arr_sum = 0
for _ in range(n):
    entry = int(input())
    arr.append(entry)

print(sum(arr))
