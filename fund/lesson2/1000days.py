'''
Напишете програма, която въвежда рождена дата във формат “dd-MM-yyyy” и пресмята датата,
на която се навършват 1000 дни от тази рождена дата и я отпечатва в същия формат.
'''

from datetime import *

day, month, year = input().split('-')
input_date = date(int(year), int(month), int(day))
hundred_years = timedelta(days=999)
future_date = input_date + hundred_years
date_format = '%d-%m-%Y'

print(future_date.strftime(date_format))
