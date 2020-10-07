# Задача 4. Трекинг мания
# Катерачи от цяла България се събират на групи и набелязват следващите върхове за изкачване. Според размера
# на групата, катерачите ще изкачват различни върхове.
#  Група до 5 човека– Мусала
#  Група от 6 до 12 – Монблан
#  Група от 13 до 25 – Килиманджаро
#  Група от 26 до 40 – К2
#  Група от 41 или повече – Еверест
# Да се напише програма, която изчислява процента на катерачите изкачващи всеки връх.
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
#  На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]
#  За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]
# Изход
# Да се отпечатат на конзолата 5 реда, всеки от които съдържа процент между 0.00% и 100.00% с точност до
# втората цифра след десетичната запетая.
#  Първи ред - процентът изкачващи Мусала
#  Втори ред – процентът изкачващи Монблан
#  Трети ред – процентът изкачващи Килиманджаро
#  Четвърти ред – процентът изкачващи К2
#  Пети ред – процентът изкачващи Еверест
# https://judge.softuni.bg/Contests/Practice/Index/2275?fbclid=IwAR3sPXgKAm96SrHzfHWwI7tBbyOZKbsrnacsyqC2bzUSbpHmVtp9aifFx5w#7

num_groups = int(input())
mussala = 0
montblan = 0
killimanjaro = 0
k2 = 0
everest = 0
total_people = 0

for group in range (1, num_groups+1):
    num_people = int(input())
    if num_people <= 5:
        mussala += num_people
    elif num_people >= 6 and num_people <= 12:
        montblan += num_people
    elif num_people >= 13 and num_people <= 25:
        killimanjaro += num_people
    elif num_people >= 26 and num_people <= 40:
        k2 += num_people
    elif num_people >= 41:
        everest += num_people
    total_people += num_people

mussala_p = mussala / total_people * 100
montblan_p = montblan / total_people * 100
killimanjaro_p = killimanjaro / total_people * 100
k2_p = k2 / total_people * 100
everest_p = everest / total_people * 100


print(f"{mussala_p:.2f}%")
print(f"{montblan_p:.2f}%")
print(f"{killimanjaro_p:.2f}%")
print(f"{k2_p:.2f}%")
print(f"{everest_p:.2f}%")
