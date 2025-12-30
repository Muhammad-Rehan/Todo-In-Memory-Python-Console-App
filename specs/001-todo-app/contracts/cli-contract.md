# CLI Interface Contract: Todo In-Memory Python Console App

## Overview
This document specifies the contract for the command-line interface of the Todo application, defining the expected input/output behavior for each operation.

## Common Response Format
All operations return to the main menu after completion or upon error. Error messages follow the format: "Error: [description]" followed by a return to the main menu.

## Operations

### 1. Add Task
**Input**:
- Menu selection: "1"
- Task description: string (1-256 characters)

**Success Output**:
- "Task added successfully!"
- Returns to main menu

**Error Cases**:
- Empty description: "Error: Task description cannot be empty"
- Description too long: "Error: Task description exceeds 256 characters"
- Returns to main menu in all error cases

### 2. View Tasks
**Input**:
- Menu selection: "2"

**Success Output**:
- If tasks exist: List of tasks in format "N. [ ] description" or "N. [x] description"
- If no tasks: "No tasks in the list"
- Returns to main menu

**Error Cases**:
- None - always succeeds

### 3. Update Task
**Input**:
- Menu selection: "3"
- Task number: integer (1-based index)
- New description: string (1-256 characters)

**Success Output**:
- "Task updated successfully!"
- Returns to main menu

**Error Cases**:
- Invalid task number: "Error: Invalid task number"
- Empty description: "Error: Task description cannot be empty"
- Description too long: "Error: Task description exceeds 256 characters"
- Returns to main menu in all error cases

### 4. Delete Task
**Input**:
- Menu selection: "4"
- Task number: integer (1-based index)

**Success Output**:
- "Task deleted successfully!"
- Remaining tasks maintain sequential numbering
- Returns to main menu

**Error Cases**:
- Invalid task number: "Error: Invalid task number"
- No tasks exist: "Error: No tasks to delete"
- Returns to main menu in all error cases

### 5. Mark Task Complete
**Input**:
- Menu selection: "5"
- Task number: integer (1-based index)

**Success Output**:
- "Task marked as complete!"
- Returns to main menu

**Error Cases**:
- Invalid task number: "Error: Invalid task number"
- No tasks exist: "Error: No tasks to mark complete"
- Returns to main menu in all error cases

### 6. Exit
**Input**:
- Menu selection: "6"

**Success Output**:
- "Goodbye!"
- Application terminates

**Error Cases**:
- None - always succeeds

## Data Model Contracts

### Task Representation
- **id**: integer, sequential starting from 1
- **description**: string, 1-256 characters
- **completed**: boolean, default False

### Task List
- Maintains insertion order
- IDs remain sequential after deletion operations
- In-memory only, no persistence