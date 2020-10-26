# 2. Комбинации от букви
# Напишете програма, която да принтира на конзолата всички комбинации от 3 букви в зададен интервал, като се пропускат
# комбинациите съдържащи зададена от конзолата буква. Накрая трябва да се изпринтира броят на отпечатаните комбинации.
# Вход
# Входът се чете от конзолата и съдържа точно 3 реда:
# Ред 1.	Малка буква от английската азбука за начало на интервала – от ‘a’ до ‚z’.
# Ред 2.	Малка буква от английската азбука за край на интервала  – от първата буква до ‚z’.
# Ред 3.	Малка буква от английската азбука – от ‘a’ до ‚z’ – като комбинациите съдържащи тази буквата се пропускат.
# Изход
# Да се отпечатат на един ред всички комбинации отговарящи на условието плюс броят им разделени с интервал
# Изход:
# aaa aac aca acc caa cac cca ccc 8

start_letter_sym = input()
end_letter_sym = input()
skip_letter = input()

start_letter = ord(start_letter_sym)
end_letter = ord(end_letter_sym)
count = 0

for letter1 in range(start_letter, end_letter+1):
    for letter2 in range(start_letter, end_letter+1):
        for letter3 in range(start_letter, end_letter+1):
            rez = chr(letter1)+chr(letter2)+chr(letter3)
            if skip_letter not in rez:
                print(f"{chr(letter1)}{chr(letter2)}{chr(letter3)} ", end="")
                count += 1
print(count)
