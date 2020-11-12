# Сериали
# От телевизионна компания ви наемат да създадете програма, която да изчислява дали за клиентите ще е възможно да си
# закупят желаните сериали. Разполагате с бюджет и брой сериали, които потребителят ще желае да закупи. Всеки сериал
# съответно има заглавие и цена.
# Някои от сериалите имат намаление:
# •	Thrones – 50%
# •	Lucifer – 40%
# •	Protector – 30%
# •	TotalDrama – 20%
# •	Area – 10%
# Вход
# От конзолата се четат:
# •	Бюджет  - реално  число в интервала [10.0… 100.0]
# •	Брой сериали - n - цяло положително число в интервала [1… 10]
# За всеки сериал се четат по два реда:
# o	Име на сериал - текст
# o	Цена за сериал -  реално  число в интервала [1.0… 15.0]
# Изход
# На конзолата да се изпише един ред:
# •	Ако бюджета ви е по-голям или равен на цената на сериалите:
# 	"You bought all the series and left with {останали пари} lv."
# •	Ако бюджета ви е по-малък от цената на сериалите:
# 	"You need {нужни пари} lv. more to buy the series!"
# Резултатът да бъде закръглен до втората цифра след десетичния знак.

discounts = {"Thrones": 0.5, "Lucifer": 0.6, "Protector": 0.7, "TotalDrama": 0.8, "Area": 0.9}

budget = float(input())
show_nums = int(input())
total_price = 0

for _ in range(show_nums):
    show_name = input()
    show_price = float(input())
    if show_name in discounts:
        show_price *= discounts[show_name]
    budget -= show_price

if budget >= 0:
    print(f"You bought all the series and left with {budget:.2f} lv.")
else:
    budget = abs(budget)
    print(f"You need {budget:.2f} lv. more to buy the series!")
