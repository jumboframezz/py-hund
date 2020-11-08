#
# Суми прости и непрости числа
# Напишете програма, която чете от конзолата цели числа, докато не се получи команда "stop". Да се намери сумата на
# всички въведени прости и сумата на всички въведени непрости числа. Тъй като по дефиниция от математиката отрицателните
# числа не могат да бъдат прости, ако на входа се подаде отрицателно число, да се изведе следното
# съобщение "Number is negative.". В този случай въведено число се игнорира и не се прибавя към нито една от двете с
# уми, а програмата продължава своето изпълнение, очаквайки въвеждане на следващо число.
# На изхода да се отпечатат на два реда двете намерени суми в следния формат:
# "Sum of all prime numbers is: {prime numbers sum}"
# "Sum of all non prime numbers is: {nonprime numbers sum}"


def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True
    else:
        return False


sum_prime = 0
sum_nonprime = 0

num_str = input()
while num_str != "stop":
    num = int(num_str)
    if num < 0:
        print("Number is negative.")
        num_str = input()
        continue
    if is_prime(num):
        sum_prime += num
    else:
        sum_nonprime += num
    num_str = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_nonprime}")
