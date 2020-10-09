
# Магазин за детски играчки
# Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни. С парите, които ще спечели,
# иска да отиде на екскурзия. Да се напише програма, която пресмята печалбата от поръчката.
# Цени на играчките:
# Пъзел - 2.60 лв.
# Говореща кукла - 3 лв.
# Плюшено мече - 4.10 лв.
# Миньон - 8.20 лв.
# Камионче - 2 лв.
# Ако поръчаните играчки са 50 или повече магазинът, прави отстъпка 25% от общата цена. От спечелените пари Петя трябва
# да даде 10% за наема на магазина. Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.
# Вход
# От конзолата се четат 6 реда:
# Цена на екскурзията - реално число;
# Брой пъзели - цяло число;
# Брой говорещи кукли - цяло число;
# Брой плюшени мечета - цяло число;
# Брой миньони - цяло число;
# Брой камиончета - цяло число.
#
# Изход
# На конзолата се отпечатва:
# Ако парите са достатъчни се отпечатва:
# "Yes! {оставащите пари} lv left."
# Ако парите НЕ са достатъчни се отпечатва:
# "Not enough money! {недостигащите пари} lv needed."
# Резултатът трябва да се форматира до втория знак след десетичната запетая.

trip_price = float(input())

num_puzzles = int(input())
num_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

pr_puzzles = num_puzzles * 2.6
pr_dolls = num_dolls * 3
pr_bears = num_bears * 4.10
pr_minions = num_minions * 8.20
pr_trucks = num_trucks * 2

order_items = num_puzzles + num_dolls + num_bears + num_minions + num_trucks

if order_items >= 50:
    discount = 0.75
else:
    discount = 1

subtotal = pr_puzzles + pr_dolls + pr_bears + pr_minions + pr_trucks

total = subtotal * discount
total *= 0.9

income = total - trip_price

if income >= 0:
    print(f"Yes! {income:.2f} lv left.")
else:
    income *= -1
    print(f"Not enough money! {income:.2f} lv needed.")
