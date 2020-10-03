# Озеленяване на дворове
#
# Божидара разполага с няколко къщи на Черноморието и желае да озелени дворовете на някои от тях, като по този начин
# създаде уютна обстановка и комфорт на гостите си. За целта е наела фирма.
# Напишете програма, която изчислява необходимите средства, които Божидара ще трябва да заплати на фирмата
# изпълнител на проекта. Цената на един кв. м. е 7.61лв със ДДС. Тъй като нейният двор е доста голям, фирмата
# изпълнител предлага 18% отстъпка от крайната цена.
#
# Вход
# От конзолата се прочита само един ред:
# Кв. метри, които ще бъдат озеленени – реално число.
#
# Изход
# На конзолата се отпечатват два реда:
# "The final price is: {крайна цена на услугата} lv."
# "The discount is: {отстъпка} lv."


area = float(input())

price = area * 7.61
discount = price * 0.18
final_price = price - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")

# git init
# git add README.md
# git commit -m "first commit"
# git branch -M master
# git remote add origin git@github.com:jumboframezz/py-fundamentals.git
# git push -u origin master