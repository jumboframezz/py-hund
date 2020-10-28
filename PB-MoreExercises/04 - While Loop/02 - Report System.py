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
# https://judge.softuni.bg/Contests/Practice/Index/1684#1

target_sum = int(input())
sale = input()
total = 0
deal_counter = 1
cache_deal_counter = 0
card_deal_counter = 0
cache_deal_amount = 0
card_deal_amount = 0

while total <= target_sum:
    price = int(sale)
    if deal_counter % 2 != 0:
        if price > 100:
            print("Error in transaction!")
            deal_counter += 1
            sale = input()
            continue
        else:
            total += price
            cache_deal_counter += 1
            cache_deal_amount += price
            print("Product sold!")
    else:
        if price < 10:
            print("Error in transaction!")
            deal_counter += 1
            sale = input()
            continue
        else:
            total += price
            card_deal_counter += 1
            card_deal_amount += price
            print("Product sold!")

    if total >= target_sum:
        break
    deal_counter += 1
    sale = input()
    if sale == "End":
        print("Failed to collect required money for charity.")
        exit(0)

print(f"Average CS: {cache_deal_amount / cache_deal_counter:.2f}")
print(f"Average CC: {card_deal_amount / card_deal_counter:.2f}")
