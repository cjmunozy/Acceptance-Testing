Feature: add a task

  Scenario: add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"
 
  Scenario: list all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task |
      | Buy groceries |
      | Pay bills |
    When the user lists all tasks
    Then the output should contain:
      Tasks:
      - Buy groceries
      - Pay bills

  Scenario: : mark a task as completed
    Given the to-do list contains tasks:
      | Task | Status |
      | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed
  
  Scenario: : : clear the entire to-do list
    Given the to-do list contains tasks:
      | Task |
      | Buy groceries |
      | Pay bills |
    When the user clears the to-do list
    Then the to-do list should be empty