import math
year = input()
p = int(input())
h = int(input())

weekend_games = (48 - h) * (3/4)
holyday_games = p * (2/3)

total_games = weekend_games + holyday_games + h
if year == "leap":
    total_games *= 1.15
print(math.floor(total_games))
