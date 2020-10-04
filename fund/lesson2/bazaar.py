veg_price = float(input())
fruit_price = float(input())

veg_kgs=int(input())
fruit_kgs=int(input())

vegs = veg_kgs*veg_price
fruits = fruit_kgs*fruit_price

profit= (vegs + fruits) / 1.94

print(profit)