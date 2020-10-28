# 12.	Търговски комисионни
# Фирма дава следните комисионни на търговците си според града, в който работят и обема на продажбите:
#               level0          level1              level2                  level3
# Град	        0 ≤ s ≤ 500	    500 < s ≤ 1 000	    1 000 < s ≤ 10 000  	s > 10 000
# Sofia	                  5%	             7%	                    8%	           12%
# Varna	                4.5%	           7.5%	                   10%	           13%
# Plovdiv	            5.5%	             8%	                   12%	          14.5%
#
# Напишете конзолна програма, която чете име на град (текст) и обем на продажби (реално число), въведени от потребителя,
# и изчислява и извежда размера на търговската комисионна според горната таблица. Резултатът да се изведе
# форматиран до 2 цифри след десетичната точка.
# При невалиден град или обем на продажбите (отрицателно число) да се отпечата "error".

def range_level(sales):
    if sales >=0 and sales <= 500:
        return "level0"
    elif sales > 500 and sales <= 1000:
        return "level1"
    elif sales > 1000 and sales <= 10000:
        return "level2"
    elif sales > 10000:
        return "level3"


city = input()
sales_vol = float(input())

commissions = {
    "Sofia": {"level0": 0.05, "level1": 0.07, "level2": 0.08, "level3": 0.12},
    "Varna": {"level0": 0.045, "level1": 0.075, "level2": 0.1, "level3": 0.13},
    "Plovdiv": {"level0": 0.055, "level1": 0.08, "level2": 0.12, "level3": 0.145},
}
if city not in commissions or sales_vol < 0:
    print("error")
    exit(0)

sales_range = range_level(sales_vol)
total = commissions[city][sales_range] * sales_vol
print(f"{total:.2f}")
