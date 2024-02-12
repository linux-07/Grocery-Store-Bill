shopName = "Arnav's Grocery Market" # Can customize this or can take user input for this
customerName = input("Enter the name of customer: ")
items = {}
total = 0
i = 1
while True:
    itemName = input(f"\nEnter the name of item {i} (press 'q' to end): ")
    if (itemName == 'q'):
        break
    itemPrice = float(input(f"Enter the price of item {i}: "))
    items[itemName] = itemPrice
    total += itemPrice
    i += 1
# Printing the bill
print("\n---------------BILL--------------\n")
print(shopName)
print(f"Name: {customerName.title()}\n")
print("-----------------------")
for item, price in items.items():
    print(f"{item.title()} - {price:.2f}")
print("-----------------------")
print(f"\nTotal Items: {len(items)}")
print(f"Total Cost: {total}")
print("-----------------------")
