#
# Пирамида от числа
# Напишете програма, която чете цяло число n, въведено от потребителя, и отпечатва пирамида от числа като в примерите:
# вход  изход
# 7     1
#       2 3
#       4 5 6
#       7


n = int(input())
counter = 1
for i in range(n):
    for ii in range(i+1):
        print(f"{counter}", end=" ")
        counter += 1
        if counter > n:
            exit(0)
    print()
