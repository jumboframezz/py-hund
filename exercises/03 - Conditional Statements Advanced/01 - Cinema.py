prices = {"Premiere": 12, "Normal": 7.50, "Discount": 5}

show_type = input()
rows = int(input())
cols = int(input())

print(f"{rows * cols * prices[show_type]} leva")
