item_1_price = input("Please enter the price of the first item: ")
item_2_price = input("Please enter the price of the second item: ")
item_3_price = input("Please enter the price of the third item: ")

#since input is saved as a string, convert all prices to integers for addition
#to occur.
subtotal = int(item_1_price) + int(item_2_price) + int(item_3_price)

#both of the below statements do arithmetic while truncating the resulting
#number to two decimal places.
tax_on_subtotal = f"{subtotal * .065:.2f}"
tip = f"{(float(tax_on_subtotal) + subtotal) * .15:.2f}"
total_amount_to_be_paid = f"{subtotal + float(tax_on_subtotal) + float(tip):.2f}"

#truncate the subtotal to have 2 decimal places.
subtotal = f"{subtotal:.2f}"

print()
print(f"The subtotal of all three items is ${subtotal}.")

print(f"The total amount of tax to be collected is ${tax_on_subtotal}.")
print(f"The total amount to be tipped is ${tip}.")
print(f"The total amount the customer must pay is ${total_amount_to_be_paid}.")

print(input('\n\nHit Enter to Close\n'))