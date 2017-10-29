import sys
from controller import *


def main():

    #list_of_items = ToDoList()
    while True:
        print("Welcome to our ToDo App")
        print("Select option: ")
        print("Add ToDo item: 1\nModify item: 2\nDelete item: 3\nMark item as done: 4\nDisplay items' list: 5\nDisplay specific ToDo item's details: 6\nExit: 0\n")
        option=input("Your choice: ")
        if option == "1":
            add_ToDo_item()
            print(list_of_items)
        elif option == "2":
            print(list_of_items)
            id = int(input("Select the item to modify. The item's id: "))
            modify_item(id)
            print("The item has been successfully modified.")
            print(list_of_items)
        elif option == "3":
            print(list_of_items)
            id=int(input("Select the item to delete. The item's id: "))
            delete_item(id)
            print("The item has been successfully deleted.")
            print(list_of_items)
        elif option == "4":
            print(list_of_items)
            id = int(input("Select an item to mark as done. The item's id: "))
            item_to_mark_as_done = list_of_items[id]
            item_to_mark_as_done.mark_as_done()
        elif option == "5":
            print(list_of_items.get_list())
        elif option == "6":
            print(list_of_items.__str__())
            id = int(input("Select item's id to see more details: "))
            detailed_item = list_of_items.__getitem__(id)
            print(detailed_item)
        elif option == "0":
            sys.exit()


if __name__ == "__main__":
    main()        

        
    