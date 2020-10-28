# 3. Почивка
# Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере дали ще успее да събере
# необходимата сума. Тя спестява или харчи част от парите си всеки ден. Ако иска да похарчи повече от наличните си
# пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.
# Вход
# От конзолата се четат:
#   •	Пари, нужни за екскурзията - реално число;
#   •	Налични пари - реално число.
# След това многократно се четат по два реда:
#   •	Вид действие – текст с две възможности: "spend" или "save";
#   •	Сумата, която ще спести/похарчи - реално число.
# Изход
# Програмата трябва да приключи при следните случаи:
#   •	Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:
#       o	"You can't save the money."
#       o	"{Общ брой изминали дни}"
# •	Ако Джеси събере парите за почивката, на конзолата се изписва:
#       o	"You saved the money for {общ брой изминали дни} days."

trip_price = float(input())
debit_amount = float(input())
day_counter = 1
spend_day_counter = 0
operation = ""

while spend_day_counter < 5:
    if debit_amount >= trip_price:
        break
    operation = input()
    amount = float(input())
    if operation == "spend":
        spend_day_counter += 1
        debit_amount -= amount
        if debit_amount < 0:
            debit_amount = 0
    else:
        debit_amount += amount
        spend_day_counter = 0
    day_counter += 1

day_counter -= 1
if spend_day_counter >= 5:
    print("You can't save the money.")
    print(f"{day_counter}")
else:
    print(f"You saved the money for {day_counter} days.")
