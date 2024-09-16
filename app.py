import argparse
import json
import os
from datetime import datetime

# File to store tasks
TASK_FILE = 'tasks.json'

# Function to load tasks from JSON file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as file:
        return json.load(file)

# Function to save tasks to JSON file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to add a new task
def add_task(description):
    tasks = load_tasks()
    task_id = 1 if not tasks else tasks[-1]['id'] + 1
    task = {
        'id': task_id,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

# Function to update an existing task
def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task updated successfully (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found")

# Function to delete a task
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f"Task with ID {task_id} deleted successfully")

# Function to mark a task as in progress
def mark_in_progress(task_id):
    update_status(task_id, 'in-progress')

# Function to mark a task as done
def mark_done(task_id):
    update_status(task_id, 'done')

# Helper function to update task status
def update_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task with ID {task_id} marked as {status}")
            return
    print(f"Task with ID {task_id} not found")

# Function to list tasks
def list_tasks(filter_status=None):
    tasks = load_tasks()
    if filter_status:
        tasks = [task for task in tasks if task['status'] == filter_status]
    if not tasks:
        print("No tasks found")
        return
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, CreatedAt: {task['createdAt']}, UpdatedAt: {task['updatedAt']}")

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Task description")

    # Update command
    parser_update = subparsers.add_parser("update", help="Update an existing task")
    parser_update.add_argument("id", type=int, help="Task ID")
    parser_update.add_argument("description", type=str, help="New task description")

    # Delete command
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="Task ID")

    # Mark in-progress command
    parser_mark_in_progress = subparsers.add_parser("mark-in-progress", help="Mark a task as in-progress")
    parser_mark_in_progress.add_argument("id", type=int, help="Task ID")

    # Mark done command
    parser_mark_done = subparsers.add_parser("mark-done", help="Mark a task as done")
    parser_mark_done.add_argument("id", type=int, help="Task ID")

    # List command
    parser_list = subparsers.add_parser("list", help="List tasks")
    parser_list.add_argument("status", nargs="?", choices=["done", "todo", "in-progress"], help="Filter tasks by status")

    # Parse arguments and call appropriate function
    args = parser.parse_args()
    
    if args.command == "add":
        add_task(args.description)
    elif args.command == "update":
        update_task(args.id, args.description)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "mark-in-progress":
        mark_in_progress(args.id)
    elif args.command == "mark-done":
        mark_done(args.id)
    elif args.command == "list":
        list_tasks(args.status)

if __name__ == "__main__":
    main()
