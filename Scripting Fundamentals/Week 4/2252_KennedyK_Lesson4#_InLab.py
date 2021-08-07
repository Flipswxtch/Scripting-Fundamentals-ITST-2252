#!/usr/bin/env python  #What is this line for? Watch the SHEBANG video in lesson 01

# FILE:2252_KennedyK_Lesson4#_InLab.py
# NAME: RockPaperScissors.py
# AUTHOR(s): Kevin Kennedy
# DATE: 07/07/2021
# PURPOSE: A fun game of rock, paper, scissors vs the computer!

#print out more description for use:
lineBreak = "#"*60
print(lineBreak, "\n\n")



#Script main body
import random

# Create a function here so that it can be imported into another module for 
# whatever reason. Return name of user so it can be used in the next function.
def introductory_statements():
    """Prints out an introductory statement to the user detailing what the program is
    and how scoring takes place. Also obtains the user's name through input and 
    returns it for later use.
    """
    print("\n\nLet's play rock, paper, scissors! You will be facing off against the" \
    " computer. Each consecutive round will add to each player's score." \
    " Please answer the following prompts.")
    first_name_of_user = input("Please enter your first name: ").title()
    return first_name_of_user

# Core code of the game itself.
def rock_paper_scissors():
    """Contains the logic of the rock, paper, scissors game. Establishes loop 
    for user to play multiple rounds. Also contains input validation loop.
    Contains variables used for keeping track of rounds played, rounds ending in
    a draw, user's score, and computer's score. 
    """
    first_name_of_user
    user_wants_to_play = True
    user_score = 0
    computer_score = 0
    rounds_played = 1
    rounds_ending_in_draw = 0

    # Establish a while loop to allow a user to play as many rounds as they like.
    while user_wants_to_play == True:

        # Validate user input as long as they enter rock, paper, or scissors.
        user_input_is_valid = False
        while user_input_is_valid == False:
            user_choice = input("Please enter your choice of either rock, paper, or scissors: ").lower()
            if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
                user_input_is_valid = True
            else:
                print(f"Your response of {user_choice} isn't valid, please try again.\n")
        
        # Establish whether the computer chooses rock, paper, or scissors by
        # assigning each respective choice to potential integers randomly generated.
        computer_choice = random.randint(1, 3)
        if computer_choice == 1:
            computer_choice = "rock"
        elif computer_choice == 2:
            computer_choice = "paper"
        elif computer_choice == 3:
            computer_choice = "scissors"

        #Create print statements for when computer or user wins.
        computer_wins = f"The computer wins! The computer chose {computer_choice}."
        user_wins = f"{first_name_of_user} wins! The computer chose {computer_choice}."

        # Iterate through each potential outcome. Add round score to user or computer
        # and print respective winner statement.
        if computer_choice == user_choice:
            rounds_ending_in_draw += 1
            print(f"Unfortunately, you both chose {user_choice} so there is no winner this round!")
        elif computer_choice == "rock":
            if user_choice == "paper":
                user_score += 1
                print(user_wins)
            elif user_choice == "scissors":
                computer_score += 1
                print(computer_wins)
        elif computer_choice == "paper":
            if user_choice == "rock":
                user_score += 1
                print(user_wins)
            elif user_choice == "scissors":
                user_score += 1
                print(user_wins)
        elif computer_choice == "scissors":
            if user_choice == "rock":
                user_score += 1
                print(user_wins)
            elif user_choice == "paper":
                computer_score += 1
                print(computer_wins)
        
        # Ask if user would like to play again and perform input validation.
        user_input_is_valid = False
        while user_input_is_valid == False:
            user_continue_response = input("\nWould you like to play again, Y/N? ").lower()
            if user_continue_response == "y" or user_continue_response == "n":
                user_input_is_valid = True
            else:
                print(f"'{user_continue_response}' is not valid, please enter 'Y' or 'N'.")

        # If user doesn't want to play another round, print round count, and score 
        # of user and computer and exit loop. If user wants to play, restart the loop.
        if user_continue_response == "n":
            print(f"\nRounds played: {rounds_played}\nRounds Ending in Draw: {rounds_ending_in_draw}")
            print(f"Computer's score: {computer_score}\n{first_name_of_user}'s score: {user_score}")
            print("Thank you for playing my rock, paper, scissors game!")
            user_wants_to_play = False                
        else:
            rounds_played += 1
            print(f"Okay, we'll play another round!")
            print(f"Computer's score: {computer_score}\n{first_name_of_user}'s score: {user_score}\n\n")






# Make sure program doesn't run when it's imported into another module
if __name__ == "__main__":
    first_name_of_user = introductory_statements()
    rock_paper_scissors()

print("\n\n", lineBreak)



#Keep shell window/script open:
print(input('\n\nHit Enter to Close\n'))



