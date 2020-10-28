# 6.	Месечни разходи
# Напишете програма която да пресмята средният разход за месец на семейство за даден период време. За всеки месец
# разходите са следните:
#     • За ток – всеки месец е различен, ще се чете от конзолата
#     • за вода – 20 лв.
#     • за интернет – 15 лв.
#     • за други – събират се тока, водата и интернета за месеца и към сумата се прибавят 20%.
# За всеки разход трябва да се пресметне колко общо е платено за всички месеци.
# Вход
# Входът се чете от конзолата:
#     • Първи ред – месеците за които се търси средният разход – цяло число в интервала [1...100]
#     • За всеки месец – сметката за ток – реално число в интервала [1.00...1000.00]
# Изход
# Да се отпечата на конзолата 5 реда:
#     • 1ви ред: "Electricity: {ток за всички месеци} lv"
#     • 2ри ред: "Water: {вода за всички месеци} lv"
#     • 3ти ред: "Internet: {интернет за всички месеци} lv"
#     • 4ти ред: "Other: {други за всички месеци} lv"
#     • 5ти ред: "Average: {средно всички разходи за месец} lv"
# Всички числа трябва да са форматирана до вторият знак след запетаята.

num_months = int(input())
electricity_sum = 0
electricity_total = 0
water_total = 0
internet_total = 0
other_total = 0
for month in range(0, num_months):
    electricity_sum = float(input())
    electricity_total += electricity_sum
    other_total += (electricity_sum + 20 + 15) * 1.2

water_total = num_months * 20
internet_total = num_months * 15
average = (electricity_total + water_total + internet_total + other_total) / num_months
print(f"Electricity: {electricity_total:.2f} lv")
print(f"Water: {water_total:.2f} lv")
print(f"Internet: {internet_total:.2f} lv")
print(f"Other: {other_total:.2f} lv")
print(f"Average: {average:.2f} lv")
