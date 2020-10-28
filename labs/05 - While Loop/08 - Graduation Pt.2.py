# 8.	Завършване – част 2
# Напишете програма, която изчислява средната оценка на ученик от цялото му обучение. На първия ред ще получите името
# на ученика, а на всеки следващ ред - неговите годишни оценки. Ученикът преминава в следващия клас, ако годишната му
# оценка е по-голяма или равна на 4.00. Ако ученикът бъде скъсан повече от един път, то той бива изключен и програмата
# приключва, като се отпечатва името на ученика и в кой клас е изключен.
#  При успешно завършване на 12-ти клас да се отпечата :
# "{име на ученика} graduated. Average grade: {средната оценка от цялото обучение}"
# В случай, че ученикът е изключен от училище, да се отпечата:
# "{име на ученика} has been excluded at {класа, в който е бил изключен} grade"
# Стойността трябва да бъде форматирана до втория знак след десетичната запетая.


student_name = input()
student_grade = 0
excluded_times = 0
total_score = 0
while student_grade < 12:
    score = float(input())
    if score >= 4:
        student_grade += 1
    else:
        excluded_times += 1
    if excluded_times >= 2:
        print(f"{student_name} has been excluded at {student_grade+1} grade")
        exit(0)
    total_score += score

average_score = total_score / student_grade
print(f"{student_name} graduated. Average grade: {average_score:.2f}")
