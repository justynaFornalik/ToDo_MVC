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

        
        
    
    def mark_as_done():
        self.is_done = True

    def __str__(self):
        return "|" + self.name + "|" + self.description + "|" 


class ToDoList():
    tasks = []

    def add_new_task_to_tasks(new_task):
        self.notes.append(new_task)

    def get_list(self):
        return self.tasks

    def __str__(self):
        tasks_list = self.get_list()
        for item in tasks_list:
            print(str(tasks_list.index(item)) + "|" + item.name + "\n")

    def __getitem__(self,index):
        return self.tasks[index]



