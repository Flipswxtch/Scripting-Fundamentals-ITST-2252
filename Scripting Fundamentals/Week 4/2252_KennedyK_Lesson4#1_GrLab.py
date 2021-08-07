#!/usr/bin/env python  #What is this line for? Watch the SHEBANG video in lesson 01

# FILE:2252_KennedyK_Lesson4#1_GrLab.py
# NAME: DiceRollingSimulator.py
# AUTHOR(s): Kevin Kennedy
# DATE: 07/08/2021
# PURPOSE: Simulates rolling a D20 dice. Can be used as many times in a row as the
# user would like.

lineBreak = "#"*60
print("\n\n", lineBreak)

import random


# Create function since that's what we worked with this week. Didn't really
# reuse code so couldn't find a better use for it.
def roll_random_number():
    """This function contains the core code of this dice rolling program.
    """

    print("This program simulates the rolling of a D20 dice. Follow the prompts" \
    " as they appear!")

    # Create while loop for the user to roll dice as many times as they want.
    user_wants_to_play = True
    while user_wants_to_play == True:

        # Require user to press enter, helps to slow down the output shown to the user.
        # Generate random number from 1-20 and print to screen.
        print(input("Press enter to roll the dice!"))
        dice_roll = random.randint(1, 20)
        print(dice_roll)

        # Prompt user to see if they'd like to roll again. Perform input 
        # validation by requiring answer to be either 'y' or 'n'.
        user_input_is_valid = False
        while user_input_is_valid == False:
            user_wants_continue = input("Would you like to roll again, Y/N? ").lower()
            if user_wants_continue == "y" or user_wants_continue == "n":
                user_input_is_valid = True
            else:
                print(f"The input you entered, '{user_wants_continue}'', is not valid. Try again.\n")
        
        # Exit outer while loop if user answers 'n' to roll again prompt.
        if user_wants_continue == "n":
            user_wants_to_play = False
        
# Make sure program does not run if imported into another module.
if __name__ == "__main__":
    roll_random_number()


print("\n\n", lineBreak)



#Keep shell window/script open:
print(input('\n\nHit Enter to Close\n'))



