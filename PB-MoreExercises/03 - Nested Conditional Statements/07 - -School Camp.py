# 7.	Ученически лагер
# Частно училище организира лагери за учениците по време на ваканциите. В зависимост от вида на ваканцията
# (пролетна, лятна или зимна) и вида на групата (момчета/момичета или смесена) цената на нощувката в хотела е
# различна, както и спортът, който ще практикуват учениците.
#
# 	                        Зимна ваканция	Пролетна ваканция	Лятна ваканция
# момчета/момичета	                  9.60	             7.20	            15
# смесена група	                        10	             9.50	            20
#
# Училището получава отстъпка от крайната цена, в зависимост от броя на настанените в хотела ученици:
# •	Ако броят на учениците е 50 или повече, училището получава 50% отстъпка
# •	Ако броят на учениците е 20 или повече и в същото време по-малък от 50, училището получава 15% отстъпка
# •	Ако броят на учениците е 10 или повече и в същото време по-малък от 20, училището получава 5% отстъпка
# В таблицата по-долу са дадени спортовете, които ще се практикуват в зависимост от вида на ваканцията и групата:
#
# 	        Зимна ваканция	    Пролетна ваканция	    Лятна ваканция
# момичета	Gymnastics	        Athletics	            Volleyball
# момчета	Judo	            Tennis	                Football
# смесена 	Ski	                Cycling	                Swimming
#
# Да се напише програма, която пресмята цената, която ще заплати училището за нощувките и принтира спорта, който ще се
# практикува от учениците.
# Вход
# От конзолата се четат 4 реда:
# 1.	Сезонът – текст - “Winter”, “Spring” или “Summer”;
# 2.	Видът на групата – текст - “boys”, “girls” или “mixed”;
# 3.	Брой на учениците – цяло число в интервала [1 … 10000];
# 4.	Брой на нощувките – цяло число в интервала [1 … 100].
# Изход
# На конзолата се отпечатва 1 ред:
# •	Спортът, който са практикували учениците и цената за нощувките, която е заплатило училището, форматирана до
# втория знак след десетичната запетая, в следния формат:
# "{спортът} {цената} lv.“

season = input()
group_type = input()
student_num = int(input())
days = int(input())
price = None
sport = None
sub_total = None
discount = 1

if season == "Winter":
    if group_type == "boys":
        price = 9.60
        sport = "Judo"
    elif group_type == "girls":
        price = 9.60
        sport = "Gymnastics"
    else:
        price = 10
        sport = "Ski"
elif season == "Spring":
    if group_type == "boys":
        price = 7.20
        sport = "Tennis"
    elif group_type == "girls":
        price = 7.20
        sport = "Athletics"
    else:
        price = 9.50
        sport = "Cycling"
elif season == "Summer":
    if group_type == "boys":
        price = 15
        sport = "Football"
    elif group_type == "girls":
        price = 15
        sport = "Volleyball"
    else:
        price = 20
        sport = "Swimming"

if student_num >= 10 and student_num < 20:
    discount = 0.95
elif student_num >= 20 and student_num < 50:
    discount = 0.85
elif student_num >= 50:
    discount = 0.5

sub_total = price * days
sub_total *= student_num
total = sub_total * discount
print(f"{sport} {total:.2f} lv.")
