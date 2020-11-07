# Задача 6. Билети за кино
# Вашата задача е да напишете програма, която да изчислява процента на билетите за всеки тип от
# продадените билети: студентски(student), стандартен(standard) и детски(kid), за всички прожекции. Трябва
# да изчислите и колко процента от залата е запълнена за всяка една прожекция.
# Вход
# Входът е поредица от цели числа и текст:
#   •   На първия ред до получаване на командата "Finish" - име на филма – текст
#   •   На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
#   •   За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаване на
#        командата "End":
#           o     Типа на закупения билет - текст ("student", "standard", "kid")
# Изход
# На конзолата трябва да се печатат следните редове:
#   • След всеки филм да се отпечата, колко процента от кино залата е пълна
#       "{името на филма} - {процент запълненост на залата}% full."
#   • При получаване на командата "Finish" да се отпечатат четири реда:
#       o "Total tickets: {общият брой закупени билети за всички филми}"
#       o "{процент на студентските билети}% student tickets."
#       o "{процент на стандартните билети}% standard tickets."
#       o "{процент на детските билети}% kids tickets."
#


def percentage(part, whole):
    return 100 * float(part) / float(whole)

def check_type(tiket):
    global total_student_tickets
    global total_standard_tickets
    global total_kid_tickets

    if ticket_type == "student":
        total_student_tickets += 1
    elif ticket_type == "standard":
        total_standard_tickets += 1
    elif ticket_type == "kid":
        total_kid_tickets += 1


total_tickets = 0
total_student_tickets = 0
total_standard_tickets = 0
total_kid_tickets = 0
movie = 0
tickets_sold = 1
ticket_type = ""

movie_name = input()


while movie_name != "Finish":
    available_seats = int(input())
    for movie in range(1, available_seats+1):
        ticket_type = input().strip()
        if ticket_type == "End":
            movie -= 1
            break
        check_type(ticket_type)
        tickets_sold += 1

    print(f"{movie_name} - {percentage(movie, available_seats):.2f}% full.")
    movie_name = input()
    tickets_sold = 1

total_tickets = total_student_tickets + total_standard_tickets + total_kid_tickets

print(f"Total tickets: {total_tickets}")
print(f"{percentage(total_student_tickets, total_tickets):.2f}% student tickets.")
print(f"{percentage(total_standard_tickets, total_tickets):.2f}% standard tickets.")
print(f"{percentage(total_kid_tickets, total_tickets):.2f}% kids tickets.")
