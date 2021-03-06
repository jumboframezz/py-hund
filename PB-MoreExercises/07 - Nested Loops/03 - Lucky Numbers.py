# 3.	Щастливи числа
# Да се напише програма, която прочита едно цяло число N и генерира всички възможни "щастливи" и различни 4-цифрени
# числа(всяка цифра от числото е в интервала [1...9]).
# Числото трябва да отговаря на следните условия:
# Щастливо число е 4-цифрено число, на което сбора от първите две цифри е равен на сбора от последните две.
# Числото N трябва да се дели без остатък от сбора на първите две цифри на "щастливото" число.
# Вход
# Входът се чете от конзолата и се състои от едно цяло число в интервала [2...10000]
# Изход
# На конзолата трябва да се отпечатат всички "щастливи" и различни 4-цифрени числа, разделени с интервал

def is_lucky(dl1, dl2, dl3, dl4, nl):
    if (dl1 + dl2) == (dl3 + dl4) and nl % (dl1+dl2) == 0:
        return True
    return False


n = int(input())
for d1 in range(1, 10):
    for d2 in range(1, 10):
        for d3 in range(1, 10):
            for d4 in range(1, 10):
                if is_lucky(d1, d2, d3, d4, n):
                    print(f"{d1}{d2}{d3}{d4} ", end="")
