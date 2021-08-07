#!/usr/bin/env python  #What is this line for? Watch the SHEBANG video in lesson 01

# FILE:2252_KennedyK_Lesson6#_InLab.py  
# NAME: State_abbreviation_guessing_game.py
# AUTHOR(s): Kevin Kennedy
# DATE: 7/20/2021
# PURPOSE: Display a state's abbreviation to a user for them to guess. If they're right
# they get a point. Display amount of points earned and the abbreviations they missed.

lineBreak = "#"*60
print(lineBreak, "\n\n")

import random

states = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
    "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE", 
    "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL",
    "Indiana": "IN", "Iowa": "IA", "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA",
    "Maine": "ME",  "Maryland": "MD", "Massachusetts": "MA", "Michigan": "MI",
    "Minnesota": "MN", "Mississippi": "MS", "Missouri": "MO", "Montana": "MT",
    "Nebraska": "NE", "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ",
    "New Mexico": "NM", "New York": "NY", "North Carolina": "NC", "North Dakota": "ND",
    "Ohio": "OH", "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA",
    "Rhode Island": "RI", "South Carolina": "SC", "South Dakota": "SD", "Tennessee": "TN",
    "Texas": "TX", "Utah": "UT", "Vermont": "VT", "Virginia": "VA",
    "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY"
}

def introduction():
    print("Welcome to my program!")
    print("This program will display an American State's abbreviation, type in the " \
    "full name of the state to earn a point. After each response, you will be prompted " \
    "asking if you would like to continue.")
    print("When you end the game, your user_score and the total possible points will be " \
    "displayed. I will also print the abbreviations that you missed!")


def generate_random_number():
    """Generate a random number that will be used to select a random state.
    """
    global random_number
    random_number = random.randint(0, 50)


def generate_state_list():
    """Generate a list of states using the keys in the states dictionary.
    """
    global state_list
    global correct_state_full
    state_list = []
    for state in states.keys():
        state_list.append(state.lower())
    
    correct_state_full = state_list[random_number]


def generate_abbreviation_list():
    """Generate a list of abbreviations from the states dictionary.
    """
    global abbreviation_list
    global correct_state_abbreviation
    abbreviation_list = []
    for abbreviation in states.values():
        abbreviation_list.append(abbreviation)

    correct_state_abbreviation = abbreviation_list[random_number]
    print(f"\nState abbreviation: {correct_state_abbreviation}")


def state_guess_validation():
    """Takes a user's input regarding their state guess and validates it.
    """
    global user_guess
    user_input_is_valid = False
    while user_input_is_valid == False:
        user_guess = input("Please enter the full name of the state: ").lower()
        if user_guess in state_list:
            user_input_is_valid = True
            return user_guess
        else:
            print("Please enter a valid state.")


def user_continue_validation():
    """Ask the user if they'd like to continue and validate it.
    """
    user_input_is_valid = False
    while user_input_is_valid == False:
        user_response = input("Would you like to keep going, Y/N? ").lower()
        if user_response == "y" or user_response == "n":
            user_input_is_valid = True
            return user_response
        else:
            print("The input you entered isn't valid. Enter 'y' or 'n'.\n")
    

def main():
    """Core logic of the program where all other functions are called. Contains the 
    outer loop that terminates when the user is done playing.
    """
    user_score = 0
    possible_points = 0
    states_user_got_wrong = []

    introduction()

    # Set up outer loop to allow user to play as long as they'd like. Run various 
    # functions to set up gameplay.
    user_wants_to_play = True
    while user_wants_to_play == True:
        generate_random_number()
        generate_state_list()
        generate_abbreviation_list()
        state_guess_validation()


        # Check if user's answer is right. Perform logic whether it is right or wrong.
        if user_guess.lower() == correct_state_full.lower():
            user_score += 1
            possible_points += 1
            print("Nice job, that's correct!\n")
        else:
            possible_points += 1
            states_user_got_wrong.append(correct_state_abbreviation)
            print(f"Sorry, that's incorrect! The right answer was {correct_state_full}.\n")


        # If user answers 'n' to continuing, print out stats related to their session.
        user_response = user_continue_validation()
        if user_response == "n":
            user_wants_to_play = False
            print("Thank you for playing! Here are the stats:")
            print(f"Correct responses: {user_score}\nIncorrect Responses: {possible_points - user_score}")
            print(f"Possible points: {possible_points}")
            print(f"Incorrect states: ", end = "")
            for abbreviation in states_user_got_wrong:
                if abbreviation != states_user_got_wrong[-1]:
                    print(abbreviation, end = ", ")
                else:
                    print(abbreviation)

# Make sure program doesn't run if imported.
if __name__ == "__main__":
    main()

print("\n\n", lineBreak)

#Keep shell window/script open:
print(input('\n\nHit Enter to Close\n'))