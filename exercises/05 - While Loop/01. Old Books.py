# 1. Старата библиотека
# •	Ани отива до родния си град след много дълъг период извън страната. Прибирайки се вкъщи, тя вижда старата
# библиотека на баба си и си спомня за любимата си книга. Помогнете на Ани, като напишете програма, в която тя въвежда
# търсената от нея книга (текст). Докато Ани не намери любимата си книга или не провери всички в библиотеката,
# програмата трябва да чете всеки път на нов ред името на всяка следваща книга (текст). Книгите в библиотеката са
# свършили щом получите текст “No More Books”.
#   •	Ако не открие търсената книгата, да се отпечата на два реда:
#       o	"The book you search is not here!"
#       o	"You checked {брой} books."
#   •	Ако открие книгата си, да се отпечата на един ред:
#       o	"You checked {брой} books and found it."
# URL: https://judge.softuni.bg/Contests/Compete/Index/2420#0

book_title = input()
entry = ""
count = 0
found = False
while not entry == "No More Books":
    entry = input()

    if entry == book_title:
        found = True
        break
    count += 1
if found:
    print(f"You checked {count} books and found it.")
else:

    print("The book you search is not here!")
    print(f"You checked {count - 1} books.")
