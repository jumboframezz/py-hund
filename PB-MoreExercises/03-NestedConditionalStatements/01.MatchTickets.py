# 1. Билети за мач
# Когато пуснали билетите за Евро2016, група запалянковци решили да си закупят.Билетите имат две
# категории с различни цени:
#
# •  VIP    – 499.99 лева.
# •  Normal – 249.99 лева.
#
# Запалянковците имат определен бюджет, а броят на хората в групата определя какъв процент от бюджета трябва да
# се задели за транспорт:
#
# •	От 1 до 4     – 75% от бюджета.
# •	От 5 до 9     – 60% от бюджета.
# •	От 10 до 24   – 50% от бюджета.
# •	От 25 до 49   – 40% от бюджета.
# •	50 или повече – 25% от бюджета.
#
# Напишете програма, която да пресмята дали с останалите пари от бюджета могат да си купят билети за
# избраната категория. И колко пари ще им останат или ще са им нужни.
# Вход
# Входът се чете от конзолата и съдържа точно 3 реда:
# •	На първия ред е бюджетът – реално число в интервала [1 000.00 ... 1 000 000.00]
# •	На втория ред е категорията – "VIP" или "Normal"
# •	На третия ред е броят на хората в групата – цяло число в интервала [1 ... 200]
# Изход
# Да се отпечата на конзолата един ред:
# •	Ако бюджетът е достатъчен:
# o	"Yes! You have {останалите пари на групата} leva left."
# •	Ако бюджетът НЕ Е достатъчен:
# o	"Not enough money! You need {сумата, която не достига} leva."
# Сумите трябва да са форматирани с точност до два знака след десетичната запетая.
# URL to check: https://judge.softuni.bg/Contests/Practice/Index/1663#0

budget = float(input())
category = input()
num_peoples = int(input())
price = 0
transport = 0
left = 0

if category == "VIP":
    price = 499.99
else:
    price = 249.99

if num_peoples >= 1 and num_peoples <= 4:
    transport = 0.75
elif num_peoples >= 5 and num_peoples <= 9:
    transport = 0.60
elif num_peoples >= 10 and num_peoples <= 24:
    transport = 0.50
elif num_peoples >= 25 and num_peoples <= 49:
    transport = 0.40
elif num_peoples >= 50:
    transport = 0.25

sub_total = num_peoples * price
budget -= budget * transport

left = abs(budget - sub_total)

if budget >= sub_total:
    print(f"Yes! You have {left:.2f} leva left.")
else:
    print(f"Not enough money! You need {left:.2f} leva.")
