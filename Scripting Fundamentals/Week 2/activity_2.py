print("Enter two primary colors (red, blue, or yellow) when prompted and I will display the secondary" \
    " color that's made when you mix them.")
    
primary_color_1 = input("\nPlease enter your first color choice: ")

#make sure user input is either red, yellow, or blue, if it's not, print statement.
if primary_color_1.lower() != "red" and primary_color_1.lower() != "yellow" and primary_color_1.lower() != "blue":
    print(f"{primary_color_1} is not a valid option. Please restart the program and enter a valid primary color.")

#if input to first question is allowed, prompt a second time. If user input isn't either
#red, yellow, or blue again, then print statement.
else:
    primary_color_2 = input("Please enter your second color choice: ")
    if primary_color_2.lower() != "red" and primary_color_2.lower() != "yellow" and primary_color_2.lower() != "blue":
        print(f"{primary_color_2} is not a valid option. Please restart the program and enter a valid primary color.")
    
    #if both inputs are valid but are the same, print statement.
    else:
        if primary_color_1.lower() == primary_color_2.lower():
            print("Please restart the program and enter two different primary colors.")
        
        #this block only happens if both inputs are either red, yellow, or blue and they
        #do not match.
        else:
            
            #create a variable that will be printed each time to save some key strokes.
            secondary_color_statement = f"\nThe secondary color of {primary_color_1.lower()} and {primary_color_2.lower()} is"
            
            #perform logic based on colors chosen, will print the appropriate secondary color
            #based upon the primary colors provided by the user.
            if (primary_color_1.lower() == "red" and primary_color_2.lower() =="blue" or 
            primary_color_1.lower() == "blue" and primary_color_2.lower() == "red"):
                print(secondary_color_statement, "Purple!")
            elif (primary_color_1.lower() == "red" and primary_color_2.lower() == "yellow" or
            primary_color_1.lower() == "yellow" and primary_color_2.lower() == "red"):
                print(secondary_color_statement, "Orange!")
            elif (primary_color_1.lower() == "blue" and primary_color_2.lower() == "yellow" or 
            primary_color_1.lower() == "yellow" and primary_color_2.lower() == "blue"):
                print(secondary_color_statement, "Green!")

print(input("\n\nPlease press enter to close this program."))