# Клуб
# Времето се затопля и клубовете пускат обещаващи промоции. Напише програма, която да изчислява
# приходите на един клуб за вечерта и дали е достигната желаната печалба, като знаете следните условия:
# цената на един коктейл е дължината неговото име. Ако цената на една поръчка е нечетно число, има 25%
# отстъпка от цената на поръчката.
# Вход
# От конзолата се четат:
# • На първия ред – желаната печалба на клуба - реално число в интервала [1.00... 15000.00]
# Поредица от два реда до получаване на командата "Party!" или до достигане на желаната печалба:
# o Име на коктейла – текст
# o Брой на коктейлите за поръчката – цяло число в интервала [1… 50]
# Изход
# На конзолата първо да се отпечата един ред:
# • При получена команда "Party!":
# "We need {недостигаща сума} leva more."
# • При достигане на желаната печалба:
# "Target acquired."
# След това да се отпечата:
# "Club income - {приходи от клуба} leva."
# Парите да бъдат форматирани до втората цифра след десетичния знак.

def is_even(n):
    if n % 2 == 0:
        return True
    return False


total = 0
goal = float(input())

cocktail_name = input()

while cocktail_name != "Party!":
    cocktail_num = int(input())
    cocktail_price = len(cocktail_name)
    sub_total = cocktail_num * cocktail_price
    if not is_even(sub_total):
        sub_total *= 0.75
    total += sub_total
    if total >= goal:
        break
    cocktail_name = input()

if total >= goal:
    print("Target acquired.")
else:
    print(f"We need {abs(goal - total):.2f} leva more.")
print(f"Club income - {total:.2f} leva.")
