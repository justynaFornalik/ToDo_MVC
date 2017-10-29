import sys
from controller import *


def main ():

    list_of_items = ToDoList()
    while True:
        print("Welcome to our ToDo App")
        print("Select option: ")
        print("Add ToDo item: 1\nModify item: 2\n Delete item: 3\nMark item as done: 4\nDisplay items' list: 5\nDisplay sepcific ToDo item's details: 6\nExit: 0\n"
        option = input("Your choice: ")
        if option == "1":
            add_ToDo_item()
            print(list_of_items)
        elif option == "2":
            print(list_of_items)
            id = int(input("Select the item to delete. The item's id: "))
            delete_item(id)
            print("The item has been successfully deleted.")
            print(list_of_items)
        elif 
        
    