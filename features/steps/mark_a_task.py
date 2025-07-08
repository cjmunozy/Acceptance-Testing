from behave import given, when, then
from todo_list import todo_list, Task, tachar_tarea

# Define a list to represent the to-do list
to_do_list = todo_list

# Step 1: Given the to-do list contains tasks
@given('the to-do list contains tasks :')
def step_impl(context):
    # Set the to-do list as an empty List
    for row in context.table:
        task = Task(row['Task'], "", "", row['Status'])
        to_do_list.append(task)

# Step 2: When the user marks task "Buy groceries" as completed
@when('the user marks task "{task_name}" as completed')
def step_impl(context, task_name):
    # Find the task in the to-do list
    task = Task(task_name, task_name, "", "Pendiente")
    if task in to_do_list:
        tachar_tarea(task)
    else:
        raise ValueError(f'Task "{task_name}" not found in the to-do list')
