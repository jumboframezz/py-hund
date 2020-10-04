import re


pattern = r"\b(?:0x)?[0-9A-F]+\b"

#in_data = "1F 0xG 0x1F G 0x4G 4G 0xAB 0xFG FG 0x10 10 AB FF"
in_data = input()

matches = re.finditer(pattern, in_data)

for i in matches:
    print(i.group(), end = " ")

