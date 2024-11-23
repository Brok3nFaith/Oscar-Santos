print("Welcome to the Grocery Tracker")
total = 0

# Get the number of items
num_items = int(input("Please enter the number of items you'll be buying: "))

# Collect prices for all items
for i in range(num_items):
    price = float(input("Please enter the price of item " + str(i + 1) + ": "))
    total += price

# Initialize discount
discount = 0

# Check eligibility for discounts
if total >= 100:
    print("You're eligible for a 10% discount!")
    apply_discount = input("Would you like to apply your discount? (y/n): ").strip().lower()
    if apply_discount == 'y':
        discount = total * 0.10
elif total >= 50:
    print("You're eligible for a 5% discount!")
    apply_discount = input("Would you like to apply your discount? (y/n): ").strip().lower()
    if apply_discount == 'y':
        discount = total * 0.05

# Calculate the final amount
subtotal = total - discount
tax = 0.05
tax_amount = subtotal * tax
final_amount = subtotal + tax_amount

# Display results
print("Your total is: $" + str(round(final_amount, 2)))
if discount > 0:
    print("After your discount, your new total amount is: $" + str(round(subtotal, 2)))
    print("You have saved $" + str(round(discount, 2)) + " after your discount!")
