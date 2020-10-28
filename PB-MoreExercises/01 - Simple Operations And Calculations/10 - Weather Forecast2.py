#
# Прогноза за времето – част 2
# Напишете програма, която при въведени градуси (реално число) принтира какво е времето, като имате предвид
# следната таблица:
#
# Градуси             Време
# 26.00 - 35.00       Hot
# 20.1 - 25.9         Warm
# 15.00 - 20.00       Mild
# 12.00 - 14.9        Cool
# 5.00 - 11.9         Cold
# Ако се въведат градуси, различни от посочените в таблицата, да се отпечата "unknown".

weather = "unknown"
t = float(input())

if t >= 26 and t <= 35:
    weather = "Hot"
elif t >= 20.1 and t <= 25.9:
    weather = "Warm"
elif t >= 15 and t <= 20:
    weather = "Mild"
elif t >= 12 and t <= 14.9:
    weather = "Cool"
elif t >= 5 and t <= 11.9:
    weather = "Cold"
print(f"{weather}")
