from model import *

list_of_items = ToDoList()


def add_ToDo_item():
    name = input("Enter name: ")
    if len(name) > 20:
            raise ValueError("Name can't be longer than 20 characters")
    description = input("Enter description: ")
    if len(description) > 150:
            raise ValueError("Description can't be longer than 150 characters")
    new_item = ToDoItem(name, description)
    list_of_items.tasks.append(new_item)
    return list_of_items


def modify_item(id):
    item_to_modify = list_of_items[id]
    new_name = input("Enter new name: ")
    new_description = input("Enter new description")
    item_to_modify.name = new_name
    item_to_modify.description = new_description
    return item_to_modify


def delete_item(id):
    list_of_items.pop(id)
    return list_of_items





