# 8.	*Стипендии
# Учениците могат да кандидатстват за социална стипендия или за стипендия за отличен успех.
#
# Изискване за социална стипендия - доход на член от семейството по-малък от минималната работна заплата и
# успех над 4.5. Размер на социалната стипендия - 35% от минималната работна заплата.
#
# Изискване за стипендия за отличен успех - успех над 5.5, включително.
# Размер на стипендията за отличен успех - успехът на ученика, умножен по коефициент 25.

# Напишете програма, която при въведени доход, успех и минимална работна заплата, дава информация дали ученик има
# право да получава стипендия, и стойността на стипендията, която е по-висока за него.
# Вход
# Потребителят въвежда 3 числа, по едно на ред:
# 1.	Доход в лева - реално число;
# 2.	Среден успех -  реално числсо;
# 3.	Минимална работна заплата – реално число.
# Изход
# •	Ако ученикът няма право да получава стипендия, се извежда:
# "You cannot get a scholarship!"
# •	Ако ученикът има право да получава само социална стипендия:
# "You get a Social scholarship {стойност на стипендия} BGN"
# •	Ако ученикът има право да получава само стипендия за отличен успех:
# "You get a scholarship for excellent results {стойност на стипендията} BGN"
# •	Ако ученикът има право да получава и двата типа стипендии, ще получи по-голямата по сума, а ако са равни ще получи
# тази за отличен успех.
# Резултатът се закръгля до по-малкото цяло число.

import math
income = float(input())
avg_score = float(input())
avg_salary = float(input())
social_scolarship = 0
excellence_scolarship = 0

if income < avg_salary and avg_score > 4.50:
    social_scolarship = math.floor(avg_salary * 0.35)

if avg_score >= 5.5:
    excellence_scolarship = math.floor(25 * avg_score)

if social_scolarship == 0 and excellence_scolarship == 0:
    print("You cannot get a scholarship!")
elif social_scolarship > 0 and excellence_scolarship == 0:
    print(f"You get a Social scholarship {social_scolarship} BGN")
elif social_scolarship == 0 and excellence_scolarship > 0:
    print(f"You get a scholarship for excellent results {excellence_scolarship} BGN")
elif social_scolarship > excellence_scolarship:
    print(f"You get a Social scholarship {social_scolarship} BGN")
elif excellence_scolarship >= social_scolarship:
    print(f"You get a scholarship for excellent results {excellence_scolarship} BGN")
