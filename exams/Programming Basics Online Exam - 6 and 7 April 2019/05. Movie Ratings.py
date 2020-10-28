# Задача 5. Филмов рейтинг
# Деси много обича да гледа филми, но често й е трудно да си избере подходящ за гледане. Набелязва си
# определен брой филми и иска да си избере кой филм да гледа спрямо рейтинга на филмите.
# Напишете програма, която показва кой филм е с най-висок рейтинг, кой е с най-нисък и колко е средният
# рейтинг от всички филми, които си е набелязала да гледа.
# Вход
# От конзолата първо се чете един ред:
# • Брой филми, които си е набелязала Деси – цяло число в интервала [1…20]
# За всеки филм се прочитат два отделни реда:
# • Име на филма – текст
# • Рейтинг на филма - реално число в интервала [1.00…10.00]
# Изход
# Отпечатват се три реда в следния формат:
# • "{име на филма с най-висок рейтинг} is with highest rating: {рейтинг на филма}"
# • "{име на филма с най-нисък рейтинг} is with lowest rating: {рейтинг на филма}"
# • "Average rating: {средният рейтинг на всички филми}"
# Максималният, минималният и средният рейтинг да се форматира до първата цифра след десетичния знак.

import sys

min_rating = sys.maxsize
max_rating = -sys.maxsize
min_rating_movie = ""
max_rating_movie = ""
average_rating = 0


num_movies = int(input())
for movie in range(num_movies):
    in_movie_name = input()
    in_rating = float(input())
    if in_rating > max_rating:
        max_rating = in_rating
        max_rating_movie = in_movie_name
    if in_rating < min_rating:
        min_rating = in_rating
        min_rating_movie = in_movie_name
    average_rating += in_rating

print(f"{max_rating_movie} is with highest rating: {max_rating}")
print(f"{min_rating_movie} is with lowest rating: {min_rating}")
print(f"Average rating: {average_rating/num_movies:.1f}")

