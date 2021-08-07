# quantity of ingredients required to produce 9 brownies
butter = .5
eggs = 2
vanilla = 1
sugar = 1
flour = .5
cocoa_powder = .5
baking_powder = .25
salt = .25
brownies_from_original_recipe = 9

number_of_brownies_desired = int(input("Please enter the number of brownies you would like baked: "))

#Divide the number of brownies the user would like to make by the number of brownies
#the original recipe provides.
ingredient_change = number_of_brownies_desired / brownies_from_original_recipe

#multiply quanity of ingredient in original recipe by the number found above to get 
#the required amount of ingredients for the amount of brownies the user desires.
butter = butter * ingredient_change
eggs = eggs * ingredient_change
vanilla = vanilla *ingredient_change
sugar = sugar * ingredient_change
flour = flour * ingredient_change
cocoa_powder = cocoa_powder * ingredient_change
baking_powder = baking_powder * ingredient_change
salt = salt * ingredient_change 

print("To make", number_of_brownies_desired, "brownies, you will need the following ingredients:")

#I know we did not learn f strings in this week's lesson, but I find them to be so much easier
#than the alternative!
print(f" {butter} cup butter\n {eggs} eggs\n {vanilla} teaspoon vanilla\n \
{sugar} cup sugar\n {flour} cup flour\n {cocoa_powder} cup cocoa powder\n \
{baking_powder} teaspoon baking powder\n {salt} teaspoon salt")