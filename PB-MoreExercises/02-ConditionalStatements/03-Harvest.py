
# Реколта
# От лозе с площ X квадратни метри се заделя 40% от реколтата за производство на вино. От 1 кв.м лозе се изкарват
# Y килограма грозде. За 1 литър вино са нужни 2,5 кг. грозде. Желаното количество вино за продан е Z литра.
# ￼Напишете програма, която пресмята колко вино може да се произведе и дали това количество е достатъчно. Ако е
# достатъчно, остатъкът се разделя по равно между работниците на лозето.
# Вход
# Входът се чете от конзолата и се състои от точно 4 реда:
# 1ви ред: X кв.м е лозето – цяло число в интервала [10 … 5000]
# 2ри ред: Y грозде за един кв.м – реално число в интервала [0.00 … 10.00]
# 3ти ред: Z нужни литри вино – цяло число в интервала [10 … 600]
# 4ти ред: брой работници – цяло число в интервала [1 … 20]
# Изход
# На конзолата трябва да се отпечата следното:
# Ако произведеното вино е по-малко от нужното:
# “It will be a tough winter! More {недостигащо вино} liters wine needed.”
# Резултатът трябва да е закръглен към по-ниско цяло число
# Ако произведеното вино е повече от нужното:
# “Good harvest this year! Total wine: {общо вино} liters.”
# Резултатът трябва да е закръглен към по-ниско цяло число
# “{Оставащо вино} liters left -> {вино за 1 работник} liters per person.”
# И двата резултата трябва да са закръглени към по-високото цяло число

import math
total_vineyard_area = int(input())
grapes_per_metter = float(input())
lt_vine_needed = int(input())
num_workers = int(input())

vineyard_area = total_vineyard_area * 0.4
total_grapes = vineyard_area * grapes_per_metter
lt_vine = total_grapes / 2.5

if lt_vine < lt_vine_needed:
    # Round down
    diff = math.floor(lt_vine_needed - lt_vine)
    print(f"It will be a tough winter! More {diff} liters wine needed.")
else:
    # Round down
    print(f"Good harvest this year! Total wine: {math.floor(lt_vine)} liters.")
    # Round up
    diff = math.ceil(lt_vine - lt_vine_needed)
    vine_per_person = math.ceil(diff / num_workers)
    print(f"{diff} liters left -> {vine_per_person} liters per person.")
