# 9. Плод или зеленчук
# Да се напише програма, която чете име на продукт, въведено от потребителя, и проверява дали е плод или зеленчук.
# • Плодовете "fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes;
# • Зеленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot;
# • Всички останали са "unknown".
# Да се изведе "fruit", "vegetable" или "unknown" според въведения продукт.

plants = {"fruit": ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"],
          "vegetable": ["tomato", "cucumber", "pepper", "carrot"]}

product = input()
if product in plants["fruit"]:
    print("fruit")
elif product in plants["vegetable"]:
    print("vegetable")
else:
    print("unknown")