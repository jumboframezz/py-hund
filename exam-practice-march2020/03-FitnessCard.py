#  Карта за фитнес
# Да се напише програма, която проверява дали първоначално налична сума е достатъчна, за да се заплати
# карта за месечен достъп във фитнес.
# Цената на картата зависи от пола на клиента и спорта, който практикува:
# Пол   Gym     Boxing  Yoga    Zumba   Dances  Pilates
# мъж   $42     $41     $45     $34     $51     $39
# жена  $35     $37     $42     $31     $53     $37
# Всички цени на карти за ученици (възраст под 19 години вкл.) са с 20% намаление.
# Вход
# От конзолата се прочитат 4 реда:
#  Сумата, с която разполагаме - реално число в интервала [10.00…1000.00]
#  Пол - символ ('m' за мъж и 'f' за жена)
#  Възраст - цяло число в интервала [5…105]
#  Спорт - текст (една от възможностите в таблицата)
# Изход
# На конзолата се отпечатва 1 ред:
#  Ако сумата е достатъчна:
# "You purchased a 1 month pass for {sport}."
# където {sport} е въведения тип спорт
#  Ако сумата не е достатъчна трябва да се пресметне колко още пари са необходими, за да се закупи
# карта:
# "You don't have enough money! You need ${money} more."
# където {money} e оставащата сума нужна, за да се закупи картата, форматирана до втория знак след
# десетичната запетая.

card_amount = int(input())
gender = input()
age = int(input())
sport = input()

if sport == "Gym":
    price = 42 if gender == "m" else 35
elif sport == "Boxing":
    price = 41 if gender == "m" else 37
elif sport == "Yoga":
    price = 45 if gender == "m" else 42
elif sport == "Zumba":
    price = 34 if gender == "m" else 31
elif sport == "Dances":
    price = 51 if gender == "m" else 53
elif sport == "Pilates":
    price = 39 if gender == "m" else 37


if age <= 19:
    price -= price * 0.2

debit = card_amount - price
if debit >= 0:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    debit *= -1
    print(f"You don't have enough money! You need ${debit:.2f} more.")