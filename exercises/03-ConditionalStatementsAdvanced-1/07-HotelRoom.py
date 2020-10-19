month = input()
days = int(input())

studio_price = 0
apartment_price = 0
studio_discount = 1
apartment_discount = 1


if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < days <= 14:
        studio_discount = 0.95
    elif days > 14:
        studio_discount = 0.70
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
elif month == "September" or month == "June":
    studio_price = 75.20
    apartment_price = 68.70
    if days >= 15:
        studio_discount = 0.80

if days > 14:
    apartment_discount = 0.9

apartment_total = apartment_price * days * apartment_discount
studio_total = studio_price * days * studio_discount
print(f"Apartment: {apartment_total:.2f} lv.")
print(f"Studio: {studio_total:.2f} lv.")
