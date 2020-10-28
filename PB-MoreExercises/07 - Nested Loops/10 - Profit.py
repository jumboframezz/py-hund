# 10.	Банкноти и монети
# Имаме банкноти и монети по 1лв., по 2лв. и по 5лв. Да се напише програма, която прочита въведените от потребителя
# брой банкноти и монети и сума, и извежда на екран всички възможни начини по които сумата може да се изплати с
# наличните банкноти.
# Вход
# Входът се чете от конзолата и съдържа точно 4 реда:
# 1.	Брой монети по 1лв. - цяло положително число;
# 2.	Брой монети по 2лв. - цяло положително число;
# 3.	Брой банкноти по 5лв. - цяло положително число;
# 4.	Сума - цяло положително число в интервала [1…1000];
# Изход
# Да се отпечатат на конзолата всички комбинации от дадените номинали, образуващи сумата, форматирани по следния начин:
# o	"{бр. 1лв.} * 1 lv. + {бр. 2лв.} * 2 lv. + {бр. 5лв.} * 5 lv. = {сума} lv."

lv1 = int(input())
lv2 = int(input())
lv5 = int(input())
target_sum = int(input())

lv1 += 1
lv2 += 1
lv5 += 1

for i in range(lv1):
    for ii in range(lv2):
        for iii in range(lv5):
            if i + ii * 2 + iii * 5 == target_sum:
                print(f"{i} * 1 lv. + {ii} * 2 lv. + {iii} * 5 lv. = {target_sum} lv.")