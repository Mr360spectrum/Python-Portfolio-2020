# Karter Ence
# Burger Castle
# 10/21/2019

validOrders = ("burger", "fries", "salad", "soda", "milkshake")
itemDescriptions = ("Half-pound burger", "Large fries", "Side salad", "Diet root beer", "Chocolate shake")
order = []
print("Welcome to Burger Castle.")
print("Menu:", validOrders)
print("Please enter each item in your order. Press 'Enter' or type 'quit' on an empty line when done.")

while True:
    item = input("Enter item: ")
    if item == "" or item.lower() == "quit":
        break
    elif item in validOrders:
        order.append(item)
    else:
        print("Sorry, we don't sell", item)

print("Order complete; you are having:")
for item in order:
    index = validOrders.index(item)
    description = itemDescriptions[index]
    print(description)
print("Thanks for visiting Burger Castle!")