# 13.	*Ски почивка
# Атанас решава да прекара отпуската си в Банско и да кара ски. Преди да отиде обаче, трябва да резервира хотел и да
# изчисли колко ще му струва престоят. Съществуват следните видове помещения със следните цени за престой:
#    "room for one person" – 18.00 лв за нощувка
#    "apartment" – 25.00 лв за нощувка
#    "president apartment" – 35.00 лв за нощувка
# Според броят на дните, в които ще остане в хотела (пример: 11 дни = 10 нощувки) и видът на помещението, което ще
# избере, той може да ползва различно намаление. Намаленията са както следва:
#
# вид помещение	        по-малко от 10 дни	        между 10 и 15 дни	        повече от 15 дни
# room for one person	не ползва намаление	        не ползва намаление	        не ползва намаление
# apartment	            30% от крайната цена	    35% от крайната цена	    50% от крайната цена
# president apartment	10% от крайната цена	    15% от крайната цена	    20% от крайната цена
#
# След престоя оценката на Атанас за услугите на хотела може да е позитивна (positive) или негативна (negative) .
# Ако оценката му е позитивна, към цената с вече приспаднатото намаление Атанас добавя 25% от нея. Ако оценката му е
# негативна приспада от цената 10%.
# Вход
# Входът се чете от конзолата и се състои от три реда:
# •	Първи ред - дни за престой - цяло число;
# •	Втори ред - вид помещение - "room for one person", "apartment" или "president apartment";
# •	Трети ред - оценка - "positive"  или "negative".
# Изход
# На конзолата трябва да се отпечата един ред - цената за престоят му в хотела, форматирана до втория
# знак след десетичната запетая.
def get_base_price(accommodation):
    if accommodation == "room for one person":
        return 18.00
    elif accommodation == "apartment":
        return 25.00
    elif accommodation == "president apartment":
        return 35


discounts = {
    "room for one person": [1, 1, 1],
    "apartment": [0.7, 0.65, 0.5],
    "president apartment": [0.9, 0.85, 0.8]
}

days_num = int(input())
room_type = input()
rating = input()
discount = 1
days_num -= 1

if days_num < 10:
    discount = discounts[room_type][0]
elif days_num >= 10 and days_num <= 15:
    discount = discounts[room_type][1]
elif days_num > 15:
    discount = discounts[room_type][2]

price = (get_base_price(room_type) * days_num)
price *= discount

if rating == "positive":
    price += price * 0.25
else:
    price -= price * 0.1

print(f"{price:.2f}")
