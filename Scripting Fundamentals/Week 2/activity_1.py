ounces = int(input("Please enter the number of ounces you would like to purchase: "))

#Do arithmetic to convert ounces of cider to both drams and gills.
drams = ounces * 8
gills = ounces / 4

#create two variables that print out a statement and a quantity. Done to lessen the
#amount of code I am to type
cider_in_drams = f"\nAmount of cider in drams: {drams}"
cider_in_gills = f"Amount of cider in gills: {gills}"

#perform some logic based on the amount of drams desired. Print amount of
# drams and gills. Print statements depending on quantity being ordered
if drams > 1024:
    print(cider_in_drams)
    print(cider_in_gills)
    print("That is a large amount of cider! You will need to purchase this amount in gallons.")
elif drams < 100:
    print(cider_in_drams)
    print(cider_in_gills)
    print("The amount of cider you would like to purchase is too small; perhaps you should just order a pint!")
else:
    print(cider_in_drams)
    print(cider_in_gills)
    print(f"Please wait while we get your order ready for you!")

print(input("\n\nPlease press enter to close this program."))