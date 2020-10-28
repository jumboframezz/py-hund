
# Резервоар за гориво
# Напишете програма, която познава дали резервоара на едно превозно средство има нужда от презареждане на горивото
# или не. От конзолата се четат два реда – текст и реално число, на първия ред се чете типа на горивото – текст
# с възможности: "Diesel", "Gasoline" или "Gas", а на втория литрите гориво, които има в резервоара. Ако литрите гориво
# са повече или равни на 25, на конзолата да се отпечата "You have enough {вида на горивото}.", ако са по-малко от 25,
# да се отпечата "Fill your tank with {вида на горивото}!". В случай, че бъде въведено гориво, различно от
# посоченото, да се отпечата "Invalid fuel!".

fuel_type = input()
fuel_amount = float(input())

if fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas":
    if fuel_amount >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")
else:
    print("Invalid fuel!")
