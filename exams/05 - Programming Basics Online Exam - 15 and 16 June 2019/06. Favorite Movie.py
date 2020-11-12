# Любим филм
# Петък вечер е и се чудите кой филм да си пуснете да гледате. Решавате да напишете програма, която да избере това
# вместо вас. До команда "STOP" получавате заглавия на любими ваши филми. Най-добрият филм за вас ще бъде този, който
# има най-много точки. Точките се изчисляват като сбор от ASCII стойностите на символите в заглавието на филма.
# (няма да има случай, в който имаме два филма с равен брой точки)
# При изчислението на точките трябва да се има предвид следното:
#   •	За всяка малка буква в заглавието, от сумата трябва да се извади два пъти дължината на заглавието на филма.
#   •	За всяка главна буква в заглавието, от сумата трябва да се извади дължината на заглавието на филма.
# Може да имате максимум 7 заглавия на филми.
# Вход
# От конзолата се четат редове до команда "STOP" или до достигането на лимита от 7 филма:
#   •	Заглавие на филм  – текст;
# Изход
# На конзолата да се отпечата:
#   •	Ако сте достигнали лимита от 7 филма трябва да отпечатате:
#       "The limit is reached."
# Да се отпечата най-добрият филм за вас:
# "     The best movie for you is {заглавие на филм} with {сума на символите} ASCII sum."
import sys


def sum_movie(mov):
    msum = 0
    for _ in range(len(mov)):
        if _ != " ":
            msum += ord(mov[_])
    return msum


best_movie = ""
best_movie_sum = -sys.maxsize

movie_count = 0
movie = input()

while movie != "STOP":
    movie_sum = sum_movie(movie)
    for letter in movie:
        if letter.isupper():
            movie_sum -= len(movie)
        elif letter.islower():
            movie_sum -= len(movie) * 2
    if movie_sum > best_movie_sum:
        best_movie = movie
        best_movie_sum = movie_sum
    movie_count += 1
    if movie_count == 7:
        print("The limit is reached.")
        break
    movie = input()

print(f"The best movie for you is {best_movie} with {best_movie_sum} ASCII sum.")
