# Задача 1. Доставка на храна
# Ресторант отваря врати и предлага няколко менюта на преференциални цени:
# • Пилешко меню – 10.35 лв.
# • Меню с риба – 12.40 лв.
# • Вегетарианско меню – 8.15 лв.
# Напишете програма, която изчислява колко ще струва на група хора да си поръчат храна за вкъщи.
# Групата ще си поръча и десерт, чиято цена е равна на 20 процента от общата сметка (без доставката). Цената
# на доставка е 2.50лв и се начислява най-накрая.
# Вход
# От конзолата се четат 3 реда:
# • Брой пилешки менюта – цяло число в интервала [0… 99]
# • Брой менюта с риба - цяло число в интервала [0… 99]
# • Брой вегетариански менюта - цяло число в интервала [0… 99]
# Изход
# Да се отпечата на конзолата един ред: "Total: {цена на поръчката}"
# Сумата да е форматирана до втория знак след десетичната запетая.

num_chicken_menus = int(input())
num_fish_menus = int(input())
num_vegie_menus = int(input())

sum_chicken = num_chicken_menus * 10.35
sum_fish = num_fish_menus * 12.40
sum_vegie = num_vegie_menus * 8.15

sub_total = sum_chicken + sum_fish + sum_vegie
sub_total *= 1.2
sub_total += 2.50

print(f"Total: {sub_total:.2f}")