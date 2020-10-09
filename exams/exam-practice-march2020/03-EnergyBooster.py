# Задача 3. Енергийни гелове
# Сезона за изкачване на алпийски върхове започва и всички алпинисти, се запасяват с енергийни гелове за
# изкачването. Фирма предлага малки и големи разфасовки с по 2 бр. и 5 бр. енергийни гела, като цената на
# един гел зависи от плодовете, от които е направен. В зависимост от размера на разфасовката, цената за
# брой енергиен гел е различна. От конзолата се четат плодовете, размерът на опаковката ((малка) 2 бр. или
# (голяма) 5 бр.), както и колко разфасовки са поръчани. Да се напише програма, която изчислява сумата,
# която трябва да се плати за поръчката.
#                Диня           Манго          Ананас         Малина
# 2 броя (small) 56.00 лв./бр.  36.66 лв./бр.  42.10 лв./бр.  20 лв./бр.
# 5 броя (big)   28.70 лв./бр.  19.60 лв./бр.  24.80 лв./бр.  15.20 лв./бр.
# При поръчки:
# • от 400 лв. до 1000 лв. включително има 15% отстъпка
# • над 1000 лв. има 50% отстъпка
# Вход
# От конзолата се четат 3 реда:
# 1. Плод - текст с възможности: "Watermelon", "Mango", "Pineapple" или "Raspberry"
# 2. Размерът на сета - текст с възможности: "small" или "big"
# 3. Брой на поръчаните сетове - цяло число в интервала [1 … 10000]
# Изход
# На конзолата се отпечатва 1 ред:
# • Цената, която трябва да се заплати, форматирана до втория знак след десетичната запетая,
# в следния формат:
# "{цената} lv."

# Цената на голям пакет гелове с диня е 5 * 28.70 = 143.50 лв.
# Цената на 4 сета: 574 лв.
# 400 <= 574 <= 1000 -> клиентът получава 15% отстъпка
# 15 % от 574 = 86.1 лв. отстъпка
# Крайна цена: 574 - 86.1 = 487.9 лв.

price = 0
total = 0

booster_type = input()
booster_size = input()
booster_qty = int(input())


if booster_type == "Watermelon":
    price = 56 if booster_size == "small" else 28.70

if booster_type == "Mango":
    price = 36.66 if booster_size == "small" else 19.60

if booster_type == "Pineapple":
    price = 42.10 if booster_size == "small" else 24.80

if booster_type == "Raspberry":
    price = 20.00 if booster_size == "small" else 15.20

price *= 2 if booster_size == "small" else 5

sub_total = price * booster_qty

if sub_total >= 400 and sub_total <= 1000:
    total = sub_total - (sub_total * 0.15)
elif sub_total > 1000:
    total = sub_total - (sub_total * 0.5)
elif sub_total < 400:
    total = sub_total

print(f"{total:.2f} lv.")