# 6.	Ромбче от звездички
# Напишете програма, която чете цяло положително число n, въведено от потребителя, и печата ромбче от
# звездички с размер n като в примерите по-долу:
# n = 4
#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *
#
# •	Разделете ромба на горна и долна част и ги печатайте с два отделни цикъла.
# •	За горната част завъртете цикъл за row от 1 то n:
#     o	Отпечатайте n-row интервала.
#     o	Отпечатайте “*”.
#     o	Отпечатайте row-1 пъти “ *”.
# •	Долната част отпечатайте аналогично на горната с цикъл от 1 до n-1.

n = 4
n = int(input())
for row in range(1, n+1):
    print(" " * (n-row) + "* " * row)
for row in range(1, n):
    print(" " * row + "* " * (n - row) )