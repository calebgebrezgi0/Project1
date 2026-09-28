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
            print("Invalid\n")


def remove_item(grocery_list):
    view_list(grocery_list)
   