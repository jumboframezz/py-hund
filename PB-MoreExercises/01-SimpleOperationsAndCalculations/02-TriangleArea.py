
# Лице на триъгълник
# Напишете програма, която чете от конзолата страна и височина на триъгълник и пресмята неговото лице. Използвайте
# формулата за лице на триъгълник: area = a * h / 2. Форматирате изхода до втория знак след десетичната запетая.
# URL to check: https://judge.softuni.bg/Contests/Practice/Index/1642#1

a = float(input())
h = float(input())

area = a * h / 2
print(f"{area:.2f}")