# 2. Система за отчет
# На благотворително събитие плащанията за закупените продукти винаги се редуват: плащане в брой и плащане с карта.
# Установени са следните правила за заплащане:
#     • Ако продуктът надвишава 100лв., за него не може да се плати в брой
#     • Ако продуктът е на цена под 10лв., за него не може да се плати с кредитна карта
# Програмата приключва или след като получим команда "End" или след като средствата бъдат събрани.
# Вход
# От конзолата се четат:
#     • Сумата, която се очаква да бъде събрана от продажбите - цяло число в интервала [1 ... 10000]
# На всеки следващ ред, до получаване на командата "End" или докато не се съберат нужните средства:
# цените на предметите,които ще бъдат закупени - цяло число в интервала [1 ... 500]
# Изход
# На конзолата да се отпечата:
#     • При успешна транзакция: "Product sold!"
#     • При неуспешна транзакция: "Error in transaction!"
#     • Ако сумата на всички закупени продукти надвиши или достигне очакваната сума, програмата трябва да
#     приключи и на конзолата да се изпишат два реда:
#         o "Average CS: {средно плащане в кеш на човек}"
#         o "Average CC: {средно плащане с карта на човек}"
#               Плащанията трябва да бъдат форматирани до втората цифра след десетичния знак.
#     • При получаване на команда "End", да се изпише един ред:
#     o "Failed to collect required money for charity."
#https://judge.softuni.bg/Contests/Practice/Index/1684#1

target_sum = int(input())

sale_counter = 1
cache_sum = 0
cashe_count = 0
card_sum = 0
card_count = 0
total_sales = 0
num_sales = 0
while total_sales <= target_sum:
    if sale_counter % 2 != 0:
        if sale_num > 100:
            print("Error in transaction!")
            continue
        else:
            cache_sum += sale_num
            total_sales += sale_num
            cashe_count += 1
            print("Product sold!")
    else:
        if sale_num < 10
            print("Error in transaction!")
            continue
        else
            car_sum += sale_num
            total_sales += sale_num
            card_count += 1
            print("Product sold!")
    sale_num = int(input())
    if sale_num == "End":
        print("Failed to collect required money for charity.")
        exit(0)

"Average CS: {средно плащане в кеш на човек}"
"Average CC: {средно плащане с карта на човек}"