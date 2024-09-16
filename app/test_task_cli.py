import pytest
import os
import json
from app.task_cli import TaskManager

TASK_FILE = 'tasks.json'

# Fixture to ensure the tasks.json is cleaned up before and after tests
@pytest.fixture(autouse=True)
def clean_tasks_file():
    if os.path.exists(TASK_FILE):
        os.remove(TASK_FILE)
    yield
    if os.path.exists(TASK_FILE):
        os.remove(TASK_FILE)

# Test case for adding a new task
def test_add_task():
    task_manager = TaskManager()
    task_manager.add_task("Complete project documentation")

    # Check if the task was added
    with open(TASK_FILE, "r") as f:
        tasks = json.load(f)
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Complete project documentation"
    assert tasks[0]["status"] == "todo"

# Test case for updating a task
def test_update_task():
    task_manager = TaskManager()
    task_manager.add_task("Complete project documentation")
    task_manager.update_task(1, "Complete and submit project documentation")

    # Check if the task was updated
    with open(TASK_FILE, "r") as f:
        tasks = json.load(f)
    assert tasks[0]["description"] == "Complete and submit project documentation"

# Test case for deleting a task
def test_delete_task():
    task_manager = TaskManager()
    task_manager.add_task("Complete project documentation")
    task_manager.delete_task(1)

    # Check if the task was deleted
    with open(TASK_FILE, "r") as f:
        tasks = json.load(f)
    assert len(tasks) == 0

# Test case for marking a task as in-progress
def test_mark_in_progress():
    task_manager = TaskManager()
    task_manager.add_task("Complete project documentation")
    task_manager.mark_in_progress(1)

    # Check if the task was marked as in-progress
    with open(TASK_FILE, "r") as f:
        tasks = json.load(f)
    assert tasks[0]["status"] == "in-progress"

# Test case for marking a task as done
def test_mark_done():
    task_manager = TaskManager()
    task_manager.add_task("Complete project documentation")
    task_manager.mark_done(1)

    # Check if the task was marked as done
    with open(TASK_FILE, "r") as f:
        tasks = json.load(f)
    assert tasks[0]["status"] == "done"

# Test case for listing tasks by status (done)
def test_list_done_tasks(capfd):
    task_manager = TaskManager()
    task_manager.add_task("Complete project documentation")
    task_manager.mark_done(1)

    # Capture the printed output from list_tasks
    task_manager.list_tasks(filter_status='done')
    captured = capfd.readouterr()
    assert "Complete project documentation" in captured.out
    assert "done" in captured.out

# Test case for handling non-existent task update
def test_update_non_existent_task(capfd):
    task_manager = TaskManager()
    task_manager.update_task(999, "This task does not exist")

    # Capture the printed output for a non-existent task
    captured = capfd.readouterr()
    assert "Task with ID 999 not found" in captured.out

# Test case for handling non-existent task deletion
def test_delete_non_existent_task(capfd):
    task_manager = TaskManager()
    task_manager.delete_task(999)

    # Capture the printed output for a non-existent task
    captured = capfd.readouterr()
    assert "Task with ID 999 not found" in captured.out
