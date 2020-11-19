"""
Първият ред – броят младши велосипедисти. Цяло число в интервала [1…100]
Вторият ред – броят старши велосипедисти. Цяло число в интервала [1… 100]
Третият ред – вид трасе – "trail", "cross-country", "downhill" или "road"
"""
juniors = int(input())
seniors = int(input())
track = input()

junior_price = 0
senior_price = 0

if track == 'trail':
    junior_price = 5.50
    senior_price = 7
elif track == 'cross-country':
    junior_price = 8
    senior_price = 9.50
elif track == 'downhill':
    junior_price = 12.25
    senior_price = 13.75
elif track == 'road':
    junior_price = 20
    senior_price = 21.5

sum_price = juniors * junior_price + seniors * senior_price

if juniors + seniors >= 50 and track == 'cross-country':
    sum_price *= 0.75

total_sum = sum_price * 0.95

print(f'{total_sum:.2f}')
