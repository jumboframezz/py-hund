
kg_food = int(input())

food = kg_food*1000

food_left = food
eaten_total=0
eaten = "0"
while eaten != "Adopted":
    eaten = input()
    if eaten == "Adopted":
            break
    food_left = food_left - int(eaten)
    eaten_total = eaten_total+int(eaten)

if food_left >= 0:
    print("Food is enough! Leftovers: %d grams."%food_left)
else:
    print("Food is not enough. You need %d grams more."%abs(eaten_total - food) )
