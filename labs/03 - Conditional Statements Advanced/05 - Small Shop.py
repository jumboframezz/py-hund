# 5.	Квартално магазинче
# Предприемчив българин отваря квартални магазинчета в няколко града и продава на различни цени според града:
#
# град / продукт	coffee	water	beer	sweets	peanuts
# Sofia	            0.50	0.80	1.20	1.45	1.60
# Plovdiv	        0.40	0.70	1.15	1.30	1.50
# Varna	            0.45	0.70	1.10	1.35	1.55
#
# Напишете програма, която чете продукт (текст), град (текст) и количество (десетично число), въведени от потребителя,
# и пресмята и отпечатва колко струва съответното количество от избрания продукт в посочения град.

prices = {"Sofia": {"coffee": 0.50, "water": 0.80, "beer": 1.20, "sweets": 1.45, "peanuts": 1.60},
          "Plovdiv": {"coffee": 0.40, "water": 0.70, "beer": 1.15, "sweets": 1.30, "peanuts": 1.50},
          "Varna": {"coffee": 0.45, "water": 0.70, "beer": 1.10, "sweets": 1.35, "peanuts": 1.55}}

# print(prices["Sofia"]["cofee"])

product = input()
city = input()
amount = float(input())
price = prices[city][product] * amount
print(price)
