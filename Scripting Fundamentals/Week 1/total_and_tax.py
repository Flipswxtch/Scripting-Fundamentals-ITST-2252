subtotal = float(input("Please enter the subtotal for your meal: "))

#perform some arithmetic and truncate the resulting answers to two decimals.
tax = f"{subtotal * .065:.2f}"
total_bill = f"{float(tax) + subtotal:.2f}"

#print out the required numbers for subtotal, tax, and the total bill.
print(f"Subtotal: ${subtotal}\nTax: ${tax}\nTotal Bill: ${total_bill}")

print(input('\n\nHit Enter to Close\n'))