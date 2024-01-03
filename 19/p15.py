def print_sL(sL):
    print("Shopping List:")
    for i, item in enumerate(sL, start=1):
        print(f"{i}. {item}")

def add_item(sL, item):
    sL.append(item)
   

def remove_item(sL, item):
    if item in sL:
        sL.remove(item)
        print(f"{item} removed from the shopping list.")
    else:
        print(f"{item} not found in the shopping list.")

sL = []

while True:
    print_sL(sL)
    print("\nMenu:")
    print("1. Add item to the shopping list")
    print("2. Remove item from the shopping list")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        new_item = input("Enter the item to add: ")
        add_item(sL, new_item)
    elif choice == '2':
        item_to_remove = input("Enter the item to remove: ")
        remove_item(sL, item_to_remove)
    elif choice == '3':
        print("Exiting the program. Final shopping list:")
        print_sL(sL)
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
