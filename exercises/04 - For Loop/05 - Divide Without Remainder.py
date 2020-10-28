
# Деление без остатък
# Дадени са n-на брой цели числа в интервала [1…1000]. От тях някакъв процент p1 се делят без остатък на 2, друг
# процент p2 се делят без остатък на 3, друг процент p3 се делят без остатък на 4. Да се напише програма, която
# изчислява и отпечатва процентите p1, p2 и p3.

def percentage(part, whole):
    return 100 * float(part) / float(whole)


p1 = 0
p2 = 0
p3 = 0

n = int(input())

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        p1 += 1
    if num % 3 == 0:
        p2 += 1
    if num % 4 == 0:
        p3 += 1
#print(f"{p1} {p2} {p3}")
print(f"{percentage(p1, n):.2f}%")
print(f"{percentage(p2, n):.2f}%")
print(f"{percentage(p3, n):.2f}%")
