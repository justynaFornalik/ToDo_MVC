import sys
import os
from model import *


def print_ui():
    with open('user_interface.txt') as user_ui:
        for line in user_ui:
            print (line)


def main():
    my_list = ToDoList()
    while True:
        print_ui()
        user_choice = input("Select action(1 - 7): ")
        if user_choice == "1":
            my_list.__str__()
        elif user_choice == "2":
            my_list.add_item()
        elif user_choice == "3":
            my_list.mark_chosen_item()
        elif user_choice == "4":
            my_list.remove_item()
        elif user_choice == "5":
            my_list.modify_item()
        elif user_choice == "6":
            my_list.display_items_details()
        elif user_choice == "7":
            sys.exit()
        else:
            print("Invalid command!")

if __name__ == '__main__':
    main()

