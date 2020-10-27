# 6. Сватбени места
# Младоженците искат да направят списък кой на кое място ще седи на сватбената церемония. Местата са разделени на
# различни сектори.
# Секторите са главните латински букви като започват от A. Във всеки сектор има определен брой редове.
# От конзолата се чете броят на редовете в първия сектор (A), като във всеки следващ сектор редовете се увеличават с 1.
# На всеки ред има определен брой места - тяхната номерация е представена с малките латински букви.
# Броя на местата на нечетните редове се прочита от конзолата, а на четните редове местата са с 2 повече.
# Вход
# От конзолата се четaт 3 реда:
# • Последния сектор от секторите - символ (B-Z)
# • Броят на редовете в първия сектор - цяло число (1-100)
# • Броят на местата на нечетен ред - цяло число (1-24)
# Изход
# Да се отпечата на конзолата всяко място на отделен ред по следния формат:
# {сектор}{ред}{място}
# Накрая трябва да отпечата броя на всички места.

last_sector = input()
last_sector_num = ord(last_sector)
start_sector_num = ord("A")
start_seat_count = ord("a")
first_sector_rows = int(input())
odd_row_num = int(input())
total_seats = 0
seat = 0

for sector in range(start_sector_num, last_sector_num+1):
    for row_count in range(1, first_sector_rows+1):
        if row_count % 2 == 0:
            seat_count = odd_row_num + 2
        else:
            seat_count = odd_row_num
        for seat in range(start_seat_count, start_seat_count + seat_count ):
            print(f"{chr(sector)}{row_count}{chr(seat)}")
            total_seats += 1
    first_sector_rows += 1

print(total_seats)
