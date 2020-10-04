

#p_happy = r"(?P<happy>\:\)|\:D|\;\)|\:\*|\:\]|\;\]|\:\}|\;\}|\(\:|\*\:|c\:|\[\:|\[\;)"
#p_sad = r"?P<sad>\:\(|D\:|\;\(|\:\[|\;\[|\:\{|\;\{|\)\:|\:c|\]\:|\]\;)"






import re, math
pattern = "(?P<happy>\:\)|\:D|\;\)|\:\*|\:\]|\;\]|\:\}|\;\}|\(\:|\*\:|c\:|\[\:|\[\;)|(?P<sad>\:\(|D\:|\;\(|\:\[|\;\[|\:\{|\;\{|\)\:|\:c|\]\:|\]\;)"

in_line = input()
#in_line = ":)^%&:)**&:]v;)ff:("
matches = re.finditer(pattern, in_line)
happy = 0
sad = 0
#index = 0.00
for m in matches:
    if m.group("happy") != None:
        happy += 1
    if m.group("sad") != None:
        sad += 1

index = happy / sad

if index >= 2 :
    index_icon = ":D"
elif index > 1:
    index_icon = ":)"
elif index == 1:
    index_icon = ":|"
elif index < 1:
        index_icon = ":("



print(f"Happiness index: {index:.2f} {index_icon}")
print(f"[Happy count: {happy}, Sad count: {sad}]")

