'''

Exam Shopping

A supermarket has products which have quantities. Your task is to stock the shop before Exam Sunday. Until you
receive the command “shopping time”, add the various products to the shop’s inventory, keeping track of their
quantity (for inventory purposes). When you receive the aforementioned command, the students start pouring in before
the exam and buy various products.

The format for stocking a product is: “stock {product} {quantity}”.
The format for buying a product is: “buy {product} {quantity}”.

If a student tries to buy a product, which doesn’t exist, print “{product} doesn't exist”. If it does exist, but
it’s out of stock, print “{product} out of stock”. If a student tries buying more than the quantity of that product,
sell them all the quantity of the product (the product is left out of stock, don’t print anything).

When you receive the command “exam time”, your task is to print the remaining inventory in the
following format: “{product} -> {quantity}”. If a product is out of stock, do not print it.

Examples:
Input                           Output
stock Boca_Cola 10              Boca_Cola -> 15
stock Boca_Cola 10
stock Kay&#39;s 3
stock Kay&#39;s 2
shopping time
buy Boca_Cola 5
buy Kay&#39;s 5
exam time

stock Boca_Cola 16              Boca_Bola doesn't exist
stock Kay's_Chips 33            Boba_Bola doesn't exist
stock Lobster_Energy 60         Boca_Cola -> 19
stock Boca_Cola 4               Kay's_Chips -> 33
stock Loreni 15                 Lobster_Energy -> 40
stock Loreni 15                 Loreni -> 60
stock Loreni 15
stock Loreni 15
shopping time
buy Boca_Bola 2
buy Lobster_Energy 20
buy Boca_Cola 1
buy Boba_Bola 12
exam time

stock Boca_Cola 16
stock Kay's_Chips 33
stock Lobster_Energy 60
stock Boca_Cola 4
stock Loreni 15
stock Loreni 15
stock Loreni 15
stock Loreni 15
shopping time
buy Boca_Bola 2
buy Lobster_Energy 20
buy Boca_Cola 1
buy Boba_Bola 12
buy Loreni 90
buy Loreni 90
exam time

Boca_Bola doesn&#39;t exist
Boba_Bola doesn&#39;t exist
Boca_Cola -&gt; 19
Kay&#39;s_Chips -&gt; 33
Lobster_Energy -&gt; 40
Loreni -&gt; 60

7. User Logins

'''

in_line=input().strip(" ")
dict = {}
print_dict = {}
while in_line != "shopping time":
    params = in_line.split(" ")
    stock = params[1]
    qty = int(params[2])
    if dict.get(stock):
            dict[stock] += qty
    else:
            dict[stock] = qty
    in_line = input().strip(" ")

in_line=""
in_line=input().strip(" ")
while in_line != "exam time":
    params = in_line.split(" ")
    stock = params[1]
    qty = int(params[2])
    if dict.get(stock):
        if dict[stock] <= 0:
            print(f"{stock} out of stock")
        elif dict[stock] - qty <= 0:
            dict[stock] = -1
        else:
            dict[stock] -= qty
    else:
        print(f"{stock} doesn't exist")

    in_line = input().strip(" ")

#for i in sorted(dict.keys()):
for i in dict:
    if dict[i] >= 1:
        print(f"{i} -> {dict[i]}")




