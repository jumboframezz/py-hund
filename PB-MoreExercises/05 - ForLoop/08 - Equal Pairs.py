# 8. Еднакви двойки
# Дадени са 2*n-на брой числа. Първото и второто формират двойка, третото и четвъртото също и т.н. Всяка двойка има
# стойност – сумата от съставящите я числа. Напишете програма, която проверява дали всички двойки имат еднаква стойност
# или печата максималната разлика между две последователни двойки. Ако всички двойки имат еднаква стойност,
# отпечатайте "Yes, value = {Value}" + стойността. В противен случай
# отпечатайте "No, maxdiff = {Difference}" + максималната разлика.


count = int(input())

max_diff = 0
old_sum = 0
new_sum = 0
diff = 0
all_same = 0
for pair in range(0, count):
    n1 = int(input())
    n2 = int(input())
    new_sum = n1 + n2
    if pair != 0:
        diff = abs(old_sum - new_sum)
    if diff > max_diff:
        max_diff = diff
    if old_sum != new_sum:
        all_same += 1
    old_sum = new_sum

if all_same > 1:
    print(f"No, maxdiff={max_diff}")
else:
    print(f"Yes, value={new_sum}")
