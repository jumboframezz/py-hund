# 2. Почивен или работен ден
# Напишете програма която, чете ден от седмицата (текст), на английски език - въведен от потребителя.Ако денят е работен
# отпечатва на конзолата - "Working day", ако е почивен - "Weekend". Ако се въведе текст различен от ден от седмицата да
# се отпечата - "Error".

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
wday = None

day = input()
if day in days:
    wday = days.index(day)
else:
    print("Error")
    exit(0)

if wday == 5 or wday == 6:
    print("Weekend")
elif wday >= 0 or wday <= 5:
    print("Working day")
