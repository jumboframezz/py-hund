# 1. Съдомиялна
# Гошо работи в ресторант и отговаря за зареждането на съдомиялната накрая на деня.
# Вашата задача е да напишете програма, която изчислява, дали дадено закупено количество бутилки от препарат за
# съдомиялна е достатъчно, за да измие определено количество съдове. Знае се, че
#   всяка бутилка съдържа 750 мл. препарат,
#   за 1 чиния са нужни 5 мл., а
#   за тенджера 15 мл.  Приемете, че на всяко трето зареждане със съдове,
# съдомиялната се пълни само с тенджери, а останалите пъти с чинии. Докато не получите команда "End" ще продължите да
# получавате бройка съдове, които трябва да бъдат измити.
# Вход
# От конзолата се четат:
#   •	Брой бутилки от препарат, който ще бъде използван за миенето на чинии - цяло число в интервала [1…10]
#   •   На всеки следващ ред, до получаване на командата "End" или докато количеството препарат не се изчерпи,
#       брой съдове, които трябва да бъдат измити - цяло число в интервала [1…100]
# Изход
# В случай, че количеството препарат е било достатъчно за измиването на съдовете:
# "Detergent was enough!"
# "{брой чисти чинии} dishes and {брой чисти тенджери} pots were washed."
# "Leftover detergent {количество останал препарат} ml."
# В случай, че количеството препарат не е било достатъчно за измиването на съдовете:
# "Not enough detergent, {количество не достигнал препарат} ml. more necessary!"
# URL to check: https://judge.softuni.bg/Contests/Practice/Index/1684#0

dish_counter = 0
pot_counter = 0
load_counter = 1

bottles = int(input())
detergent = bottles * 750
load = input()
while load != "End":
    num_load = int(load)
    if load_counter % 3 == 0:
        pot_counter += int(load)
        detergent -= num_load * 15
    else:
        dish_counter += num_load
        detergent -= num_load * 5
    if detergent < 0:
        break
    load_counter += 1
    load = input()

if detergent >= 0:
    print("Detergent was enough!")
    print(f"{dish_counter} dishes and {pot_counter} pots were washed.")
    print(f"Leftover detergent {detergent} ml.")
else:
    print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
