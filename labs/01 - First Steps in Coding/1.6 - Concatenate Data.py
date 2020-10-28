# Изготвяне на проекти
# Напишете програма, която изчислява колко часове ще са необходими на един архитект,
# за да изготви проектите на няколко строителни обекта. Изготвянето на един проект отнема три часа.
#
# Вход
# От конзолата се четат 2 реда:
# Името на архитекта - текст;
# Брой на проектите - цяло число.
#
# Изход
# На конзолата се отпечатва:
# "The architect {името на архитекта} will need {необходими часове} hours to complete {брой на проектите} project/s."
#
# Примерен вход и изход
# вход
# George
# 4
#
# изход
# The architect George will need 12 hours to complete 4 project/s.

arch_name = input()
num_projects = int(input())

total_hours = str(num_projects * 3)

print("The architect "+arch_name+ " will need " + total_hours + " hours to complete " + str(num_projects) + " projects/s.")
