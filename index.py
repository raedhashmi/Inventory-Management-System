import msvcrt
class main:
    items = []

    while True:
        print("\033[93m" + "What's on your mind? (Navigation keys: 1-5)" + "\033[0m")
        options = [
            "1. Add an item",
            "2. Edit an item record",
            "3. View all items",
            "4. Delete an item record",
            "5. Exit"
        ]
        print("\n".join(options))
        key = msvcrt.getch()

        if key == b'1':  # Option 1
            print("\033[93m" + "Add an item" + "\033[0m")
            import uuid
            itemID = uuid.uuid4()
            itemName = str(input("Enter item name: "))
            itemQuantity = int(input("Enter item quantity: "))
            items.append({"id": itemID, "name": itemName, "quantity": itemQuantity})
            print("Item '" + itemName + "' has been added")
        elif key == b'2':  # Option 2
            print("\033[93m" + "Edit an item record" + "\033[0m")
            findItemName = str(input("Enter item name: "))
            for item in items:
                if item["name"] == findItemName:
                    newItemName = str(input("Enter new item name: "))
                    newItemQuantity = int(input("Enter new item quantity: "))
                    item["name"] = newItemName
                    item["quantity"] = newItemQuantity
                    print("Item '" + newItemName + "' has been edited")
                    break
            else:
                print("Item not found")
        elif key == b'3':  # Option 3
            print("\033[93m" + "View all items" + "\033[0m")
            for item in items:
                print("\033[94m" + "Item Name: " + item["name"] + "\033[0m")
                print(" Item ID: " + str(item["id"]))
                print(" Item Quantity: " + str(item["quantity"]))
        elif key == b'4':  # Option 4
            print("\033[93m" + "Delete an item record" + "\033[0m")
            findItemName = str(input("Enter item name to delete: "))
            for item in items:
                if item["name"] == findItemName:
                    items.remove(item)
                    print("Item '" + findItemName + "' has been deleted")
                    break
            else:
                print("Item not found")
        elif key == b'5':  # Exit
            break

