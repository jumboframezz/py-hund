# Задача 6. Великденска украса
# За великденските празници, магазин започва да продава три вида великденска украса – кошнички за яйца
# (basket), великденски венци (wreath) и шоколадови зайци (chocolate bunny). Вашата задача е да
# напишете програма, която да изчислява каква сметка трябва да плати всеки един клиент на магазина, като
# се има в предвид, че всеки клиент закупил четен брой продукти, ще получи 20% отстъпка от крайната цена.
# След като всички клиенти приключат с покупките, трябва да се отпечата средно по колко пари е похарчил
# всеки човек.
# Цените на продуктите са:
# • кошничка за яйца (basket) – 1.50 лв.
# • великденски венец (wreath) – 3.80 лв.
# • шоколадов заек (chocolate bunny) – 7 лв.
# Вход
# От конзолата първоначално се чете един ред:
# • Брои на клиентите в магазина – цяло число [1… 100]
# • След това за всеки един клиент на нов ред до получаване на командата "Finish" се чете:
# o Покупката която клиента е избрал – текст ("basket", "wreath" или "chocolate bunny")
# Изход
# • При получаване на командата "Finish" да се отпечата един ред:
# o "You purchased {броя на покупките} items for {крайната цена} leva."
# • Накрая, след като всички клиенти приключат с покупките, да се отпечата на един ред
# o "Average bill per client is: {средно аритметично на парите които е
# похарчил всеки един клиент} leva."
# Всички пари трябва да бъдат форматирани до втората цифра след десетичния знак.
# URL to check: https://judge.softuni.bg/Contests/Practice/Index/1637#11


num_clients = int(input())
product = ""
total_sales = 0


for client in range(1, num_clients+1):
    product = input()
    count = 0
    client_bill = 0
    while not product == "Finish":
        if product == "basket":
            client_bill += 1.50
        elif product == "wreath":
            client_bill += 3.80
        elif product == "chocolate bunny":
            client_bill += 7
        count += 1
        product = input()
    if count % 2 == 0:
        client_bill *= 0.8
    print(f"You purchased {count} items for {client_bill:.2f} leva.")
    total_sales += client_bill
average_sales = total_sales / num_clients
print(f"Average bill per client is: {average_sales:.2f} leva.")
