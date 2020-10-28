# 5.	Квадратна рамка
# Напишете програма, която чете цяло положително число n, въведено от потребителя, и чертае на
# конзолата квадратна рамка с размер n * n като в примерите по-долу:
# n = 4:
# + - - +
# | - - |
# | - - |
# + - - +

n = int(input())

print("+", end=" ")
for i in range(1, n-1):
    print("-", end=" ")
print("+")

for i in range(1, n-1):
    print("|", end=" ")
    for ii in range(1, n-1):
        print("-", end=" ")
    print("|")

print("+", end=" ")
for i in range(1, n-1):
    print("-", end=" ")
print("+")
