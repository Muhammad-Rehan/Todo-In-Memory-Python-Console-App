"""
TaskManager service to manage a collection of tasks in memory.
"""
from typing import List, Optional
from todo_app.models.task import Task


class TaskManager:
    """Manages a collection of tasks in memory."""

    def __init__(self):
        """Initialize the TaskManager with an empty list of tasks."""
        self._tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, description: str) -> Task:
        """
        Add a new task to the collection.

        Args:
            description (str): The description for the new task

        Returns:
            Task: The newly created task
        """
        task = Task(self._next_id, description, completed=False)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the collection.

        Returns:
            List[Task]: A list of all tasks
        """
        return self._tasks.copy()

    def update_task(self, task_id: int, new_description: str) -> Optional[Task]:
        """
        Update a task's description by ID.

        Args:
            task_id (int): The ID of the task to update
            new_description (str): The new description for the task

        Returns:
            Optional[Task]: The updated task if found, None otherwise
        """
        task = self._find_task_by_id(task_id)
        if task:
            task.update_description(new_description)
            return task
        return None

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if not found
        """
        task = self._find_task_by_id(task_id)
        if task:
            self._tasks.remove(task)
            self._reassign_ids()
            return True
        return False

    def mark_task_complete(self, task_id: int) -> Optional[Task]:
        """
        Mark a task as complete by ID.

        Args:
            task_id (int): The ID of the task to mark complete

        Returns:
            Optional[Task]: The updated task if found, None otherwise
        """
        task = self._find_task_by_id(task_id)
        if task:
            task.mark_complete()
            return task
        return None

    def _find_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Find a task by its ID.

        Args:
            task_id (int): The ID of the task to find

        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def _reassign_ids(self) -> None:
        """Reassign sequential IDs to all tasks after a deletion."""
        for i, task in enumerate(self._tasks, start=1):
            task.id = i
        # Update next_id to be one more than the highest ID
        self._next_id = len(self._tasks) + 1

    def is_empty(self) -> bool:
        """
        Check if the task list is empty.

        Returns:
            bool: True if there are no tasks, False otherwise
        """
        return len(self._tasks) == 0