# Туристическа агенция
# Туристическа агенция има нужда от система за изчисляване на дължимата сума при резервация. В
# зависимост от различните дестинации и различните пакети, цената е различна.
# Цените за ден са следните:
# Цена за ден
#           Банско/Боровец                          Варна/Бургас
#       с екипировка    без екипировка          със закуска    без закуска
#             100лв.              80лв                130лв.   100лв.
# VIP отстъпка  10%                 5%                  12%              7%
# Ако клиентът е заявил престой повече от 7 дни, получава единия ден безплатно.
# Вход
# От конзолата се четат 4 реда:
# 1. Име на града - текст с възможности ("Bansko", "Borovets", "Varna" или "Burgas")
# 2. Вид на пакета - текст с възможности ("noEquipment", "withEquipment", "noBreakfast" или
# "withBreakfast")
# 3. Притежание на VIP отстъпка - текст с възможности "yes" или "no"
# 4. Дни за престой - цяло число в интервала [1 … 10000]
# Изход
# На конзолата се отпечатва 1 ред:
# • Когато потребителят е въвел всички данни правилно, отпечатваме:
# "The price is {цената, форматирана до втория знак}lv! Have a nice time!"
# • Ако потребителят е въвел по-малко от 1 ден за престой, отпечатваме:
# "Days must be positive number!"
# • Когато при въвеждането на града или вида на пакета се въведат невалидни данни, отпечатваме:
# "Invalid input!"
prices = {"Resort": {"noEquipment": 80, "withEquipment": 100,"noBreakfast": 100, "withBreakfast": 130},
          "VIP": {"noEquipment": 5, "withEquipment": 10,"noBreakfast": 7, "withBreakfast": 12}}

town = input()
stay_type = input()
discount = input()
stay_num = int(input())

stay_list = ["noEquipment", "withEquipment", "noBreakfast", "withBreakfast"]
towns_list = ["Bansko", "Borovets", "Varna", "Burgas"]
if stay_num < 1:
    print("Days must be positive number!")
    exit(0)

if town not in towns_list or stay_type not  in stay_list:
    print("Invalid input!")
    exit(0)

if stay_num > 7:
    stay_num -= 1

price = prices["Resort"][stay_type]
total = price * stay_num
if discount == "yes":
    vip = prices["VIP"][stay_type]
    total -= total * (vip / 100)

print(f"The price is {total:.2f}lv! Have a nice time!")
