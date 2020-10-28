# 7.	Работно време
# Да се напише програма, която чете час от денонощието(цяло число) и ден от седмицата(текст) - въведени от потребителя
# и проверява дали офисът на фирма е отворен, като работното време на офисът е от 10-18 часа, от понеделник до
# събота включително

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

hour = int(input())
dow = input()

dayn = days.index(dow)
if dayn >= 0 and dayn <= 5 and hour >= 10 and hour <= 18:
    print("open")
else:
    print("closed")