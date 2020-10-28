# 2. Подготовка за изпит
# Напишете програма, в която Марин решава задачи от изпити, докато не получи съобщение "Enough" от лектора си.
# При всяка решена задача той получава оценка. Програмата трябва да приключи прочитането на данни при
# команда "Enough" или ако Марин получи определения брой незадоволителни оценки.
# Незадоволителна е всяка оценка, която е по-малка или равна на 4.
# Вход
#   •	На първи ред - брой незадоволителни оценки - цяло число;
#   •	След това многократно се четат по два реда:
#       o	Име на задача – текст;
#       o	Оценка - цяло число в интервала [2…6].
# Изход
#   •	Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
#       o	"Average score: {средна оценка}"
#       o	"Number of problems: {броя на всички задачи}"
#       o	"Last problem: {името на последната задача}"
# •	Ако получи определеният брой незадоволителни оценки:
#       o	"You need a break, {брой незадоволителни оценки} poor grades."
# Средната оценка да бъде форматирана до втория знак след десетичната запетая.

bad_score_limit = int(input())
bad_score_counter = 0
total_score = 0
task_name = ""
last_task_name = ""
task_counter = 0

while bad_score_counter < bad_score_limit:
    last_task_name = task_name
    task_name = input()
    if task_name == "Enough":
        break
    score = int(input())
    total_score += score
    task_counter += 1
    if score <= 4:
        bad_score_counter += 1

if bad_score_counter >= bad_score_limit:
    print(f"You need a break, {bad_score_counter} poor grades.")
else:
    print(f"Average score: {total_score/task_counter:.2f}")
    print(f"Number of problems: {task_counter}")
    print(f"Last problem: {last_task_name}")
