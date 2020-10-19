price = {"Roses": 5, "Dahlias": 3.80, "Tulips": 2.80, "Narcissus": 3, "Gladiolus": 2.50}
flower_type = input()
flower_num = int(input())
budget = float(input())

amount = price[flower_type] * flower_num

if flower_type == "Roses" and flower_num > 80:
    amount *= 0.9
elif flower_type == "Dahlias" and flower_num > 90:
    amount *= 0.85
elif flower_type == "Tulips" and flower_num > 80:
    amount *= 0.85
elif flower_type == "Narcissus" and flower_num < 120:
    amount *= 1.15
elif flower_type == "Gladiolus" and flower_num < 80:
    amount *= 1.2

if amount <= budget:
    print(f"Hey, you have a great garden with {flower_num} {flower_type} and {budget-amount:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(budget - amount):.2f} leva more.")
