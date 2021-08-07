#!/usr/bin/env python  #What is this line for? Watch the SHEBANG video in lesson 01

# FILE:2252_KennedyK_Lesson7#_InLab.py  
# NAME: WorldSeriesWinningYears.py
# AUTHOR(s): Kevin Kennedy
# DATE: 7/30/2021
# PURPOSE: Prints out the years a team won the World Series. The team is chosen by
# a user through input.

lineBreak = "#"*60
print(lineBreak, "\n\n")

def introductory_statements():
    print("Hello, this program will provide the amount of total World Series wins"\
    " and the years that were won for a team that you enter. ")
    print("You must enter the full name, i.e., Chicago Cubs, New York Giants.")
    print("**Note: You can also enter 'No Winner'\n")

def create_team_and_year_lists():
    """Creates lists that store years and team names. 
    """
    global list_of_teams
    global list_of_years
    world_series_winners = open("WorldSeriesWinners.txt")
    list_of_teams = []
    list_of_years = []
    line_index = 1
    for line in world_series_winners.readlines():
        if line_index % 2 == 0:
            list_of_years.append(line.strip())
        else:
            list_of_teams.append(line.strip().lower())
        line_index += 1

def team_input_validation():
    """This function prompts the user for the name of a team and provides some
    validation.
    """
    global user_team_choice
    is_valid_input = False
    while is_valid_input == False:
        try:
            user_team_choice = input("Please enter the name of a team: ").lower()
        except:
            print("Something unforseen has gone wrong!")
        else:
            if user_team_choice in list_of_teams:
                is_valid_input = True
            elif user_team_choice not in list_of_teams:
                print(f"'{user_team_choice}' is not a valid team.")            

def get_matching_years():
    """A function that goes through the list of teams and compares the users choice
    to each item in the list. If the users choice matches then an index number is
    saved. This index number is then used to pull the respective years a team has won.
    """
    list_index = 0
    indexes_of_matching_team = []
    # Checks to find the indexes where the user's chosen team matches a team 
    # name in the list of teams. Appends the index number to a list of indexes.
    for team in list_of_teams:
        if team == user_team_choice:
            indexes_of_matching_team.append(list_index)
            list_index += 1
        else:
            list_index += 1
            continue
        
    list_of_matching_years = []
    # Pull out each year associated with the indexes found above.
    for index in indexes_of_matching_team:
        list_of_matching_years.append(list_of_years[index])
    
    # Change wording of output depending upon if there was a winner or not.
    if user_team_choice != "no winner":
        print(f"\nTotal number of World Series wins: {len(list_of_matching_years)}")
        print(f"Years the {user_team_choice.title()} won:", end = " ")
    elif user_team_choice == "no winner":
        print(f"\nTotal number of years with no winner: {len(list_of_matching_years)}")
        print(f"The years there was no winner are: ")

    # Format the output of years appropriately.
    for year in list_of_matching_years:
        if year in list_of_matching_years[:-1]:
            print(year, end = ", ")
        else:
            print(year)

def play_again_validation():
    """Ask user if they want to play again and validate the input. The input
    must be 'Y', 'y', 'N', or 'n'.
    """
    user_input_is_valid = False
    while user_input_is_valid == False:
        user_response = input("\nWould you like to input another team, Y/N? ").lower()
        if user_response == "y" or user_response == "n":
            user_input_is_valid = True
            return user_response
        else:
            print(f"The input you entered, {user_response}, is not valid. Try again.\n")

def main():
    """This function contains an outer loop that dictates whether a player plays
    multiple times. It also calls all other functions as needed.
    """
    introductory_statements()
    create_team_and_year_lists()

    user_play_again = True
    while user_play_again == True:
        team_input_validation()
        get_matching_years()

        user_response = play_again_validation()
        if user_response == "n":
            user_play_again = False
            print("Thank you for using my program!")
            print("\n\n", lineBreak)

# Make sure program doesn't run if imported.
if __name__ == "__main__":
    main()