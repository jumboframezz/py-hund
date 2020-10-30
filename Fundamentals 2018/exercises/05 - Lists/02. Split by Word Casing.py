# 02. Split by Word Casing
# Read a text, split it into words and distribute them into 3 lists.
# 	Lower-case words like “programming”, “at” and “databases” – consist of lowercase letters only.
# 	Upper-case words like “PHP”, “JS” and “SQL” – consist of uppercase letters only.
# 	Mixed-case words like “C#”, “SoftUni” and “Java” – all others.
# Use the following separators between the words: , ; : . ! ( ) " ' \ / [ ] space
# Print the 3 lists as shown in the example below.
#
# Input:
#
#
# Output:
# Lower-case: programming, at, databases, etc
# Mixed-case: Learn, SoftUni, Java, 5, Web, C#
# Upper-case: PHP, JS, HTML, CSS, SQL, AJAX

line = ""
#  line = "Learn programming at SoftUni: Java, PHP, JS, HTML 5, CSS, Web, C#, SQL, databases, AJAX, etc."
if len(line) == 0:
    line = input()

delimiters = [",", ";", ":", ".", "!", "(", ")", "\"", "\'", "\\", "/", "[", "]"]

lower = []
upper = []
mixed = []

for separator in delimiters:
    line = line.replace(separator, " ")

words = [word for word in line.split()]
for word in words:
    if word == word.lower() and word.isalpha():
        lower.append(word)
    elif word == word.upper() and word.isalpha():
        upper.append(word)
    else:
        mixed.append(word)

print(f"Lower-case: {', '.join(lower)}")
print(f"Mixed-case: {', '.join(mixed)}")
print(f"Upper-case: {', '.join(upper)}")
