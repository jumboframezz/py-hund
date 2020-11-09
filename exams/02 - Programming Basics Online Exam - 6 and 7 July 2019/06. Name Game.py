#  Игра на имена
# Иван е измислил нова игра в която да се състезава със своите приятели. Вашата задача е да напишете
# програма за играта. Всеки играч написва името си, след това за всяка една буква от името си написва по едно
# цяло число, ако числото съвпада с ASCII стойността на съответната буква, играчът получава 10 точки, в
# противен случай, получава само 2 точки. Победител е играчът с най-много точки в края на играта. В случай, че
# двама играчи имат равен брой точки, печели този, който втори е достигнал резултата.
# Вход
# До получаване на командата "Stop" се чете по един ред:
# • Име на играча с дължина n - текст
# За всеки играч се четат n на брой реда:
# • число – цяло число в интервала[0…127]
# Изход
# Да се отпечата един ред в следния формат:
# • "The winner is {името на победителя} with {точките на победителя} points!"

import sys
winner_name = ""
winner_points = -sys.maxsize

player_name = input()
while player_name != "Stop":
    player_points = 0
    for index in range(len(player_name)):
        entry = int(input())
        if ord(player_name[index]) == entry:
            player_points += 10
        else:
            player_points += 2
    if player_points >= winner_points:
        winner_name = player_name
        winner_points = player_points
    player_name = input()

print(f"The winner is {winner_name} with {winner_points} points!")
