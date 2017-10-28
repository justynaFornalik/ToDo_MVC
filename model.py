#     Expected features:

# Add ToDo item consisting of the following attributes:
# name - string, max 20 characters
# description - string, max 150 characters
# is_done - bool, false by default
# Modify item
# allow changing name
# allow changing description
# Delete item
# Mark item as done
# Display items' list
# display id
# display name
#  Display specific todo item's details
# display id
# display name
# display description
# Each action described above should have view.


class ToDoItem():
    name = ""
    description = ""
    is_done = False

    def __init__(self, name, description):
        self.name = name
        self.description = description

        if len(self.name) > 20:
            raise ValueError("Name can't be longer than 20 characters")

        if len(self.description) > 150:
            raise ValueError("Description can't be longer than 150 characters")
    
    def mark_as_done():
        self.is_done = True

    def __str__(self):
        return self.name + "|" + self.description


class ToDoList():
    tasks = []

    def add_new_task_to_tasks(new_task):
        self.notes.append(new_task)

    def __str__(self):
        for item in tasks:
            return str(tasks.index(item)) + "|" + item.__str__() + "\n"

