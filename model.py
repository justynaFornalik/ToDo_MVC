class ToDoItem():
    name = ""
    description = ""
    is_done = False

    def __init__(self, name, description):
        if not type(name) != str and type(description) != str:
            raise ValueError

        self.name = name
        self.description = description

    def mark(self):
        self.is_done = True

    def __str__(self):
        is_done_sign = "[ ]"
        if self.is_done:
            is_done_sign = "[x]"

        return self.name + "|" + self.description + "|" + is_done_sign + "|" + "\n" 


class ToDoList():
    def __init__(self):
        items_list = []
        self.items_list = items_list

    def __str__(self):
        items_info = ""
        for item in self.items_list:
            items_info = items_info + str(self.items_list.index(item)) + "|" + item.__str__() 
        print(items_info) 

    def get_list(self):
        return self.items_list

    def add_item(self):
        name = input("Enter name: ")
        if len(name) > 20:
            raise ValueError("Name can't be longer than 20 characters")
        description = input("Enter description: ")
        if len(description) > 150:
            raise ValueError("Description can't be longer than 150 characters")
        new_item = ToDoItem(name, description)
        self.items_list.append(new_item)
        return self.items_list

    def remove_item(self):
        """Removes TodoItem object from index of list items_list"""
        index = int(input("Select the item to delete. The item's id: "))
        if index <= len(self.items_list)-1:
            self.items_list.pop(index)
            print("You successfully deleted the item!")
        else:
            print("id out of range!")
        return self.items_list

    def modify_item(self):
        index = int(input("Select the item to modify. The item's id: "))
        if index <= len(self.items_list)-1:
            item_modified = self.items_list[index]
            new_name = input("Enter new name: ")
            if len(new_name) > 20:
                raise ValueError("Name can't be longer than 20 characters")
            new_description = input("Enter new description: ")
            if len(new_description) > 150:
                raise ValueError("Description can't be longer than 150 characters")
            item_modified.name = new_name
            item_modified.description = new_description
            print("You successfully modified the item!")     
        else:
            print("id out of range!")
        return self.items_list

    def mark_chosen_item(self):
        index = int(input("Select item to mark as done. The item's id: "))
        if index <= len(self.items_list)-1:
            item_to_mark = self.items_list[index]
            item_to_mark.mark()
            print("You successfully marked the item as done!")
        else:
            print("id out of range!")

        return self.items_list

    def display_items_details(self):
        index = int(input("Select the item to display. The item's id: "))
        if index <= len(self.items_list)-1:
            item_to_display = self.items_list[index]
            print(item_to_display.__str__())
        else:
            print("id out of range!")



