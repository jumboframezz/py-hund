# Кино
# От кино ви наемат да напишете програма, чрез която да разберете дали на една прожекцията ще се запълни залата и
# колко пари ще се изкарат от нея. Получавате места в залата и на всеки следващ ред до команда "Movie time!", колко
# хора влизат в залата. Цената на един билет е 5 лв. Ако текущия брой хора влезли в залата се дели на 3 без остатък,
# се прави отстъпка 5лв от общата им сметка.
# Ако в залата се опитат да влязат повече хора от колкото места са останали, то се счита че местата са изчерпани и
# програмата трябва да приключи четенето на вход.
# Вход
# От конзолата се четат:
#   •	На първия ред - капацитет на залата - цяло число в интервала [50... 150]
# На всеки следващ ред до команда "Movie time!":
# o	Брой хора влизащи в киното - цяло число в интервала [1… 15]
# Изход
# На конзолата първо да се отпечата един ред:
#   •	При получена команда "Movie time!":
#       "There are {останали места} seats left in the cinema."
#   •	При изчерпване на местата в залата:
# 	    "The cinema is full."
# След това да се отпечата:
# 	"Cinema income - {приходи от залата} lv."

total_people = 0
total_money = 0
hall_capacity = int(input())
entry = input()


while entry != "Movie time!":
    persons = int(entry)
    money = 0
    if total_people + persons > hall_capacity:
        print("The cinema is full.")
        break
    money = persons * 5
    if persons % 3 == 0:
        money -= 5
    total_money += money
    total_people += persons
    entry = input()

if entry == "Movie time!":
    free_seats = hall_capacity - total_people
    print(f"There are {free_seats} seats left in the cinema.")

print(f"Cinema income - {total_money} lv.")
