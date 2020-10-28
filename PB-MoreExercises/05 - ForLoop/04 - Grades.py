
# Оценки
# Напишете програма, която да пресмята статистика на оценки от изпит. В началото програмата получава броят на
# студентите явили се на изпита и за всеки студент неговата оценка. На края програмата трябва да изпечата процента
# на студенти с оценка между 2.00 и 2.99, между 3.00 и 3.99, между 4.00 и 4.99, 5.00 или повече. Също така и
# средният успех на изпита.
# ￼Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# На първия ред – броя на студентите явили се на изпит – цяло число в интервала [1...1000]
# За всеки един студент на отделен ред – оценката от изпита – реално число в интервала [2.00...6.00]
# Изход
# Да се отпечатат на конзолата 5 реда, които съдържат следната информация:
# "Top students: {процент студенти с успех 5.00 или повече}%"
# "Between 4.00 and 4.99: {между 4.00 и 4.99 включително}%"
# "Between 3.00 and 3.99: {между 3.00 и 3.99 включително}%"
# "Fail: {по-малко от 3.00}%"
# "Average: {среден успех}"
# Всички числа трябва да са форматирани до вторият знак след десетичната запетая.
# Expected output OK, need to check in judge

def percentage(part, whole):
    return 100 * float(part) / float(whole)


average_grade = 0
grade_5 = 0
grade_4 = 0
grade_3 = 0
grade_2 = 0
grade_total = 0

num_students = int(input())
for cnt in range(0, num_students):
    grade = float(input())
    if grade >= 5:
        grade_5 += 1
    elif 4 <= grade <= 4.99:
        grade_4 += 1
    elif 3 <= grade <= 3.99:
        grade_3 += 1
    elif grade < 3:
        grade_2 += 1
    grade_total += grade

print(f"Top students: {percentage(grade_5, num_students):.2f}%")
print(f"Between 4.00 and 4.99: {percentage(grade_4, num_students):.2f}%")
print(f"Between 3.00 and 3.99: {percentage(grade_3, num_students):.2f}%")
print(f"Fail: {percentage(grade_2, num_students):.2f}%")
print(f"Average: {grade_total / num_students:.2f}")
