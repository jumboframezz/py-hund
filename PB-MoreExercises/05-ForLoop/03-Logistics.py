
# Логистика
# Отговаряте за логистиката на различни товари. В зависимост от теглото на товара е нужно различно превозно средство.
# Цената на тон, за която се превозва товара е различна за всяко превозно средство:
# До 3 тона – микробус (200 лева на тон)
# От 4 до 11 тона – камион (175 лева на тон)
# 12 и повече тона – влак (120 лева на тон)
# Вашата задача е да изчислите средната цена на тон превозен товар, както и процента на тоновете  превозвани с всяко
# превозно средство, спрямо общото тегло(в тонове) на всички товари.
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# На първия ред – броя на товарите за превоз – цяло число в интервала [1...1000]
# За всеки един товар на отделен ред – тонажа на товара – цяло число в интервала [1...1000]
# Изход
# Да се отпечатат на конзолата 4 реда, както следва:
# Първи ред – средната цена на тон превозен товар (закръглена до втория знак след дес. запетая);
# Втори ред – процентът тона превозвани с микробус (процент между 0.00% и 100.00%);
# Трети ред – процентът  тона превозвани с камион (процент между 0.00% и 100.00%);
# Четвърти ред – процентът тона превозвани с влак (процент между 0.00% и 100.00%).


def percentage(part, whole):
    return 100 * float(part) / float(whole)


cargo_num = int(input())
total_weight = 0
bus_sum = 0
truck_sum = 0
train_sum = 0
bus_weight = 0
truck_weight = 0
train_weight = 0
total_sum = 0


for cargo in range(0, cargo_num):
    cargo_weight = int(input())
    if cargo_weight <= 3:
        bus_weight += cargo_weight
    elif cargo_weight >= 4 and cargo_weight <= 11:  # 4 >= cargo_weight <= 11
        truck_weight += cargo_weight
    elif cargo_weight >= 12:
        train_weight += cargo_weight
    total_weight += cargo_weight

bus_sum = bus_weight * 200
truck_sum = truck_weight * 175
train_sum = train_weight * 120

total_sum = bus_sum + truck_sum + train_sum
print(f"{total_sum/total_weight:.2f}")
print(f"{percentage(bus_weight, total_weight):.2f}%")
print(f"{percentage(truck_weight, total_weight):.2f}%")
print(f"{percentage(train_weight, total_weight):.2f}%")
