#!/usr/bin/env python3
"""
Quick test script to verify all components of the Todo app work together.
"""
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from todo_app.models.task import Task
from todo_app.services.task_manager import TaskManager
from todo_app.cli.interface import TodoCLI

def test_task_model():
    """Test the Task model."""
    print("Testing Task model...")

    # Test basic task creation
    task = Task(1, "Test task")
    assert task.id == 1
    assert task.description == "Test task"
    assert task.completed == False
    print(f"  [PASS] Created task: {task}")

    # Test task completion
    task.mark_complete()
    assert task.completed == True
    print(f"  [PASS] Marked task complete: {task}")

    # Test description validation
    try:
        Task(2, "")  # Should fail
        assert False, "Empty description should raise ValueError"
    except ValueError:
        print("  [PASS] Empty description validation works")

    try:
        Task(2, "A" * 257)  # Should fail
        assert False, "Long description should raise ValueError"
    except ValueError:
        print("  [PASS] Long description validation works")

    print("Task model tests passed!\n")

def test_task_manager():
    """Test the TaskManager service."""
    print("Testing TaskManager...")

    tm = TaskManager()

    # Test adding tasks
    task1 = tm.add_task("First task")
    task2 = tm.add_task("Second task")
    assert len(tm.get_all_tasks()) == 2
    assert task1.id == 1
    assert task2.id == 2
    print("  [PASS] Added tasks successfully")

    # Test updating a task
    updated_task = tm.update_task(1, "Updated first task")
    assert updated_task is not None
    assert updated_task.description == "Updated first task"
    print("  [PASS] Updated task successfully")

    # Test marking complete
    completed_task = tm.mark_task_complete(2)
    assert completed_task is not None
    assert completed_task.completed == True
    print("  [PASS] Marked task complete successfully")

    # Test deleting a task
    deleted = tm.delete_task(1)
    assert deleted == True
    assert len(tm.get_all_tasks()) == 1
    # Check that remaining task has correct ID
    remaining_task = tm.get_all_tasks()[0]
    assert remaining_task.id == 1  # IDs should be reassigned
    print("  [PASS] Deleted task and reassigned IDs successfully")

    print("TaskManager tests passed!\n")

def main():
    """Run all tests."""
    print("Running Todo App component tests...\n")

    test_task_model()
    test_task_manager()

    print("All tests passed! The Todo app components are working correctly.")

if __name__ == "__main__":
    main()