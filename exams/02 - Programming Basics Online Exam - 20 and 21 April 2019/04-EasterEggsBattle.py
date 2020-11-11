# Задача 4. Битката на великденските яйца
# На Великден семейството на Деси се събира и тя решава да организира "битка" между великденски яйца.
# Правилата на "битката" са следните:
# • Участват двама играчи
# • Всеки от тях започва с определен брой яйца
# • При получаване на команда "one" -> първият играч печели => яйцата на втория намаляват с едно
# • При получаване на команда "two" -> вторият играч печели => яйцата на първия намаляват с едно
# • Играта приключва, ако някой от играчите остане без яйца или до получаване на команда "End of
# battle"
# Вход
# Първоначално се четат два реда:
# 1. Брой яйца, които има първият играч - цяло число в интервала [1 … 99]
# 2. Брой яйца, които има вторият играч - цяло число в интервала [1 … 99]
# След това до получаване на команда "End of battle" се четe многократно един ред:
# 3. Победител - текст - "one" или "two"
# Изход
# Ако първият играч остане без яйца:
# • "Player one is out of eggs. Player two has {брой останали яйца на втория играч}
# eggs left."
# Ако вторият играч остане без яйца:
# • "Player two is out of eggs. Player one has {брой останали яйца на първия играч}
# eggs left."
# При команда "End of battle" да се отпечатат два реда:
# • "Player one has {брой останали яйца на първия играч} eggs left."
# • "Player two has {брой останали яйца на втория играч} eggs left."
# URL to check: https://judge.softuni.bg/Contests/Practice/Index/1637#6

player1_eggs = int(input())
player2_eggs = int(input())

winner = input()

while not winner == "End of battle":

    if winner == "one":
        player2_eggs -= 1
    if winner == "two":
        player1_eggs -= 1

    if player1_eggs == 0:
        print(f"Player one is out of eggs. Player two has {player2_eggs} eggs left.")
        break
    if player2_eggs == 0:
        print(f"Player two is out of eggs. Player one has {player1_eggs} eggs left.")
        break
    winner = input()

if winner == "End of battle":
    print(f"Player one has {player1_eggs} eggs left.")
    print(f"Player two has {player2_eggs} eggs left.")
