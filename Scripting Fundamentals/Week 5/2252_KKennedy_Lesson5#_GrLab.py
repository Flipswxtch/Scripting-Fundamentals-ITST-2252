#!/usr/bin/env python  #What is this line for? Watch the SHEBANG video in lesson 01

# FILE:2252_KKennedy_Lesson5#_GrLab.py  
# NAME: TalkLikeAPirate.py  
# AUTHOR(s): Kevin Kennedy  
# DATE: 07/14/2021
# PURPOSE: Take an English sentence from the user and convert certain words to
# pirate speak.

lineBreak = "#"*60
print(lineBreak, "\n\n")

words_that_can_translate = ["hello", "hi", "my", "friend","sir", "where", " is ",
"the ", "there", "you", "ing"]

translated_words = ["ahoy", "yo-ho-ho", "me", "bucko", "matey", "whar", " be ", 
"th'", "thar", "ye", "in'"]

# Introduction statements, print out list of words that can be translated.
def introductory_statements():
    """This function contains introductory statements and prints a list of 
    words that can be converted.
    """
    print("Hello, welcome to Talk Like a Pirate!")
    print("This program will take an English phrase that you input and will convert specific " \
        "words to pirate speak. Below is a list of the words that will be converted so make" \
            "sure to include them in your sentence!\n")
    print("Words that can be converted: ")
    for word in words_that_can_translate:
        print(word.strip())
    print("*Words that end in 'ing'")

# Core logic of the program
def translate_to_pirate_speak():
    """This is the core logic of the program where translation occurrs and the user chooses
    whether or not to play again.
    """
    # Initiate while loop that continues as long as the user wants to play.
    user_wants_translation = True
    while user_wants_translation == True:
        phrase_to_convert = input("\nPlease enter a phrase that contains some words listed " \
        "above: ")

        # These two for loops make lists that contain the capitalized version of each
        # word that can be translated and the translated words. Does not include
        # words ending in 'ing' as the 'ing' won't need capitalized.
        capitalized_words_that_can_translate = []
        for word in words_that_can_translate[:-1]:
            capitalized_words_that_can_translate.append(word.capitalize())
        capitalized_translated_words = []
        for word in translated_words[:-1]:
            capitalized_translated_words.append(word.capitalize())
        
        # Conversion happens here. Quantity of iterations is determined by the length of 
        # the words_that_can_translate list. With each iteration, a word is swapped out if it is found.
        new_phrase = phrase_to_convert.replace(words_that_can_translate[0], translated_words[0])
        for index in range(1, len(words_that_can_translate)):
            new_phrase = new_phrase.replace(words_that_can_translate[index], translated_words[index])
        for index in range(0, len(capitalized_words_that_can_translate)):
            new_phrase = new_phrase.replace(capitalized_words_that_can_translate[index], capitalized_translated_words[index])

        print(f"\nHere is your converted phrase:\n{new_phrase}")

        # Input validation while asking the user if they want to play again.
        user_input_is_valid = False
        while user_input_is_valid == False:
            user_wants_continue = input("\nWould you like to input another phrase, Y/N? ").lower()
            if user_wants_continue == "y" or user_wants_continue == "n":
                user_input_is_valid = True
            else:
                print(f"The input you entered, {user_wants_continue}, is not valid. Try again.\n")

        # Exit the outer while loop if the user says 'n' to playing again.
        if user_wants_continue == 'n':
            user_wants_translation = False
            print("Thank you for playing!")

print("\n\n", lineBreak)

# Make sure program doesn't run if imported into another module.
if __name__ == "__main__":
    introductory_statements()
    translate_to_pirate_speak()

#Keep shell window/script open:
print(input('\n\nHit Enter to Close\n'))