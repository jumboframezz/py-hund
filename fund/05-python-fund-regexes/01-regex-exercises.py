

'''^[A-Z]{1}[a-z]+ {1}[A-Z]{1}[a-z]+'''
import re

names = input()
#names = "Ivan Ivanov, Ivan ivanov, ivan Ivanov, IVan Ivanov, Test Testov, Ivan Ivanov"

pattern = r"\b[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+"
matches = re.findall(pattern, names)

for i in matches:
    print(i, end = " ")

