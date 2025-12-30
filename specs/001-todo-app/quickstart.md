# Quickstart Guide: Todo In-Memory Python Console App

## Prerequisites
- Python 3.13 or higher
- No external dependencies required

## Setup
1. Clone or download the repository
2. Navigate to the project directory
3. Ensure Python 3.13+ is installed and accessible from command line

## Running the Application
```bash
python src/todo_app/main.py
```

## Basic Usage
1. The application starts with an empty task list
2. A menu will be displayed with the following options:
   - 1. Add Task
   - 2. View Tasks
   - 3. Update Task
   - 4. Delete Task
   - 5. Mark Task Complete
   - 6. Exit
3. Select an option by entering the corresponding number
4. Follow the prompts for the selected operation

## Feature Walkthrough

### Adding a Task
1. Select option "1. Add Task"
2. Enter the task description (max 256 characters)
3. The task will be added to the list as incomplete
4. You'll return to the main menu

### Viewing Tasks
1. Select option "2. View Tasks"
2. All tasks will be displayed with:
   - Sequential numbering (1, 2, 3...)
   - [ ] for incomplete tasks
   - [x] for completed tasks
   - Task description
3. You'll return to the main menu

### Updating a Task
1. Select option "3. Update Task"
2. Enter the task number to update (as shown in "View Tasks")
3. Enter the new description for the task
4. The task description will be updated while preserving completion status
5. You'll return to the main menu

### Deleting a Task
1. Select option "4. Delete Task"
2. Enter the task number to delete (as shown in "View Tasks")
3. The task will be removed from the list
4. Remaining tasks will maintain sequential numbering
5. You'll return to the main menu

### Marking a Task Complete
1. Select option "5. Mark Task Complete"
2. Enter the task number to mark complete (as shown in "View Tasks")
3. The task's status will be updated to completed
4. The task will now show as [x] when viewing the list
5. You'll return to the main menu

### Exiting the Application
1. Select option "6. Exit"
2. The application will terminate

## Error Handling
- Invalid menu selections will show an error and return to the main menu
- Invalid task numbers will show an error and return to the main menu
- Empty task descriptions will show an error and return to the main menu
- Descriptions over 256 characters will show an error and return to the main menu
- Empty task list operations will show an error and return to the main menu

## Example Session
```
Welcome to the Todo App!
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Exit
> 1
Enter task description: Buy groceries
Task added successfully!

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Exit
> 2
1. [ ] Buy groceries

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Exit
> 5
Enter task number to mark complete: 1
Task marked as complete!

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Exit
> 2
1. [x] Buy groceries

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Exit
> 6
Goodbye!
```