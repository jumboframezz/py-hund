# Снимачен ден
# Вие сте режисьор на филма "Програмирането е забавно", като имате определено време за снимки. От вас се иска да
# напишете програма, с която ще разберете дали снимачният ден ще ви стигне да заснемете филма. Снимачният ден
# започва с подготовка на терен, което е 15 процента от времето за снимки! Филмът има определен брой сцени,
# които се заснемат за определено време.
# Вход
# От конзолата се четат 3 реда:
# 1.	Време за снимки – цяло число в диапазона [0… 1440]
# 2.	Брой сцени  – цяло число в диапазона [5… 25]
# 3.	Времетраене на сцена – цяло число в диапазона [20… 90]
# Изход
# На конзолата да се отпечата един ред:
#   •	Ако времето за заснемане на филма ви стигне:
#       "You managed to finish the movie on time! You have {останало време} minutes left!"
#   •	Ако времето НЕ ВИ стигне:
#       "Time is up! To complete the movie you need {нужно време} minutes."
# Останалото време да се закръгли до най-близкото цяло число.

available_time = int(input())
shoot_scenes = int(input())
scene_length = int(input())

preparation = available_time * 0.15
needed_time = shoot_scenes * scene_length + preparation



diff = available_time - needed_time
if diff >= 0:
    left = round(diff)
    print(f"You managed to finish the movie on time! You have {left} minutes left!")
else:
    left = round(abs(diff))
    print(f"Time is up! To complete the movie you need {left} minutes.")
