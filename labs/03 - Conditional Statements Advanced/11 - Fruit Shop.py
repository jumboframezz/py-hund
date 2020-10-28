# Магазин за плодове през работните дни работи на следните цени:
#
# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	2.50	1.20	0.85	1.45	    2.70	5.50	    3.85
#
# През събота и неделя магазинът работи на по-високи цени:
#
# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	2.70	1.25	0.90	1.60	    3.00	5.60	    4.20
#
# Напишете програма, която чете от конзолата следните три променливи, въведени от потребителя, и пресмята цената
# според цените от таблиците по-горе:
# •	плод  - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
# •	ден от седмицата  - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
# •	количество (реално число).
# Резултатът да се отпечата закръглен с 2 цифри след десетичната точка. При невалиден ден от седмицата или невалидно
# име на плод да се отпечата "error".
def is_weekend(day):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day not in days:
        return "Error"
    elif days.index(day) >= 0 and days.index(day) <= 4:
        return "WorkingDay"
    else:
        return "Weekend"


fruits_prices = {"WorkingDay": {"banana": 2.50, "apple": 1.20, "orange": 0.85, "grapefruit": 1.45, "kiwi": 2.70, "pineapple": 5.50, "grapes": 3.85},
                 "Weekend": {"banana": 2.70, "apple": 1.25, "orange": 0.90, "grapefruit": 1.60, "kiwi": 3.0, "pineapple": 5.60, "grapes": 4.20}}

fruit = input()
dow = input()
amount = float(input())
week_part = is_weekend(dow)

if week_part == "Error" or fruit not in fruits_prices["WorkingDay"]:
    print("error")
    exit(0)

prices = fruits_prices[week_part]
total = prices[fruit] * amount
print(f"{total:.2f}")
