
import re



pattern = r"(([2-9]|10)+|[JQKA]+)+[SHDC]"

#in_line="2SASKS6SJSQSOS10S"
in_line=input()


matches = re.finditer(pattern, in_line)

for i in matches:
    print(i.group(), end = " ")
