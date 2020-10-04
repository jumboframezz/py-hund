sleeve = float(input())
front = float(input())
fabric = input()
tie = input()



if fabric == "Linen":
    fabric_price = 15
elif fabric == "Cotton":
    fabric_price =12
elif fabric == "Denim":
    fabric_price = 20
elif fabric == "Twill":
    fabric_price = 16
elif fabric == "Flannel":
    fabric_price = 11
else:
    fabric_price = 1


area = sleeve *2 + front *2
area = area + (area * 0.1)
area_m = area /100

price = area_m * fabric_price +10

if tie == "Yes":
    price  = price +(price*0.2)
print ("The price of the shirt is: %.2flv."%price)

