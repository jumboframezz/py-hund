# Задача 3. Боядисване на яйца
# С наближаването на Великденските празници, цех за боядисване на яйца, започва да боядисва различни
# размери яйца, които след това продава на партиди. В таблицата са показани размерите на яйцата,
# различните бои и каква е цената за продажба на една партида яйца, зависеща от размерите и цвета боя.
#                   Червено(Red)        Зелено(Green)   Жълто (Yellow)
# Големи(Large)     16 лв.              12 лв.          9 лв.
# Средни (Medium)   13 лв.              9 лв.           7 лв.
# Малки (Small)     9 лв.               8 лв.           5 лв.
# Напишете програма, която изчислява какви ще са приходите на цеха от продажбите, като знаете размера на
# яйцата и техният цвят. С 35% от крайната цена ще бъдат покрити производствени разходи.
# Вход
# Входът се чете от конзолата и се състои от три реда:
# • Първи ред – размер на яйцата – текст с възможности "Large", "Medium" или "Small"
# • Втори ред – цвят на яйцата – текст с възможности "Red", "Green" или "Yellow"
# • Трети ред – брой партиди – цяло число в интервала [1… 350]
# Изход
# На конзолата трябва да се отпечата един ред:
# "{крайната цена} leva."
# Резултатът да се форматира до втората цифра след десетичния знак

egg_size = input()
egg_color = input()
lot_number = int(input())
egg_price = 0
total = 0.00

if egg_size == "Large":
    if egg_color == "Red":
        egg_price = 16
    elif egg_color == "Green":
        egg_price = 12
    else:
        egg_price = 9
elif egg_size == "Medium":
    if egg_color == "Red":
        egg_price = 13
    elif egg_color == "Green":
        egg_price = 9
    else:
        egg_price = 7
else:
    if egg_color == "Red":
        egg_price = 9
    elif egg_color == "Green":
        egg_price = 8
    else:
        egg_price = 5

total = float(egg_price * lot_number)
total -= total * 0.35
print(f"{total:.2f} leva.")
