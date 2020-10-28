# 6.	Число в интервалa
# Да се напише програма, която проверява дали въведеното от потребителя число е в интервала [-100, 100] и е различно
# от 0 и извежда "Yes", ако отговаря на условията, или "No" ако е извън тях


number = float(input())
print("Yes") if (number >= -100 and number <= 100) and number != 0 else print("No")

# Simpler:
# if (number >= -100 and number <= 100) and number != 0:
#     print("Yes")
# else:
#     print("No")
