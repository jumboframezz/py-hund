'''
5. Numbers with Step
Write a python program, which receives a start number, an end number and a step. Write a simple for loop, which
prints all the numbers from the start number to the end number, using the specified step. Print the numbers on
separate lines.
Use the range() function.
'''

start = int(input())
end = int(input())
step = int(input())



for i in range (start, end, step):
    print (i)
