import re

pattern = r"\b(?P<day>\d{2})([-\.\/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"

dates = input()

matches = re.finditer(pattern, dates)

for match in matches:
    day = match.group("day")
    month = match.group("month")
    year = match.group("year")
    print(f"Day: {day}, Month: {month}, Year: {year}")

