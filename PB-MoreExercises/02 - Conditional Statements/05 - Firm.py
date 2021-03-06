
# Фирма
# Фирма получава заявка за изработването на проект, за който са необходими определен брой часове. Фирмата разполага с
# определен брой дни. През 10% от дните служителите са на обучение и не могат да работят по проекта. Един нормален
# работен ден във фирмата е 8 часа. Всеки служител може да работи по проекта в извънработно време по 2 часа на ден.
# Часовете трябва да са закръглени към по-ниско цяло число (Например –> 6.98 часа се закръглят на 6 часа).
# Напишете програма, която изчислява дали фирмата може да завърши проекта навреме и колко часа не достигат или остават.
# Вход
# Входът се чете от конзолата и съдържа точно 3 реда:
# На първия ред са необходимите часовете – цяло число в интервала [0 ... 200 000]
# На втория ред са дните, с които фирмата разполага – цяло число в интервала [0 ... 20 000]
# На третия ред е броят на служителите, работещи извънредно – цяло число в интервала [0 ... 200]
# Изход
# Да се отпечата на конзолата един ред:
# Ако времето е достатъчно:
# “Yes!{оставащите часове} hours left.”
# Ако  времето НЕ Е достатъчно:
# “Not enough time!{недостигащите часове} hours needed.“
import math

hours_needed = int(input())
days_allowed = int(input())
persons_overtime = int(input())


hours = math.floor((days_allowed * 0.9) * 8)
overtime = persons_overtime * (2 * days_allowed)

total_hours = hours + overtime
if total_hours >= hours_needed:
    diff = total_hours - hours_needed
    print(f"Yes!{diff} hours left.")
else:
    diff = hours_needed - total_hours
    print(f"Not enough time!{diff} hours needed.")
