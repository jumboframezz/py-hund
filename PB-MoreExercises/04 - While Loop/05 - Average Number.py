
# Средно аритметично
# Напишете програма, която прочита едно число n, след това прочита n на брой цели числа и принтира средно аритметичното
# на тяхната сума число, форматирано до втората цифра след десетични знак.


nums = int(input())
average_sum = 0
for val in range(0, nums):
    number = int(input())
    average_sum += number

print(f"{average_sum / nums:.2f}")