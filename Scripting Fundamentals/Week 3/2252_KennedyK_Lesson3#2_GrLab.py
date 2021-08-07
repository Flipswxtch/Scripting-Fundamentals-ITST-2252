#!/usr/bin/env python

# FILE:2252_KennedyK_Lesson3#2_GrLab.py
# NAME: Hashtag Triangle
# AUTHOR(s): Kevin Kennedy
# DATE: 06/29/2021
# PURPOSE: Print out a triangle using nested loops

lineBreak = "#" * 60
print(lineBreak, "\n\n")

# create variable to start while loop
count = 0

# create while loop that executes as long as count < 1.
while count < 1:
    print("#")

    # iterate through the number 0-4 which are the number of spaces between 
    # hashes on their respective newline.
    for number_of_spaces in range(0, 5):
        print("#" + " " * number_of_spaces + "#")

    # do the same as above but iterate by -1 to reduce the number of spaces
    for number_of_spaces in range(4, 0, -1):
        print("#" + " " * (number_of_spaces - 1) + "#")
    
    #change count to exit out of while loop
    count += 1
    print("#")

print("\n\n\n")
print(lineBreak)

#Keep shell window/script open:
print(input('\n\nHit Enter to Close\n'))