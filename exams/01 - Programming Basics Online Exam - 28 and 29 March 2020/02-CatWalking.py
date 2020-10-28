# 2. Котешка разходка
# Деси трябва да разхожда своята котка ежедневно, но не може да прецени колко минути са досатъчни на
# ден. Като знаете колко калории приема котката на ден, колко пъти и по колко минути Деси разхожда котката
# си, напишете програма, която изчислява дали разходката е достатъчна. За всяка минута от разходката,
# котката гори по 5 калории. Разходката е достатъчна, ако котката изграря 50% от приетите калории.
# Вход
# Входът се чете от конзолата и съдържа точно 3 реда:
# • На първия ред - минути разходка на ден - цяло число в интервала [1...50]
# • На втория ред - броят на разходките дневно - цяло число в интервала [1…10]
# • На третия ред - приетите от котката калории на ден – цяло число в интервала [100…4000]
# Изход
# Да се отпечата на конзолата един ред:
# • Ако изгорените калории през разходката са повече или равни на 50% от приетите през деня калории:
# "Yes, the walk for your cat is enough. Burned calories per day: {общо изгорени
# калории от разходката}."
# • Ако изгорените калории през разходката са по-малко от 50% от приетите през деня калории:
# "No, the walk for your cat is not enough. Burned calories per day: {общо
# изгорени калории от разходката}."

walking_duration = int(input())
walking_times = int(input())
calories_per_day = int(input())

total_duration = walking_duration * walking_times
burned_callories = total_duration * 5

if float(burned_callories) >= (calories_per_day/2):
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_callories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_callories}.")
