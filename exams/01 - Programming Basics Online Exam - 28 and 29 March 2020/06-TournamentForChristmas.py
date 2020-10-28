# Задача 6. Коледен турнир
# Напишете програма, която проследява представянето на вашия отбор на благотворителен коледен турнир.
# Всеки ден получавате имена на игри до команда "Finish". Със спечелването на всяка една игра печелите по
# 20лв. за благотворителност. Трябва да изчислите колко пари сте спечелили на края на деня. Ако имате
# повече спечелени игри, отколкото загубени – вие сте победители този ден и увеличавате парите от него с
# 10%. При приключване на турнира ако през повечето дни сте били победители печелите турнира и
# увеличавате всичките спечелени пари с 20%.
# Никога няма да имате равен брой спечелени и загубени игри.
# Вход
# Първоначално от конзолата се прочита броя дни на турнира – цяло число в интервала [1… 20]
# До получаване на командата "Finish" се чете:
# • Спорт – текст
# За всеки спорт се прочита:
# o Резултат – текст с възможности: "win" или "lose"
# Изход
# Накрая се отпечатва един ред:
# • Ако сте спечелили турнира:
#  "You won the tournament! Total raised money: {спечелените пари}"
# • Ако сте загубили на турнира:
# "You lost the tournament! Total raised money: {спечелените пари}"
# Парите да бъдат форматирани до втората цифра след десетичния знак.
# https://judge.softuni.bg/Contests/Practice/Index/2275?fbclid=IwAR3sPXgKAm96SrHzfHWwI7tBbyOZKbsrnacsyqC2bzUSbpHmVtp9aifFx5w#8

num_days = int(input())
wins_total = 0
losses_total = 0
earnings_total = 0

for day in range(1, num_days+1):
    earnings = 0
    losses = 0
    wins = 0

    sport = input()
    while not sport == "Finish":
        result = input()
        if result == "win":
            wins += 1
        else:
            losses += 1
        sport = input()
    earnings = wins * 20
    if wins > losses:
        earnings += (earnings * 0.1)
    losses_total += losses
    wins_total += wins
    earnings_total += earnings

if wins_total > losses_total:
    earnings_total += earnings_total * 0.2
    print(f"You won the tournament! Total raised money: {earnings_total:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {earnings_total:.2f}")
