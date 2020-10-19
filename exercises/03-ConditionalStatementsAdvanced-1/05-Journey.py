budget = float(input())
season = input()
destination = ""
price = 0
resort = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "winter":
        price = budget * 0.7
        resort = "Hotel"
    else:
        price = budget * 0.3
        resort = "Camp"
elif 101 <= budget <= 1000:
    destination = "Balkans"
    if season == "winter":
        resort = "Hotel"
        price = budget * 0.8
    else:
        price = budget * 0.4
        resort = "Camp"
elif budget > 1000:
    destination = "Europe"
    resort = "Hotel"
    price = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{resort} - {price:.2f}")
