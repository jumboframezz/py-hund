
# Train the Trainers
# Курсът "Train the trainers" е към края си и финалното оценяване наближава. Вашата задача е да помогнете на журито,
# което ще оценява презентациите, като напишете програма, в която да изчислява средната оценка от представянето на
# всяка една презентация от даден студент, а накрая - средния успех от всички тях.
# От конзолата на първият ред се прочита броят на хората в журито n - цяло число.
# След това на отделен ред се прочита името на презентацията – текст.
# За всяка една презентация на нов ред се четат n - на брой оценки - реално число.
# След изчисляване на средната оценка за конкретна презентация, на конзолата се печата:
#  "{името на презентацията} - {средна оценка}."
# След получаване на команда "Finish", на конзолата се печата
# "Student's final assessment is {среден успех от всички презентации}." и програмата приключва.
# Всички оценки трябва да бъдат форматирани до втория знак след десетичната запетая.


jury = int(input())
presentation_name = input()
presentation_score = 0
total_score = 0
total_presentations = 0
while presentation_name != "Finish":
    presentation_score = 0
    for score in range(jury):
        presentation_score += float(input())
        total_presentations += 1
    total_score += presentation_score
    print(f"{presentation_name} - {presentation_score / jury:.2f}.")
    presentation_name = input()
print(f"Student's final assessment is {total_score / total_presentations:.2f}.")
