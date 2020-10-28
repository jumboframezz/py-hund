#
# Сумиране на секунди
# Трима спортни състезатели финишират за някакъв брой секунди (между 1 и 50). Да се напише програма, която чете
# времената на състезателите в секунди, въведени от потребителя и пресмята сумарното им време във формат
# "минути:секунди". Секундите да се изведат с водеща нула (2  "02", 7  "07", 35  "35").
# URL to check: https://judge.softuni.bg/Contests/Compete/Index/2414#0
# tags: decimal-format time-format

first_time = int(input())
second_time = int(input())
third_time = int(input())

total = first_time + second_time + third_time

time_m = total // 60
time_sec = total % 60

print(f"{time_m}:{time_sec:02d}")

