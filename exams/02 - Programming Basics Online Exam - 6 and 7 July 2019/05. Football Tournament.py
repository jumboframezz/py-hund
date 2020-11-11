#  5. Футболно състезание
# Задачата ви е да напишете програма, която приема името на отбор и прави статистика за него. През един
# сезон всеки отбор изиграва определен брой футболни срещи, като за всяка среща на отбора се дават точки в
# зависимост от изхода от срещата. Има три възможни изхода от една среща:
# ▪ W - Отборът е победител и получава 3 точки
# ▪ D - Срещата е завършила без победител и отборът получава 1 точка
# ▪ L - Отборът е загубил срещата и не получава точки
# Напишете програма, която приема името на футболен отбор и извежда неговата статистика, на база на
# изиграните срещи през този сезон. Неговата статистика трябва да включва общия брой спечелени точки през
# настоящия сезон, подробна статистика за изхода на изиграните игри и процент победи през сезона. Ако
# отборът по някаква причина не е играл мачове през настоящия сезон се извежда специално съобщение.
# Вход
# От конзолата се четат два реда:
#   •   Името на футболния отбор, за който водим статистика - текст
#   •   Броя изиграни срещи през настоящия сезон - цяло число в интервала [0… 100]
# За всяка изиграна среща се прочита отделен ред:
#           o   Резултатът от изиграната среща в един от горепосочените формати – символ с възможности
#           'W', 'D' и 'L'
# Изход
# В зависимост от това дали отборът е играл мачове през настоящия сезон се извеждат два вида изход.
#   •   Ако отборът не е изиграл нито един мач през настоящия сезон се извежда точно един ред в следния формат:
#           o   "{името на отбора} hasn't played any games during this season."
#   •   Ако отборът е изиграл един мач или повече се извеждат шест реда в следния формат:
#           o   "{името на отбора} has won {брой спечелени точки} points during this season"
#           o   "Total stats:"
#           o   "## W: {брой спечелени игри}"
#           o   "## D: {брой игри, завършили наравно}"
#           o   "## L: {брой загубени игри}"
#           o   "Win rate: {процент спечелени игри}%"
# Процентът спечелени игри трябва да бъде форматиран до втората цифра след десетичния знак.

def percentage(part, whole):
    return 100 * float(part) / float(whole)


team_name = input()
num_matches = int(input())
total_points = 0
total_w = 0
total_d = 0
total_l = 0

if num_matches <= 0:
    print(f"{team_name} hasn't played any games during this season.")
    exit(0)

for match in range(num_matches):
    score = input()
    if score == "W":
        total_w += 1
        total_points += 3
    elif score == "D":
        total_d += 1
        total_points += 1
    elif score == "L":
        total_l += 1

print(f"{team_name} has won {total_points} points during this season.")
print(f"Total stats:")
print(f"## W: {total_w}")
print(f"## D: {total_d}")
print(f"## L: {total_l}")
print(f"Win rate: {percentage(total_w, num_matches):.2f}%")