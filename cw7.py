grocery_list = ["milk", "bread", "eggs"]
def add_item(item):
    grocery_list.append(item)
def remove_item(item):
    grocery_list.pop()
def show(item):
    print("Item:", item)
show = lambda item: print("Item:", item)
def count_characters(items):
    if items == []:
        return 0
    return len(items[0]) + count_characters(items[1:])
print("Total characters:", count_characters(grocery_list))
