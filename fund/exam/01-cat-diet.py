

percent_fat = int(input())
percent_proteins = int(input())
percent_carbohydrates = int(input())

total_calories = int(input())
percent_water = int(input())


fat = (percent_fat / 100) * total_calories / 9
proteins = (percent_proteins / 100) * total_calories / 4
carbohydrates = (percent_carbohydrates / 100) * total_calories /4
water = (percent_water / 100)

food_weight = fat + proteins +carbohydrates



calories_per_g = total_calories / food_weight
result = calories_per_g * (1-water)
print("%.4f"%result)

