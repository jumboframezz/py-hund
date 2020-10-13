# Multiply a List of Integers
# Write a program to read a list of integers, an integer p, multiply each item by p and print the resulting list.
# URL: https://judge.softuni.bg/Contests/Practice/Index/924#1
# 1 3 12 4

numbers = list(map(int, input().split(" ")))
list_numbers = []
n = int(input())
for item in numbers:
    list_numbers.append(item * n)

for item in list_numbers:
    print(f"{item}", end=" ")
