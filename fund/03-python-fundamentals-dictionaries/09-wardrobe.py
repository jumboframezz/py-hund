'''
Wardrobe

You just bought a new wardrobe. The weird thing about it is that it came prepackaged with a big box of clothes
(just like those refrigerators, which ship with free beer inside them)! So, you’ll need to find something to wear.

Input

On the first line of the input, you will receive n –  the number of lines of clothes, which came prepackaged for
the wardrobe.

On the next n lines, you will receive the clothes for each color in the format:
“{color} -> {item1},{item2},{item3}…”

If a color is added a second time, add all items from it and count the duplicates.
Finally, you will receive the color and item of the clothing, that you need to look for.

Output

Go through all the colors of the clothes and print them in the following format:

{color} clothes:

* {item1} - {count}
* {item2} - {count}
* {item3} - {count}
…
* {itemN} - {count}

If the color lines up with the clothing item, print “(found!)” alongside the item. See the examples to better
understand the output.

Examples:
Input:
4
Blue -> dress,jeans,hat
Gold -> dress,t-shirt,boxers
White -> briefs,tanktop
Blue -> gloves
Blue dress

5
Blue -> shoes
Blue -> shoes,shoes,shoes
Blue -> shoes,shoes
Blue -> shoes
Blue -> shoes,shoes
Red tanktop

'''

colour=""
dresses={}
occurences = {}

n = int(input())

for i in range (0,n):
    in_line = input().split(" -> ")
    colour = in_line[0]
    if not dresses.get(colour):
        dresses[colour] = in_line[1].split(",")
    else:
        for j in in_line[1].split(","):
            dresses[colour].append(j)
dress_to_find = input().split(" ")

for jj in dresses:
    print(f"{jj} clothes:")
    for jjj in dresses[jj]:
        if not jjj in occurences:
               occurences[jjj] = 1
        else:
               occurences[jjj] +=1
    for iii in occurences:
        if jj == dress_to_find[0] and iii == dress_to_find[1]:
            print(f"* {iii} - {occurences[iii]} (found!)")
        else:
            print(f"* {iii} - {occurences[iii]}")
    occurences.clear()