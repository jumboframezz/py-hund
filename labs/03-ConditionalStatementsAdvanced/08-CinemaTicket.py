# 8.	Билет за кино
# Да се напише програма която чете ден от седмицата (текст) – въведен от потребителя и принтира на конзолата
# цената на билет за кино според деня от седмицата:
#
# Monday	Tuesday	Wednesday	Thursday	Friday	Saturday	Sunday
#     12	     12	       14	      14	    12	      16	    16
#

prices = {"Monday": 12,	"Tuesday": 12, "Wednesday": 14, "Thursday": 14, "Friday": 12, "Saturday": 16, "Sunday": 16}
dow = input()
print(prices[dow])