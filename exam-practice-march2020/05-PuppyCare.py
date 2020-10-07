# Задача 5. Грижи за кученце
# Ани намира кученце, за което ще се грижи, докато се намери някой да го осинови. То изяжда дневно
# определено количество храна. Да се напише програма, която проверява дали количеството храна, което е
# закупено за кученцето, ще е достатъчно докато кученцето бъде осиновено.
# Вход
# От конзолата се прочитат:
# • Закупеното количество храна за кученцето в килограми – цяло число в интервала [1 …100]
# • На всеки следващ ред до получаване на команда Adopted ще получавате колко грама изяжда
# кученцето на всяко хранене - цяло число в интервала [10 …1000]
# Изход
# На конзолата се отпечатва 1 ред:
#  Ако количеството храна е достатъчно да се отпечата:
# "Food is enough! Leftovers: {останала храна} grams."
#  Ако количеството храна не е достатъчно да се отпечата:
# "Food is not enough. You need {нужно количество храна} grams more."
# https://judge.softuni.bg/Contests/Practice/Index/2275?fbclid=IwAR3sPXgKAm96SrHzfHWwI7tBbyOZKbsrnacsyqC2bzUSbpHmVtp9aifFx5w#8

food_amount_kg = int(input())
food_amount_g = food_amount_kg * 1000

portion = input()
while not portion == "Adopted":
    food_amount_g -= int (portion)
    portion = input()

if food_amount_g >= 0:
    print(f"Food is enough! Leftovers: {food_amount_g} grams.")
else:
    missing_g = food_amount_g * -1
    print(f"Food is not enough. You need {missing_g} grams more.")