
# You can check your solutions here: https://judge.softuni.bg/Contests/924/.
#
# Sum List Items
#
# Write a program, which reads a list of integers, calculates its sum and prints it.
# The input consists of a number n (the number of items) + n integers, each as a separate line.
#

n = int(input())
arr = []
for i in range(0, n):
    arr.append(int(input()))


print(sum(arr))