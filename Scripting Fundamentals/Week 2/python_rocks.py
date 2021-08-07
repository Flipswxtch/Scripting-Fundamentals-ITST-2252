guest_height = int(input("Please enter the guests height in inches: "))

if guest_height < 30:
    print("You are in the Guppy tier and your ticket is free!")
elif 36 > guest_height >= 30:
    print("You are in the Pollywod tier and your ticket is $2!")
elif 42 > guest_height >= 36:
    print("You are in the Apprentice tier and your ticket is $5!")
elif 48 > guest_height >= 42:
    print("You are in the Explorer tier and your ticket is $8!")
elif guest_height >= 48:
    print("You are in the Adventurer tier and your ticket is $10!")

print(input("\n\nPlease press enter to close"))