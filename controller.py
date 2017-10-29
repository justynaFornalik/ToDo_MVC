from model import *




def add_ToDo_item():
    name = input("Enter name: ")
    description = input("Enter description: ")
    new_item = ToDoItem(name, description)
    list_of_items.tasks.append(new_item)
    return list_of_items


def modify_item(item):
    new_name = input("Enter new name: ")
    new_description = input("Enter new description")
    item.name = new_name
    item.description = new_description
    return item


def delete_item(id):
    list_of_items.pop(id)
    return list_of_items





