# Задача 6. Великденски конкурс
# С наближаването на Великден, пекарна организира конкурс за направата на най-хубав козунак. Напишете
# програма, която да намира сладкаря с най-висок резултат. В началото на конкурса се въвежда броя на
# козунаците, които ще бъдат дегустирани от посетителите на пекарната, като за всеки козунак различен
# брой посетители, ще дадат оценка от 1 до 10.
# Вход
# Първоначално от конзолата се прочита броя на козунаците – цяло число в интервала [1… 100]
# След това за всеки козунак се прочита:
# • Името на пекаря, който е направил козунака – текст
# • До получаване на командата "Stop" се прочита
# o оценка за козунак от един човек – цяло число в интервала [1... 10]
# Изход
# След получаване на командата "Stop" се печата един ред:
# • "{името на пекаря} has {общият брой получени точки} points."
# Ако след командата "Stop", пекарят е с най-много точки до момента, да се отпечата допълнителен ред:
# • "{името на пекаря} is the new number 1!"
# След дегустация на всички козунаци, да се отпечата един ред:
# • "{името на пекаря с най-много точки} won competition with {точките на пекаря} points!"
# URL to check: https://judge.softuni.bg/Contests/Practice/Index/1637#10


num_bakes = int(input())
chef_name = ""
command = ""
max_score = 0
max_score_name = ""
chef_score = 0

for bake in range(1, num_bakes+1):
    chef_name = input()
    command = input()
    chef_score = 0
    while not command == "Stop":
        if command.isdigit():
            chef_score += int(command)
        command = input()

    print(f"{chef_name} has {chef_score} points.")
    if chef_score > max_score:
        print(f"{chef_name} is the new number 1!")
        max_score_name = chef_name
        max_score = chef_score


print(f"{max_score_name} won competition with {max_score} points!")
