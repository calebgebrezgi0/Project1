def add_item(grocery_list):
    name = input("Item name: ")
    quantity = int(input("Quantity: "))
    item = {"name": name, "quantity": quantity, "checked": False}
    grocery_list.append(item)
    print("Added " + name + "\n")

def view_list(grocery_list):
    if len(grocery_list) == 0:
        print("List is empty.\n")