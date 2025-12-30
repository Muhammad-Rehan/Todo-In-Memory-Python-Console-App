"""
Command-line interface for the Todo application.
"""
from typing import Optional
from todo_app.services.task_manager import TaskManager


class TodoCLI:
    """Command-line interface for the Todo application."""

    def __init__(self):
        """Initialize the CLI with a TaskManager instance."""
        self.task_manager = TaskManager()

    def run(self):
        """Main application loop."""
        print("Welcome to the Todo App!")
        while True:
            self._display_menu()
            choice = input("> ").strip()

            if choice == "1":
                self._add_task()
            elif choice == "2":
                self._view_tasks()
            elif choice == "3":
                self._update_task()
            elif choice == "4":
                self._delete_task()
            elif choice == "5":
                self._mark_task_complete()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Error: Invalid menu selection")
                continue

    def _display_menu(self):
        """Display the main menu options."""
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Exit")

    def _add_task(self):
        """Handle adding a new task."""
        description = input("Enter task description: ").strip()

        try:
            # Validate description length
            if not description:
                print("Error: Task description cannot be empty")
                return
            if len(description) > 256:
                print("Error: Task description exceeds 256 characters")
                return

            task = self.task_manager.add_task(description)
            print("Task added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def _view_tasks(self):
        """Handle viewing all tasks."""
        tasks = self.task_manager.get_all_tasks()

        if not tasks:
            print("No tasks in the list")
        else:
            for task in tasks:
                print(task)

    def _update_task(self):
        """Handle updating a task."""
        if self.task_manager.is_empty():
            print("Error: No tasks to update")
            return

        try:
            task_number = int(input("Enter task number to update: "))
        except ValueError:
            print("Error: Invalid task number")
            return

        description = input("Enter new description: ").strip()

        try:
            # Validate description
            if not description:
                print("Error: Task description cannot be empty")
                return
            if len(description) > 256:
                print("Error: Task description exceeds 256 characters")
                return

            updated_task = self.task_manager.update_task(task_number, description)
            if updated_task:
                print("Task updated successfully!")
            else:
                print("Error: Invalid task number")
        except ValueError as e:
            print(f"Error: {e}")

    def _delete_task(self):
        """Handle deleting a task."""
        if self.task_manager.is_empty():
            print("Error: No tasks to delete")
            return

        try:
            task_number = int(input("Enter task number to delete: "))
            deleted = self.task_manager.delete_task(task_number)
            if deleted:
                print("Task deleted successfully!")
            else:
                print("Error: Invalid task number")
        except ValueError:
            print("Error: Invalid task number")

    def _mark_task_complete(self):
        """Handle marking a task as complete."""
        if self.task_manager.is_empty():
            print("Error: No tasks to mark complete")
            return

        try:
            task_number = int(input("Enter task number to mark complete: "))
            task = self.task_manager.mark_task_complete(task_number)
            if task:
                print("Task marked as complete!")
            else:
                print("Error: Invalid task number")
        except ValueError:
            print("Error: Invalid task number")