def add_menu(menus):
    name = input("Enter name of item: ")
    price = input("Enter price of item: ")

    menu = {"name": name, "price": price}

    menus.append(menu)
    print("Menu added successfully!")


def edit_menu(menus):
    name = input("Enter name you wanna edit: ")
    found = False

    for menu in menus:
        if menu["name"].lower() == name.lower():
            print("Select item to edit: ")
            print("1. Name\n2. Price")
            choice = int(input("Enter your choice"))

            if choice == 1:
                new_item = input("Enter new item: ")
                menu["name"] = new_item
            elif choice == 2:
                new_price = input("Enter new price: ")
                menu["price"] = new_price
            else:
                print("Invalid choice!!")
                return

            print("Item editted successfully!")
            found = True
            break

    if not found:
        print("Item not found")


def remove_item(menus):
    name = input("Enter item name to remove: ")
    found = False

    for menu in menus:
        if menu["name"].lower() == name.lower():
            menus.remove(menu)
            print("Contact removed successfully!")
            found = True
            break
    if not found:
        print("Item not found.")


def search_menu(menus):
    search_item = input("Enter item name to serch: ")
    found_menu = []
    for menu in menus:
        if search_item.lower() in menu.values():
            found_menu.append(menu)

    if found_menu:
        print("Search menu:")
        display_menu(found_menu)

    else:
        print("item not found!")


def display_menu(menus):
    for menu in menus:
        print(menu["name"], menu["price"])

        print()


def list_all_menu(menus):
    if menus:
        print("Menu items:")
        display_menu(menus)
    else:
        print("Items not found!!")


def manage_menus():
    menus = [
        {"name": "Items", "price": "Price(in Rs)"},
        {"name": "chowmin", "price": "90"},
        {"name": "coffee", "price": "100"},
        {"name": "momos", "price": "120"},
    ]

    while True:
        print(
            "1.Add item\n2.Edit menu\n3.Remove menu\n4.Search menu\n5.Show all items\n6.Exit\n"
        )
        choice = int(input("Enter your choice(1-6):"))

        if choice == 1:
            add_menu(menus)
        elif choice == 2:
            edit_menu(menus)
        elif choice == 3:
            remove_item(menus)
        elif choice == 4:
            search_menu(menus)
        elif choice == 5:
            list_all_menu(menus)
        elif choice == 6:
            print("Exiting....")
            break
        else:
            print("Invalid choice")


manage_menus()
