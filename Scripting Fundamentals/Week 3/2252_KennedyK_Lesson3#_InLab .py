#!/usr/bin/env python

# FILE:2252_KennedyK_Lesson3#2_GrLab.py
# NAME: Chess Table
# AUTHOR(s): Kevin Kennedy
# DATE: 06/29/2021
# PURPOSE: Create a text-only chess table using iteration.

lineBreak = "#" * 60
print(lineBreak, "\n")
print("Below is a text-only chess table using iteration with for loops!")

# create a list of letters so that I may iterate through them.
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

#Print top of table
print("\n", "-" * 41)

#Begin by iterating through range of numbers, start at 8 and end at 1.
for number in range(8, 0, -1):

    #iterate through each letter in list of letters. Create variable that will 
    #contain each board space along with the pipe symbols in the table.
    for letter in letters:
        combination = " | " + letter + str(number)

        #was unable to add pipe symbol at the end so put conditional here to check
        #if letter h is in the combination, if it is add pipe to end of the combo.
        if 'h' in combination:
            combination = combination + " |"
        print(combination, end = "")

    #print bottom outline of table
    print("\n", "-" * 41)

print("\n\n\n")
print(lineBreak)

#Keep shell window/script open:
print(input('\n\nHit Enter to Close\n'))