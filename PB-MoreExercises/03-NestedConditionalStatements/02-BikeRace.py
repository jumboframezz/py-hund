# 2. Вело състезание
# Предстои Вело състезание за благотворителност в което участниците са разпределени в младша("juniors") и
# старша("seniors") група. Парите се набавят от таксата за участие на велосипедистите. Според възрастовата група и вида
# на трасето на което ще се провежда състезанието, таксата е различна.
#
# Група	    trail	cross-country	downhill	road
# juniors	 5.50	            8	   12.25	  20
# seniors	    7	         9.50	   13.75   21.50
#
# Ако в "cross-country" състезанието се съберат 50 или повече участника(общо младши и старши), таксата  намалява с 25%.
# Организаторите отделят 5% процента от събраната сума за разходи.
# Вход
# От конзолата се четат 2 числа и един стринг, всяко на отделен ред:
# •	Първият ред – броят младши велосипедисти. Цяло число в интервала [1…100]
# •	Вторият ред – броят старши велосипедисти. Цяло число в интервала [1… 100]
# •	Третият ред – вид трасе – "trail", "cross-country", "downhill" или "road"
# Изход
# Да се отпечата на конзолата едно число:
# "{дарената сума}" - форматирана с точност до 2 знака след десетичната запетая.


junior_cnt = int(input())
senior_cnt = int(input())
track_type = input()
junior_sum = 0
senior_sum = 0

if track_type == "trail":
    junior_sum = junior_cnt * 5.50
    senior_sum = senior_cnt * 7
elif track_type == "cross-country":
    junior_sum = junior_cnt * 8
    senior_sum = senior_cnt * 9.50
elif track_type == "downhill":
    junior_sum = junior_cnt * 12.25
    senior_sum = senior_cnt * 13.75
elif track_type == "road":
    junior_sum = junior_cnt * 20
    senior_sum = senior_cnt * 21.50

total = junior_sum + senior_sum
total -= total * 0.05

if junior_cnt + senior_cnt >= 50 and track_type == "cross-country":
    total -= total * 0.25

print(f"{total:.2f}")
