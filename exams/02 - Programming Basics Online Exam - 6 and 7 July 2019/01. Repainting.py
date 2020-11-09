# . Пребоядисване
# Румен иска да пребоядиса хола, като за целта е наел майстори. Напишете програма, която изчислява
# разходите за ремонта, вземайки предвид следните цени:
#   •   Предпазен найлон - 1.50 лв. за кв.м.
#   •   Боя - 14.50 лв. за литър
#   •   Разредител за боя - 5.00 лв. за литър
# За всеки случай, към необходимите материали, Румен иска да добави още 10% от количеството боя и 2 кв.м.
# найлон, разбира се и 0.40 лв. за торбички, а сумата, която се заплаща на майсторите за 1 час работа, е равна
# на 30% от сбора на всички разходи за материали.
# Вход
# Входът се чете от конзолата и съдържа точно 4 реда:
# 1. Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
# 2. Необходимо количество боя (в литри) - цяло число в интервала [1…100]
# 3. Количество разредител (в литри) - цяло число в интервала [1…30]
# 4. Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]
# Изход
# Да се отпечата на конзолата един ред:
# • "Total expenses: {сумата на всички разходи} lv."
# Резултатът трябва да е форматиран до втората цифра след десетичния знак.

foil_needed = float(input())
paint_needed = float(input())
thinner_needed = int(input())
hours_needed = int(input())

foil_needed += 2
paint_needed *= 1.1
bags = 0.4
foil_sum = float(foil_needed * 1.5)
paint_sum = float(paint_needed * 14.50)
thinner_sum = thinner_needed * 5
materials_price = foil_sum + paint_sum + thinner_sum + bags
workhour_price = materials_price * 0.3
total_sum = materials_price + hours_needed * workhour_price
print(f"Total expenses: {total_sum:.2f} lv.")
