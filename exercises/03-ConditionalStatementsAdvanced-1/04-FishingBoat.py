budget = int(input())
season = input()
fishermans = int(input())
discount = 1

price = {"Spring": 3000, "Summer": 4200, "Autumn": 4200, "Winter": 2600}
subtotal = price[season]

if fishermans <= 6:
    discount = 0.9
elif 7 <= fishermans <= 11:
    discount = 0.85
elif fishermans >= 12:
    discount = 0.75

subtotal *= discount
if fishermans % 2 == 0 and season != "Autumn":
    subtotal *= 0.95


left = budget - subtotal
if left >= 0:
    print(f"Yes! You have {left:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(left):.2f} leva.")