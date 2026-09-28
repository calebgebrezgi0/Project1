MENU = ("Add item", "View list", "Check off item", "Remove item", "Quit")


def add_item(grocery_list):
    name = input("Item name: ")
    quantity = int(input("Quantity: "))
    item = {"name": name, "quantity": quantity, "checked": False}
    grocery_list.append(item)
    print("Added " + name + "\n")


def view_list(grocery_list):
    if len(grocery_list) == 0:
        print("List is empty.\n")
    else:
        number = 1
        for item in grocery_list:
            if item["checked"]:
                mark = "[x]"
            else:
                mark = "[ ]"
            print(number, mark, item["name"], "x" + str(item["quantity"]))
            number += 1
        print()


def check_item(grocery_list):
    view_list(grocery_list)
    if len(grocery_list) > 0:
        number = int(input("Number to check off: "))
        if 1 <= number <= len(grocery_list):
            grocery_list[number - 1]["checked"] = True
            print("Checked off!\n")
        else:
            print("Invalid.\n")


def remove_item(grocery_list):
    view_list(grocery_list)
    if len(grocery_list) > 0:
        number = int(input("Number to remove: "))
        if 1 <= number <= len(grocery_list):
            grocery_list.pop(number - 1)
            print("Removed!\n")
        else:
            print("Invalid.\n")


def main():
    grocery_list = []
    running = True

    while running:
        print("=== Grocery Checklist ===")
        number = 1
        for option in MENU:
            print(str(number) + ". " + option)
            number += 1

        choice = input("Choose 1-5: ")

        if choice == "1":
            add_item(grocery_list)
        elif choice == "2":
            view_list(grocery_list)
        elif choice == "3":
            check_item(grocery_list)
        elif choice == "4":
            remove_item(grocery_list)
        elif choice == "5":
            print("Ending")
            running = False
        else:
            print("Invalid option.\n")


main()
