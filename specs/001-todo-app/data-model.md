# Data Model: Todo In-Memory Python Console App

## Task Entity

### Fields
- **id** (int): Sequential identifier assigned when added to the task list (1-indexed)
- **description** (str): Text description of the task (max 256 characters)
- **completed** (bool): Boolean indicating completion status (default: False)

### Relationships
- The Task entity exists independently but is managed within a TaskManager collection

### Validation Rules
- Description must not be empty or contain only whitespace
- Description must not exceed 256 characters
- ID must be positive integer
- Completed status must be boolean

### State Transitions
- New Task: `completed = False` (default)
- Updated Task: `completed` may remain unchanged or be set to `True`
- Completed Task: `completed = True` (via mark complete operation)

## Task Collection

### Structure
- **tasks** (list): Python list containing Task objects in order of addition
- **next_id** (int): Counter for assigning sequential IDs to new tasks

### Operations
- Add Task: Append to list, assign next available ID
- Update Task: Modify description of existing task by ID
- Delete Task: Remove from list by ID, update remaining IDs to maintain sequence
- Mark Complete: Update completed status of existing task by ID
- View Tasks: Return list of all tasks for display

### Constraints
- IDs must remain sequential after any deletion operation
- Empty list is valid state
- Maximum practical size limited by available memory only