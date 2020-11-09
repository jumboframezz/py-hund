# 5. Магазин за компютърни игри
# Магазин за компютърни игри ви наема за да направите статистика на процента продажби на игрите от
# последния месец, като изчислите по колко процента от общите продажби са за някоя от игрите.
# Процентите трябва да бъдат разделени на четири части, три заглавия на игри и всички останали :
# • Hearthstone
# • Fornite
# • Overwatch
# • Others
# Вход
# От конзолата се четат:
# • Брой продадени игри- n - цяло положително число в интервала [1… 100]
# За следващите n реда се чете по един ред:
# o Име на игра - текст
# Изход
# На конзолата да се изпишат четири реда:
# "Hearthstone - {процент продажби на Hearthstone}%"
# "Fornite - {процент продажби на Fornite}%"
# "Overwatch - {процент продажби на Overwatch}%"
# "Others - {процент продажби на всички останали игри}%"
# Резултатът да бъде закръглен до втората цифра след десетичния знак.

def percentage(part, whole):
    return 100 * float(part) / float(whole)


top_games = {"Hearthstone": 0, "Fornite": 0, "Overwatch": 0, "Others": 0}

sold_games = int(input())
num_sales = 0
for sale in range(sold_games):
    game_tile = input()
    if game_tile not in top_games.keys():
        game_tile = "Others"
    top_games[game_tile] += 1
    num_sales += 1

for game in top_games.keys():
    print(f"{game} - {percentage(top_games[game], num_sales):.2f}%")
