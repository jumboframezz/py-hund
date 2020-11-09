#  Най-силната дума
# За Лора думите притежават голяма сила. Тя те моли да измислиш алгоритъм, с който да откриеш коя е "найсилната" дума.
#  До получаване на команда "End of words" ще се четат от конзолата думи. За да се открие
# силата на всяка една, трябва да се намери сборът от ASCII стойностите на символите, от които се състои
# думата. Ако започва с гласна буква - 'a', 'e', 'i', 'o', 'u', 'y' (или техните еквивалентни главни букви),
# полученият сбор трябва да се умножи по дължината на думата, в противен случай, да се раздели на
# дължината и да се закръгли до най-близкото цяло число надолу.
# Вход
# До получаване на команда "End of words" се чете по един ред от конзолата:
# • дума – текст
# Изход
# След приключване на програмата се печата на един ред думата с "най-голяма сила":
# • "The most powerful word is {думата с най-голяма сила} - {силата на думата}"
import sys
import math


vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
winner_word = ""
winner_sum = -sys.maxsize

word = input()
while word != "End of words":
    word_sum = 0
    for _ in word:
        word_sum += ord(_)
    if word[0] in vowels:
        word_sum *= len(word)
    else:
        word_sum = math.floor(word_sum / len(word))
    if word_sum > winner_sum:
        winner_word = word
        winner_sum = word_sum
    word = input()

print(f"The most powerful word is {winner_word} - {winner_sum}")
