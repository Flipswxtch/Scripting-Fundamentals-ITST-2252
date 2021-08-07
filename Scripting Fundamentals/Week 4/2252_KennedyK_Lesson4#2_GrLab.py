#!/usr/bin/env python

# FILE:2252_KennedyK_Lesson4#2_GrLab.py
# NAME: RandomNumberAddition.py
# AUTHOR(s): Kevin Kennedy
# DATE: 07/08/2021
# PURPOSE: Randomly generate two numbers for an addition problem, ask user to add them
# and provide an answer. Congratulate for right answer, scold for bad answer. User
# can play as many times as they like.

#print out more description for use:
lineBreak = "#"*60
print(lineBreak, "\n\n")

import random

# Create function that is used for input validation when the user provides an answer for 
# the addition problem. 
def answer_input_validation():
    """Try Except logic used to validate users answer to addition problem. Answer
    provided must be an integer or they're scolded and reprompted.
    """
    user_input_is_valid = False
    while user_input_is_valid == False:
        try:
            users_answer_to_problem = int(input("\nEnter the answer to the addition problem: "))
            user_input_is_valid = True
            break
        # The ValueError is used because the user must enter an integer. If the 
        # answer given is not an integer, they are scolded and reprompted.
        except ValueError:
            user_input_is_valid = False
            print("That is not an integer. Please enter an appropriate answer.")
    return users_answer_to_problem


# Create a function that is used to validate the users input when responding to
# if they would like to play again. 
def continue_playing_validation():
    """Provides input validation while asking user if they'd like to play again.
    Requires users answer to be 'y' or 'n'.
    """
    user_input_is_valid = False
    while user_input_is_valid == False:
        user_wants_another_problem = input("Would you like another problem, Y/N? ").lower()
        if user_wants_another_problem in ["y", "n"]:
            user_input_is_valid = True
        elif user_wants_another_problem not in ["y", "n"]:
            user_input_is_valid = False
            print(f"The input you entered, '{user_wants_another_problem}', is not valid. Try again.\n")
    return user_wants_another_problem
    

# This is the core code. It contains the logic of the game and calls the two functions
# defined above.
def addition_of_two_random_numbers():
    """Randomly generate two numbers. Asks user to add and provide their answer. Scolds
    user for wrong answer, congratulates for good answer. User is prompted to see if they'd
    like to play again.
    """
    user_wants_to_play = True
    while user_wants_to_play == True:
        print(input("Press enter to generate a problem!"))

        # Generate two random numbers, format the addition problem, and print to screen.
        randomly_generated_number_one = random.randint(1, 500)
        randomly_generated_number_two = random.randint(1, 500)
        answer_to_problem = randomly_generated_number_one + randomly_generated_number_two
        print(" ",randomly_generated_number_one, "\n+", randomly_generated_number_two)
        print("------")

        # This if block only executes if the user provided the correct answer to the problem.
        # Print statement saying user answer is correct. Ask user if they want to play again,
        # perform logic based on if they want to play again.
        users_answer_to_problem = answer_input_validation()
        if users_answer_to_problem == answer_to_problem:
            print("That is correct!\n")
            user_wants_another_problem = continue_playing_validation() 
            if user_wants_another_problem == "n":
                user_wants_to_play = False
                print("Thank you for playing!")
            elif user_wants_another_problem == "y":
                print("Okay, let's play another round!\n")

        # This block executes if user doesn't provide the right answer. Scold them and prompt
        # them to see if they'd like to play again. Perform logic either way.
        else:
            print(f"That is not the correct answer. The right answer is {answer_to_problem}.\n")
            user_wants_another_problem = continue_playing_validation() 
            if user_wants_another_problem == "n":
                user_wants_to_play = False
                print("Thank you for playing!")
            elif user_wants_another_problem == "y":
                print("Okay, let's play another round!\n")

            


# Make sure main program doesn't run if it's imported into another module.
if __name__ == "__main__":
    addition_of_two_random_numbers()

print("\n\n", lineBreak)



#Keep shell window/script open:
print(input('\n\nHit Enter to Close\n'))
