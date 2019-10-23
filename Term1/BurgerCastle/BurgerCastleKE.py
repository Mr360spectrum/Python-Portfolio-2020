# Karter Ence
# Burger Castle
# 10/21/2019

# Initialize a tuple of valid orders
validOrders = ("burger", "fries", "salad", "soda", "milkshake")
# Initialize tuple of descriptions
itemDescriptions = ("Half-pound burger", "Large fries", "Side salad", "Diet root beer", "Chocolate shake")
# Initialize order as empty list
order = []
# Welcome the user and display valid orders
print("Welcome to Burger Castle.")
print("Menu:", validOrders)
print("Please enter each item in your order. Press 'Enter' or type 'quit' on an empty line when done.")

# Keep getting inputs from the user until they quit
while True:
    item = input("Enter item: ")
    if item == "" or item.lower() == "quit":
        break
    # Add the user's inputs to order if it is in validOrders
    elif item in validOrders:
        order.append(item)
    # Tell the user that they do not sell that item if it is not in valid Orders
    else:
        print("Sorry, we don't sell", item)

# Tell the user what they ordered with descriptions
print("Order complete; you are having:")
for item in order:
    # Display the correct description by using the same index from the validOrders
    index = validOrders.index(item)
    description = itemDescriptions[index]
    print(description)
print("Thanks for visiting Burger Castle!")