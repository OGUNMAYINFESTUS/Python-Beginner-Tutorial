# Create an empty shopping list
shopping_list = []

# Creat a function for adding items to the list.
def add_item():
    item = input("What items do you want to buy? ")
    shopping_list.append(item)
    print(shopping_list)
# A loop for running the "add_item()" function five times.
for i in range(5):
    add_item()

