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

    def __init__(self, name, description, is_done):
        self.name = name
        self.description = description
        self.is_done = is_done

    def mark_as_done():
        self.is_done = True



class ToDo():
    notes = []

