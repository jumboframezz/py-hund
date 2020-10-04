
n = int(input())

for i in range (0, n):
     cat_name = input()
     cat_family = input()
     cat_year = input()

     cat_id = str(cat_year)+str(ord(cat_name[0]))+str(ord(cat_family[0]))+str(i+1)
     print (cat_id)
