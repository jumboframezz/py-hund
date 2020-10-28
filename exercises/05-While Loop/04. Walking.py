# 4.	Стъпки
# Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000 стъпки всеки ден. Някои
# дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си.

# Напишете програма, която чете от конзолата по колко стъпки изминава тя всеки път като излиза през деня и когато
# постигне целта си да се изписва:
#   "Goal reached! Good job!" и колко стъпки повече е извървяла "{разликата между стъпките} steps over the goal!"

# Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките, които е извървяла
# докато се прибира. След което, ако не е успяла да постигне целта си, на конзолата трябва да се изпише:
#     "{разликата между стъпките} more steps to reach goal."

goal_steps = 10000
steps_for_day = 0
entry = input()

while entry != "Going home":
    steps_for_day += int(entry)
    if steps_for_day >= goal_steps:
        break
    entry = input()

if entry == "Going home":
    steps_for_day += int(input())
    if steps_for_day >= goal_steps:
        print("Goal reached! Good job!")
        print(f"{steps_for_day - goal_steps} steps over the goal!")
    else:
        print(f"{goal_steps - steps_for_day} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{steps_for_day - goal_steps} steps over the goal!")

