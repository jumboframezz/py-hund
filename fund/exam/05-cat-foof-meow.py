
import math

n = int(input())
width = n*4


middle = "|"+ "\/"*n + "|"
dots = "." * int(n-1)

sub_middle = "|"+ "~"*int(n*2) + "|"


head = dots + middle + dots
sub_head = dots + sub_middle + dots
print (head)
print (sub_head)

count =0
for i in range(n, 0, -1 ):
    print ("%s|"%dots, end="")
    middle_line = " " * count + "{}"*int(i)+ " " * count
    print ("%s"%middle_line,end="")
    print ("|%s"%dots)
    count +=1

spaces= " "*int((n*2-4)/2)

print ("%s|"%dots, end="")
print ("%sMEOW%s"%(spaces,spaces),end="")
print ("|%s"%dots)

print ("%s|"%dots, end="")
print ("%sFOOD%s"%(spaces,spaces),end="")
print ("|%s"%dots)

count =n-1
for i in range(1, n+1):
    print ("%s|"%dots, end="")
    middle_line = " " * count + "{}"*int(i)+ " " * count
    print ("%s"%middle_line,end="")
    print ("|%s"%dots)
    count -=1

print (sub_head)
print (head)

