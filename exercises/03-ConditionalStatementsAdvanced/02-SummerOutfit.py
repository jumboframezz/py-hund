outfit = ""
shoes = ""
temperature = int(input())
part_of_day = input()
if 10 <= temperature <= 18:
    if part_of_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif part_of_day == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    else:
        outfit = "Shirt"
        shoes = "Moccasins"

elif 18 < temperature <= 24:
    if part_of_day == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif part_of_day == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    else:
        outfit = "Shirt"
        shoes = "Moccasins"
elif temperature >= 25:
    if part_of_day == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif part_of_day == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    else:
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
