from behave import given, when, then
from todo_list import todo_list, Task, listar_tareas

# Define a list to represent the to-do list
to_do_list = todo_list

# Define a string to hold the output of the task listing
output = ""

# Step 1: Given the to-do list contains tasks
@given('the to-do list contains tasks')
def step_impl(context):
    # Set the to-do list as an empty List
    for row in context.table:
        to_do_list.append(Task(row['Task'], row['Task'], "", "Pendiente"))

# Step 2: When the user lists all tasks
@when('the user lists all tasks')
def step_impl(context):
    # List all tasks in the to-do list
    global output
    output = listar_tareas()

# Step 3: Then the output should contain all the tasks
@then('the output should contain "{text}"')
def step_impl(context, text):
    # Check if the task is in the to-do list
    assert text == output, (
        f'Task "{text}" not found in the output'
    )
