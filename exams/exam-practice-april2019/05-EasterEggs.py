# Задача 5. Великденски яйца
# Предстои Великден и едно от най-вълнуващите неща е боядисването на яйца. Наличните цветове за
# боядисване са:
# • червено (red)
# • оранжев (orange)
# • син (blue)
# • зелен (green)
# Напишете програма, която изчислява какъв е броят на яйцата от всеки цвят и от кой цвят яйцата са най - много,
# като знаете общия им брой и цвета на всяко яйце.
# Вход
# От конзолата се чете 1 ред:
# • Броят на боядисаните яйца – цяло число в интервала [1 ... 100]
# За всяко яйце се чете:
# o Цветът на яйцето – текст с възможности: "red", "orange", "blue", "green"
# Изход
# Да се отпечатат на конзолата 5 реда:
# • "Red eggs: {брой на червените яйца}"
# • "Orange eggs: {брой на оранжевите яйца}"
# • "Blue eggs: {брой на сините яйца}"
# • "Green eggs: {брой на зелените яйца}"
# • "Max eggs: {максимален брой на яйцата от цвят} -> {цвят}"
# URL to check: https://judge.softuni.bg/Contests/Practice/Index/1637#8

num_eggs = int(input())
red = 0
orange = 0
blue = 0
green = 0

for egg in range(1, num_eggs+1):
    color = input()
    if color == "red":
        red += 1
    elif color == "orange":
        orange += 1
    elif color == "blue":
        blue += 1
    elif color == "green":
        green += 1

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")

max_color = "red"
max_eggs = red

if orange > max_eggs:
    max_color = "orange"
    max_eggs = orange

if blue > max_eggs:
    max_color = "blue"
    max_eggs = blue

if green > max_eggs:
    max_color = "green"
    max_eggs = green

print(f"Max eggs: {max_eggs} -> {max_color}")
