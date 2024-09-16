import subprocess
import os
import json
import pytest

# Define the path to the CLI script
TASK_CLI = "task-cli.py"
TASK_FILE = "tasks.json"

# Helper function to run a CLI command and return output
def run_cli(args):
    result = subprocess.run(["python", TASK_CLI] + args, capture_output=True, text=True)
    return result.stdout.strip()

# Helper function to clean up the tasks.json file before each test
@pytest.fixture(autouse=True)
def clean_tasks_file():
    if os.path.exists(TASK_FILE):
        os.remove(TASK_FILE)
    yield
    if os.path.exists(TASK_FILE):
        os.remove(TASK_FILE)

# Test case for adding a new task
def test_add_task():
    output = run_cli(["add", "Complete project documentation"])
    assert "Task added successfully" in output

    # Check if the task was written to tasks.json
    with open(TASK_FILE, "r") as f:
        tasks = json.load(f)
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Complete project documentation"
    assert tasks[0]["status"] == "todo"

# Test case for listing all tasks
def test_list_tasks():
    run_cli(["add", "Complete project documentation"])
    output = run_cli(["list"])
    assert "Complete project documentation" in output

# Test case for updating a task
def test_update_task():
    run_cli(["add", "Complete project documentation"])
    output = run_cli(["update", "1", "Complete and submit project documentation"])
    assert "Task updated successfully" in output

    # Check if the task was updated in tasks.json
    with open(TASK_FILE, "r") as f:
        tasks = json.load(f)
    assert tasks[0]["description"] == "Complete and submit project documentation"

# Test case for marking a task as in-progress
def test_mark_in_progress():
    run_cli(["add", "Complete project documentation"])
    output = run_cli(["mark-in-progress", "1"])
    assert "marked as in-progress" in output

    # Check if the task status was updated in tasks.json
    with open(TASK_FILE, "r") as f:
        tasks = json.load(f)
    assert tasks[0]["status"] == "in-progress"

# Test case for marking a task as done
def test_mark_done():
    run_cli(["add", "Complete project documentation"])
    run_cli(["mark-in-progress", "1"])
    output = run_cli(["mark-done", "1"])
    assert "marked as done" in output

    # Check if the task status was updated in tasks.json
    with open(TASK_FILE, "r") as f:
        tasks = json.load(f)
    assert tasks[0]["status"] == "done"

# Test case for deleting a task
def test_delete_task():
    run_cli(["add", "Complete project documentation"])
    output = run_cli(["delete", "1"])
    assert "deleted successfully" in output

    # Check if the task was removed from tasks.json
    with open(TASK_FILE, "r") as f:
        tasks = json.load(f)
    assert len(tasks) == 0

# Test case for listing done tasks
def test_list_done_tasks():
    run_cli(["add", "Complete project documentation"])
    run_cli(["mark-done", "1"])
    output = run_cli(["list", "done"])
    assert "Complete project documentation" in output
    assert "done" in output

# Test case for listing tasks by status (todo)
def test_list_todo_tasks():
    run_cli(["add", "Complete project documentation"])
    output = run_cli(["list", "todo"])
    assert "Complete project documentation" in output
    assert "todo" in output

# Test case for handling non-existent task update
def test_update_non_existent_task():
    output = run_cli(["update", "999", "This task does not exist"])
    assert "Task with ID 999 not found" in output

# Test case for handling non-existent task deletion
def test_delete_non_existent_task():
    output = run_cli(["delete", "999"])
    assert "Task with ID 999 not found" in output
