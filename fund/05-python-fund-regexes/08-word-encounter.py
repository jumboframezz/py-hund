'''
Problem 08. Word Encounter

You will be given a filter, in the form of a string of two characters – the first being an ASCII character,
and the second – a digit.

You will then receive a sequence of sentences. You must extract all words from those sentences, and print only
the words that contain the given filter character, at least N times – N being the filter digit.

There are 2 types of sentences – Valid and Invalid. The valid ones, always start with a capital letter, and
always end with one of the following characters: ".", "!", "?". Invalid sentences, should be ignored.

Note: You WILL NOT be given more than 1 sentence on a single input line.

The input sequence ends, when you receive the command "end". After that you must print all the filtered words,
you've gathered.
The valid words must be printed, on a single line, separated by a comma and a space.

Examples

Input                                                  Output
l2                                                     will, likely, Will, playlife
This will, likely be a funny feeling, Laslo.
Will you come to my playlife ;)?
end

o1                                                    How, about, No, know, bro
How about... No...
Maaan, this is amazing! Yeah; I know bro!
end

Hint
Check if there is a way to find where a word, in a sentence, starts, and ends. There surely must be a way to
do that with Regular Expressions.



'''
import re
in_line=input()
num_maches=int(in_line[1:])
match_char=in_line[0]
sentence_patt=r"^[A-Z](.*[.|?|!])?$"

words = []
line = ""
rpatt=r"\w+"
in_line = input()
while in_line != "end":
    if re.match(sentence_patt, in_line ):
        m =  re.finditer(rpatt, in_line)
        for i in m:
            if i.group().count(match_char) >= num_maches:
                words.append(i.group())
    in_line = input()

for i in words:
    line += f"{i}, "

print(line.strip(", "))

