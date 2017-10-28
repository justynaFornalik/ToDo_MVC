from model import *

list_of_items = ToDoList()


def add_ToDo_item():
    name = input("Enter name: ")
    description = input("Enter description: ")
    new_item = ToDoItem(name, description)
    list_of_items.tasks.append(new_item)
    print(list_of_items.tasks)
      
add_ToDo_item()

