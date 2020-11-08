
# Еднакви суми на четни и нечетни позиции
# Напишете програма, която чете от конзолата две шестцифрени цели числа в диапазона. Винаги първото въведено число
# ще бъде по-малко от второто. На конзолата да се отпечатат на 1, ред разделени с интервал, всички числа, които се
# намират между двете, прочетени от конзолата числа, и отговарят на условието сумата от цифрите на четни и нечетни
# позиции да са равни. Ако няма числа, отговарящи на условието на конзолата не се извежда резултат.


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


first_num = int(input())
second_num = int(input())
sum_odd = 0
sum_even = 0

for digits in range(first_num, second_num + 1):
    digit_str = str(digits)
    for digit in range(len(digit_str)):
        if is_even(digit):
            sum_even += int(digit_str[digit])
        else:
            sum_odd += int(digit_str[digit])
    if sum_even == sum_odd:
        print(f"{digits}", end=" ")
    sum_odd = 0
    sum_even = 0
