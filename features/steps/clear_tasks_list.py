from behave import given, when, then
from todo_list import todo_list, Task, limpiar_lista

# Define a list to represent the to-do list
to_do_list = todo_list

# Step 1: Given the to-do list contains tasks
@given('the to-do list contains tasks:')
def step_impl(context):
    # Set the to-do list as an empty List
    global to_do_list
    for row in context.table:
        to_do_list.append(Task(row['Task'], row['Task'], "", "Pendiente"))

# Step 2: When the user clears the to-do list
@when('the user clears the to-do list')
def step_impl(context):
    # Clear the to-do list
    limpiar_lista(to_do_list)

# Step 3: Then the to-do list should be empty
@then('the to-do list should be empty')
def step_impl(context):
    # Check if the to-do list is empty
    assert len(to_do_list) == 0, "The to-do list is not empty"
    # Optionally, you can also print a message
    print("The to-do list has been cleared successfully.")
