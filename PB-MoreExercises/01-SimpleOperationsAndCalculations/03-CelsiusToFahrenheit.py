# Напишете програма, която чете градуси по скалата на Целзий (°C) и ги преобразува до градуси по скалата на
# Фаренхайт (°F). Потърсете в Интернет подходяща формула, с която да извършите изчисленията.
# T(°F) = T(°C) × 1.8 + 32
# Форматирате изхода до втория знак след десетичната запетая.
# URL to check: https://judge.softuni.bg/Contests/Practice/Index/1642#2

c = float(input())
f = c * 1.8 + 32

print(f"{f:.2f}")
