# Last Stop
# The group has reached Paris and went to visit "La Louvre". They accidently found a map behind "The Wedding at Canna"
# painting. It had some instructions, so they have decided to follow them and see where they will lead them.
# Your job is to help them.
# Create a program that follows instructions in order to fulfil a quest. First, you will receive a collection of
# numbers – each representing a painting number. After that, you are going to be receiving instructions, until the
# "END" command is given.
#       -	Change {paintingNumber} {changedNumber} – find the painting with the first number in the collection
#           (if it exists) and change its number with the second number – {changedNumber}.
#       -	Hide {paintingNumber} – find the painting with this value and if it exists and hide it (remove it).
#       -	Switch {paintingNumber} {paintingNumber2} – find the given paintings in the collections if they exist
#           and switch their places.
#       -	Insert {place} {paintingNumber} – insert the painting (paintingNumber) on the next place after
#           the given one, if it exists.
#       -	Reverse – you must reverse the order of the paintings.
# Once you complete the instructions, print the numbers of the paintings on a single line, split by a space.
# Input / Constraints
#   •	On the 1st line, you are going to receive the numbers of the paintings, split by a single
#       space – integer numbers in the range [1…1000]
#   •	On the next lines, you are going to receive commands, until you receive the "END" command
# Output
# •	Print the message you have received after the conversion of all numbers on a single line
# Input                                     Output
# 115 115 101 114 73 111 116 75             70 114 111 116 114 101 115 115
# Insert 5 114
# Switch 116 73
# Hide 75
# Reverse
# Change 73 70
# Insert 10 85
# END

def index_exists(arr, index):
    try:
        res = arr[index]
        return True
    except IndexError:
        return False


def change(arr, p1, p2):
    if p1 in arr:
        index = arr.index(p1)
        arr[index] = p2
    return arr


def hide(arr, p1):
    if p1 in arr:
        index = arr.index(p1)
        arr.pop(index)
    return arr


def switch(arr, p1, p2):
    if p1 in arr and p2 in arr:
        index1 = arr.index(p1)
        index2 = arr.index(p2)
        arr[index1], arr[index2] = arr[index2], arr[index1]
    return arr


def insert_p(arr, p1, p2):
    if p1 >= 0 and p1 < len(arr):
        arr.insert(p1 + 1, p2)
    return arr


def reverse_p(arr):
    arr.reverse()
    return arr


items = [int(_) for _ in input().split()]
entry = input()
while entry != "END":
    cmd = entry.split()
    if index_exists(cmd, 1): cmd[1] = int(cmd[1])
    if index_exists(cmd, 2): cmd[2] = int(cmd[2])
    if cmd[0] == "Change":
        items = change(items, cmd[1], cmd[2])
    elif cmd[0] == "Hide":
        items = hide(items, cmd[1])
    elif cmd[0] == "Switch":
        items = switch(items, cmd[1], cmd[2])
    elif cmd[0] == "Insert":
        items = insert_p(items, cmd[1], cmd[2])
    elif cmd[0] == "Reverse":
        items = reverse_p(items)
    entry = input()

print(" ".join([str(_) for _ in items]))
