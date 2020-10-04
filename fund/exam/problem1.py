import datetime

name = 'Fred'
age = 46
anniversary = datetime.date(1972, 10, 8)
print(f'My name is {name}, my age next year is {age+1}, my anniversary is {anniversary:%A, %B %d, %Y}.')
print(f'He said his name is {name!r}.')

x=f'My name is {name}, my age next year is {age+1}, my anniversary is {anniversary:%A, %B %d, %Y}.'

