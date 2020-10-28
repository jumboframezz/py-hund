# 1.Ден от седмицата
# Напишете програма, която чете цяло число, въведено от потребителя, и отпечатва ден от седмицата (на английски език),
# в граници [1...7] или отпечатва "Error" в случай, че въведеното число е невалидно.

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day = int(input())
if day >=1 and day <= 7:
    print(days[day-1])
else:
    print("Error")

