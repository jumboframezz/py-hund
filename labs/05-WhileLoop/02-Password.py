# 2.	Парола
# Напишете програма, която първоначално прочита име и парола на потребителски профил. След това чете парола за вход,
# при въвеждане на грешна парола, потребителя да се подкани да въведе нова парола.


user_name = input()
password = input()

login_pass = input()
while login_pass != password:
    login_pass = input()
print(f"Welcome {user_name}!")