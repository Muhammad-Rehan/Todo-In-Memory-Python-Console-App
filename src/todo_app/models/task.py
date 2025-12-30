"""
Task model representing a single todo item.
"""
from typing import Optional


class Task:
    """Represents a single item on the todo list."""

    def __init__(self, task_id: int, description: str, completed: bool = False):
        """
        Initialize a Task instance.

        Args:
            task_id (int): Sequential identifier for the task (1-indexed)
            description (str): Text description of the task (max 256 characters)
            completed (bool): Boolean indicating completion status (default: False)
        """
        self.id = task_id
        self.description = self._validate_description(description)
        self.completed = completed

    def _validate_description(self, description: str) -> str:
        """
        Validate the task description.

        Args:
            description (str): The description to validate

        Returns:
            str: The validated description

        Raises:
            ValueError: If description is empty or exceeds 256 characters
        """
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")

        if len(description) > 256:
            raise ValueError("Task description exceeds 256 characters")

        return description

    def update_description(self, new_description: str) -> None:
        """
        Update the task description.

        Args:
            new_description (str): The new description for the task
        """
        self.description = self._validate_description(new_description)

    def mark_complete(self) -> None:
        """Mark the task as complete."""
        self.completed = True

    def mark_incomplete(self) -> None:
        """Mark the task as incomplete."""
        self.completed = False

    def __str__(self) -> str:
        """
        String representation of the task.

        Returns:
            str: Formatted string representation of the task
        """
        status = "[x]" if self.completed else "[ ]"
        return f"{self.id}. {status} {self.description}"