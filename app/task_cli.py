import argparse
import json
import os
from datetime import datetime

TASK_FILE = 'tasks.json'

# Task class to represent each individual task
class Task:
    def __init__(self, task_id, description, status='todo', created_at=None, updated_at=None):
        self.id = task_id
        self.description = description
        self.status = status
        self.createdAt = created_at or datetime.now().isoformat()
        self.updatedAt = updated_at or datetime.now().isoformat()

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }

# TaskManager class to handle the operations on tasks
class TaskManager:
    def __init__(self, task_file=TASK_FILE):
        self.task_file = task_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.task_file):
            return []
        with open(self.task_file, 'r') as file:
            return [Task(**task) for task in json.load(file)]

    def save_tasks(self):
        with open(self.task_file, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description):
        task_id = 1 if not self.tasks else self.tasks[-1].id + 1
        task = Task(task_id, description)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added successfully (ID: {task_id})")

    def update_task(self, task_id, description):
        task = self.find_task(task_id)
        if task:
            task.description = description
            task.updatedAt = datetime.now().isoformat()
            self.save_tasks()
            print(f"Task updated successfully (ID: {task_id})")
        else:
            print(f"Task with ID {task_id} not found")

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            self.tasks = [t for t in self.tasks if t.id != task_id]
            self.save_tasks()
            print(f"Task with ID {task_id} deleted successfully")
        else:
            print(f"Task with ID {task_id} not found")

    def mark_in_progress(self, task_id):
        self.update_status(task_id, 'in-progress')

    def mark_done(self, task_id):
        self.update_status(task_id, 'done')

    def update_status(self, task_id, status):
        task = self.find_task(task_id)
        if task:
            task.status = status
            task.updatedAt = datetime.now().isoformat()
            self.save_tasks()
            print(f"Task with ID {task_id} marked as {status}")
        else:
            print(f"Task with ID {task_id} not found")

    def list_tasks(self, filter_status=None):
        tasks_to_list = self.tasks if filter_status is None else [task for task in self.tasks if task.status == filter_status]
        if not tasks_to_list:
            print("No tasks found")
            return
        for task in tasks_to_list:
            print(f"ID: {task.id}, Description: {task.description}, Status: {task.status}, CreatedAt: {task.createdAt}, UpdatedAt: {task.updatedAt}")

    def find_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

# TaskCLI class to handle command line interactions
class TaskCLI:
    def __init__(self):
        self.task_manager = TaskManager()

    def run(self):
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

        args = parser.parse_args()
        if args.command == "add":
            self.task_manager.add_task(args.description)
        elif args.command == "update":
            self.task_manager.update_task(args.id, args.description)
        elif args.command == "delete":
            self.task_manager.delete_task(args.id)
        elif args.command == "mark-in-progress":
            self.task_manager.mark_in_progress(args.id)
        elif args.command == "mark-done":
            self.task_manager.mark_done(args.id)
        elif args.command == "list":
            self.task_manager.list_tasks(args.status)

if __name__ == "__main__":
    TaskCLI().run()
