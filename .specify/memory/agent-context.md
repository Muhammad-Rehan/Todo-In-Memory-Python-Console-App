# Todo In-Memory Python Console App Development Guidelines

Auto-generated from all feature plans. Last updated: 2025-12-27

## Active Technologies

- Language: Python 3.13+
- Dependencies: Standard Python libraries only
- Storage: In-memory only
- Testing: Manual testing based on usage scenarios
- Target Platform: Cross-platform (Windows, macOS, Linux)

## Project Structure

```text
src/
├── todo_app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py          # Task model definition
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_manager.py  # Task management logic
│   ├── cli/
│   │   ├── __init__.py
│   │   └── interface.py     # Command-line interface
│   └── main.py              # Application entry point
│
tests/
├── unit/
│   └── test_task.py         # Task model tests
├── integration/
│   └── test_task_manager.py # Task manager tests
└── contract/
    └── test_cli.py          # CLI interface tests
```

## Commands

- Run application: `python src/todo_app/main.py`
- Run tests: Manual testing based on usage scenarios

## Code Style

- Follow PEP 8 style guidelines for Python
- Use clear, descriptive function and variable names
- Keep functions focused on a single responsibility
- Include docstrings for public functions
- Use type hints where beneficial for clarity

## Recent Changes

- 001-todo-app: Initial implementation of core todo functionality (Add, View, Update, Delete, Mark Complete)
- Created modular architecture with separation of concerns
- Implemented in-memory task management with sequential ID assignment

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->