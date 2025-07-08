from behave import given, when, then
from todo_list import todo_list, Task

# Define a list to represent the to-do list
to_do_list = todo_list

# Step 1: Given the to-do list is empty
@given('the to-do list is empty')
def step_impl(context):
    # Set the to-do list as an empty List
    global to_do_list
    to_do_list.clear()

# Step 2: When the user adds a task "Buy groceries"
@when('the user adds a task "{text}"')
def step_impl(context, text):
    # Add the task to the to-do list
    global to_do_list
    to_do_list.append(Task(text, text, "", "Pendiente"))

# Step 3: Then the to-do list should contain "Buy groceries"
@then('the to-do list should contain "{text}"')
def step_impl(context, text):
    # Check if the task is in the to-do list
    assert Task(text, text, "", "Pendiente") in to_do_list, (
        f'Task "{text}" not found in the to-do list'
    )
