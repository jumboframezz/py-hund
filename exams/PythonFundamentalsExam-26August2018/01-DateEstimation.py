# Problem 1. Date estimation
# Input / Constraints
# Today is your exam. It’s 26th of August 2018. you will be given a single date in format year-month-day. You should
# estimate if the date has passed regarding to the date mention above (2018-08-26), if it is not or if it is today.
# If it is not you should print how many days are left till that date. Note that the current day stills count!
# Date Format:
# yyyy-mm-dd
# Output
# The output should be printed on the console.
# If the date has passed you should print the following output:
# • "Passed"
# If the day is today:
# "Today date"
# If the date is future:
# • "{number of days} days"
#
# Input           Output
# 2018-08-20      Passed
# 2021-08-26      1097 days left
# URL: https://judge.softuni.bg/Contests/1140/Python-Fundamentals-Exam-26-August-2018
import time
import datetime

def days_between(d1, d2):
    from datetime import datetime
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return (d2 - d1).days


exam_date = "2018-08-26"
in_date = input()
diff = days_between(exam_date, in_date)

if diff < 0:
    print("Passed")
elif diff == 0:
    print("Today date")
elif diff > 0:
    print(f"{diff + 1} days left")






