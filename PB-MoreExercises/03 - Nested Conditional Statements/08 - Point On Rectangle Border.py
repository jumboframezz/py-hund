# 8.Точка върху страната на правоъгълник
# Напишете програма, която проверява дали точка {x, y} се намира върху някоя от страните на
# правоъгълник {x1, y1} – {x2, y2}. Входните данни се четат от конзолата и се състоят от 6 реда въведени от
# потребителя: десетичните числа x1, y1, x2, y2, x и y (като се гарантира, че x1 < x2 и y1 < y2). Да се отпечата
# "Border" (точката лежи на някоя от страните) или "Inside / Outside" (в противен случай).
# * Подсказка: използвайте една или няколко условни if проверки с логически операции.
# Точка {x, y} лежи върху някоя от страните на правоъгълник {x1, y1} – {x2, y2},
# ако е изпълнено едно от следните условия:
# •	x съвпада с x1 или x2 и същевременно y е между y1 и y2
# •	y съвпада с y1 или y2 и същевременно x е между x1 и x2
# Можете да проверите горните условия с една по-сложна if-else конструкция или с няколко по-прости
# проверки или с вложени if-else проверки.

def inrange(xr, yr, xr1, yr1, xr2, yr2):
    if (xr == xr1 or xr == xr2) and (yr >= yr1 and yr <= yr2):
        return True
    else:
        return False


def inborder(xr, yr, xr1, yr1, xr2, yr2):
    if inrange(xr, yr, xr1, yr1, xr2, yr2) or inrange(yr, xr, yr1, xr1, yr2, xr2):
        return True
    else:
        return False


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

if inborder(x, y, x1, y1, x2, y2):
    print("Border")
else:
    print("Inside / Outside")
