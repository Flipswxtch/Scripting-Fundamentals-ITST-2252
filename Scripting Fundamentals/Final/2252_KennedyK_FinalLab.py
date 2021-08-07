#!/usr/bin/env python  #What is this line for? Watch the SHEBANG video in lesson 01

# FILE:2252_KennedyK_FinalLab.py  
# NAME: RandomFactGuessingGame.py
# AUTHOR(s): Kevin Kennedy
# DATE: 08/03/2021
# PURPOSE: Provides a random fact related question to a user and then prompts 
# them for an answer. Displays the proper answer
# Credit for the final five questions: https://bestlifeonline.com/random-obscure-facts/

import random

lineBreak = "#"*60
print(lineBreak, "\n\n")

# dictionary with questions as the keys and answers as the values.
trivia_questions_and_answers = {
"How many computer-generated effects were used in the " \
"movie Lord of the Rings - Return of the King?\na) 540\nb) 799\nc) 1205\nd) 1488"
: "d) 1488",
"In the movie 'The Blues Brothers', what does Jake order at the diner?" \
"\na) A medium pizza with pineapple and ham\nb) 3 cheeseburgers with the works and a tall glass of" \
"milk\nc) 4 fried chickens and a Coke\nd) A bucket of fries and a Pepsi."
: "c) 4 fried chickens and a Coke",
"In The Simpsons, what football team has Homer always wanted to own?" \
"\na) Washington Redskins\nb) Dallas Cowboys\nc) Denver Broncos\nd) Cleveland Browns"
: "b) Dallas Cowboys",
"In the TV show Seinfeld, what did Elaine decide was 'her song'?\na) I am Woman\nb) Desperado\nc) Yesterday\nd) Witchy Woman"
:"d) Witchy Woman",
"Babe Ruth debuted in professional baseball at the age of 19 years old with which team?" \
"\na) Boston Red Sox\nb) New York Yankees\nc) St Louis Browns\nd) Cincinnati Reds"
: "a) Boston Red Sox",
"What color were stop signs originally made in?\na) red\nb) green\nc) yellow\nd) blue"
:"c) yellow",
"What is the hottest temperature recorded on Earth?\na) 200 Fahrenheit\nb) 1000 Fahrenheit" \
"\nc) one million Fahrenheit\nd) 3.6 million Fahrenheit"
: "d) 3.6 million Fahrenheit",
"What Solar System body is currently slowing the rotation of the Earth?\na) The Moon\nb) The Sun" \
"\nc) An astroid\nd) Jupiter"
: "a) The Moon",
"How many licks, on average, does it take to get to the center of a Tootsie Pop?\na) 434\nb) 364 " \
"\nc) 1254\nd) 76" 
: "b) 364",
"What has the largest eyes of any known animal on Earth?\na) Giant Squids\nb) Elephants" \
"\nc) Whales\nd) Hippos"
: " a) Giant Squids",
}

def introduction():
    """ Contains print statements that introduce the player to the program.
    """
    print("Welcome! This program contains a multiple choice quiz of random facts. Your goal " \
    "is to provide the correct answer.")
    print("There are a total of 10 questions, each containing four options.")
    print("Your score, total missed, and the total amount of possible points will be displayed.\n")    

def user_answer_input_validation():
    """ Prompts user for their answer to the trivia question and validates it. Valid
    responses are either capital or lowercase letters of 'a'-'d'.
    """
    letter_options_list = ["a", "b", "c", "d"]
    global user_answer
    input_is_valid = False
    while input_is_valid == False:
        try:
            user_answer = input("What is your chosen answer, 'a', 'b', 'c', or 'd'? ").lower()
        except:
            print("Something unforseen has gone wrong!")
        else:
            if user_answer in letter_options_list:
                input_is_valid = True
            elif user_answer not in letter_options_list:
                print(f"The answer you provided, {user_answer}, is not valid.\n")

def trivia_game():
    """ Iterates over each key in the dictionary and prints it to screen. Compares
    the users answer to the correct answer. Keeps track of total possible points
    and the user's earned points. 
    """
    global user_score
    global score_possible
    global missed_score
    user_score = 0
    score_possible = 0
    for question, answer in trivia_questions_and_answers.items():
        print(question)

        user_answer_input_validation()

        # Compare only the first letter of the answer with the user's answer
        if user_answer == answer[0:1]:
            user_score += 1
            print("That is correct! You've been awarded a point.\n")
        else:
            print(f"That is not correct. The correct answer was {answer}.\n")
        score_possible += 1 
        input("Press enter to continue\n")

    # Prints total possible points, points missed, and user's earned points.
    missed_score = score_possible - user_score
    print("Here are the stats for the previous round:")
    print(f"User's score: {user_score}\nPoints missed: {missed_score}\nPossible score: {score_possible}")

def user_continue_validation():
    """Ask the user if they'd like to be quizzed again and validate their response.
    Requires the answer to be 'Y', 'N', 'y', or 'n'.
    """
    user_input_is_valid = False
    while user_input_is_valid == False:
        user_response = input("Would you like to be quizzed again, Y/N? ").lower()
        if user_response == "y" or user_response == "n":
            user_input_is_valid = True
            return user_response
        else:
            print("The input you entered isn't valid. Enter 'y' or 'n'.\n")

def main():
    """ Core logic of the function that contains the outer loop dictating whether
    the user gets quizzed again or not. Also calls other functions as needed.
    """
    introduction()

    user_wants_to_play = True
    while user_wants_to_play == True:
        trivia_game()

        user_response = user_continue_validation()
        if user_response == "n":
            user_wants_to_play = False
            print("Thank you for playing!")

# Do not run if program is imported
if __name__ == "__main__":
    main()

print("\n\n", lineBreak)