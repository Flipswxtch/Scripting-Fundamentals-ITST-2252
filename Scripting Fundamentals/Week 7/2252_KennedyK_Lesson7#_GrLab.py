#!/usr/bin/env python  #What is this line for? Watch the SHEBANG video in lesson 01

# FILE:2252_KennedyK_Lesson7#_GrLab.py  
# NAME: RandonNumberStatistics.py
# AUTHOR(s): Kevin Kennedy
# DATE: 7/30/2021
# PURPOSE: Creates a file with read and write permissions. Then a number of random 
# integers are generated and written to the file. After this occurs, the lines of the
# file are fetched in order to add them to a list where they will be used to print
# out statistics such as minimum, maximum, the sum, and the average.

lineBreak = "#"*60
print(lineBreak, "\n\n")

import random


def introduction():
    """Introduces the user to the program.
    """
    print("Hello, welcome to my program!")
    print("This program will take an integer that you input, create a list which "\
    "contains that many numbers, and will then provide statistical information " \
    "surrounding that list of numbers.")

def number_input_validation():
    """Validates users input when asking for the quantity of numbers to generate.
    """
    global quantity_of_numbers
    is_valid_input = False
    while is_valid_input == False:
        try:
            quantity_of_numbers = int(input("\nPlease enter the quantity of numbers" \
            " you would like to generate: "))
            is_valid_input = True
            break
        except ValueError:
            is_valid_input = False
            print("That is not an integer. Please enter an appropriate answer.")

def create_random_number_file():
    """Create's a file with read and write permissions. The random numbers are 
    generated here, converted to a string with a new line at the end, 
    and are then written to the file.
    """
    random_number_file = open("numbers.txt", "w+")
    for number in range(1, quantity_of_numbers + 1):
        random_number = random.randint(0, 100)
        random_number = str(random_number) + "\n"
        random_number_file.write((random_number))
    random_number_file.close()

def generate_list_from_file():
    """This function pulls the numbers from the numbers.txt file and puts them
    into a list for later use.
    """
    random_number_list = []
    random_number_file = open("numbers.txt")
    for line in random_number_file:
        line = int(line.strip())
        random_number_list.append(line)
    random_number_file.close()
    return random_number_list


def list_min_and_max():
    """Generate and print the min and max of the list.
    """
    random_number_list = generate_list_from_file()
    print(f"List of numbers: {random_number_list}")
    print(f"Min: {min(random_number_list)}")
    print(f"Max: {max(random_number_list)}")

def sum_of_list():
    """Generate and print the sum of all elements in the list.
    """
    random_number_list = generate_list_from_file()
    global list_sum
    list_sum = 0
    for number in random_number_list:
        list_sum += number
    print(f"Sum: {list_sum}")


def average_of_list():
    """Generate and print the average of the generated list.
    """
    random_number_list = generate_list_from_file()
    list_average = list_sum / len(random_number_list)
    print(f"Average: {list_average:.2f}")

def play_again_validation():
    """Ask user if they want to play again and validate the input. The input
    must be 'Y', 'y', 'N', or 'n'.
    """
    user_input_is_valid = False
    while user_input_is_valid == False:
        user_response = input("Would you like to go again, Y/N? ").lower()
        if user_response == "y" or user_response == "n":
            user_input_is_valid = True
            return user_response
        else:
            print(f"The input you entered, {user_response}, is not valid. Try again.\n")

def main():
    """Core of the program where all other functions are called. Contains the outer
    loop that dictates how long a user plays.
    """
    introduction()

    user_wants_to_play = True
    while user_wants_to_play == True:
        number_input_validation()

        create_random_number_file()
        list_min_and_max()
        sum_of_list()
        average_of_list()

        user_response = play_again_validation()
        if user_response == "n":
            user_wants_to_play = False
            print("Thank you for using this program!")


if __name__ == "__main__":
    main()

print("\n\n", lineBreak)



#Keep shell window/script open:
print(input('\n\nHit Enter to Close\n'))