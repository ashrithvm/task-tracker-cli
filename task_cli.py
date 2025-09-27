#!/usr/bin/env python3
"""
A simple command-line interface (CLI) to track tasks.

This script allows users to add, update, delete, and list tasks.
Tasks are stored in a JSON file in the same directory.
"""

import argparse
import json
import os
import sys
from datetime import datetime

# Define the name of the file where tasks will be stored.
TASKS_FILE = "tasks.json"

def get_tasks():
    """
Loads the list of tasks from the JSON file.

Checks if the tasks file exists. If not, it returns an empty list.
If the file exists but is empty, it also returns an empty list.
Otherwise, it reads the file and decodes the JSON content into a Python list.

Returns:
list: A list of task dictionaries.
    """
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        content = f.read()
        if not content:
            return []
        return json.loads(content)

def save_tasks(tasks):
    """
Saves the list of tasks to the JSON file.

This function takes a list of task dictionaries and writes it to the
tasks file in JSON format with human-readable indentation.

Args:
tasks (list): The list of task dictionaries to save.
    """
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def generate_id(tasks):
    """
Generates a new unique ID for a task.

It finds the maximum ID among existing tasks and returns the next integer.
If there are no tasks, it starts with ID 1.

Args:
tasks (list): The current list of tasks.

Returns:
int: A new unique ID.
    """
    if not tasks:
        return 1
    # Find the highest existing ID and add 1
    return max(task['id'] for task in tasks) + 1

def add_task(description):
    """
Adds a new task to the list.

It loads the current tasks, creates a new task dictionary with a unique ID,
the provided description, a default status of 'todo', and timestamps.
Then it saves the updated list of tasks.

Args:
description (str): The text description of the task.
    """
    tasks = get_tasks()
    new_id = generate_id(tasks)
    timestamp = datetime.now().isoformat()
    new_task = {
        'id': new_id,
        'description': description,
        'status': 'todo',
        'createdAt': timestamp,
        'updatedAt': timestamp
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def find_task(tasks, task_id):
    """
Finds a task by its ID.

A helper function to iterate through the list of tasks and return the
one that matches the given ID.

Args:
tasks (list): The list of tasks to search within.
task_id (int): The ID of the task to find.

Returns:
dict or None: The task dictionary if found, otherwise None.
    """
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

def update_task(task_id, description):
    """
Updates the description of an existing task.

Finds the task by its ID, updates its description and 'updatedAt' timestamp,
and saves the changes. If the task is not found, it prints an error.

Args:
task_id (int): The ID of the task to update.
description (str): The new description for the task.
    """
    tasks = get_tasks()
    task = find_task(tasks, task_id)
    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return
    task['description'] = description
    task['updatedAt'] = datetime.now().isoformat()
    save_tasks(tasks)
    print(f"Task {task_id} updated successfully.")

def delete_task(task_id):
    """
Deletes a task by its ID.

It filters the task list to exclude the task with the given ID and saves
the new list. If no task was removed (i.e., ID not found), it prints an error.

Args:
task_id (int): The ID of the task to delete.
    """
    tasks = get_tasks()
    # Create a new list containing all tasks except the one with the specified ID
    new_tasks = [task for task in tasks if task['id'] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"Error: Task with ID {task_id} not found.")
        return
    save_tasks(new_tasks)
    print(f"Task {task_id} deleted successfully.")

def mark_task(task_id, status):
    """
Marks a task with a specific status ('in-progress' or 'done').

Finds the task by ID, validates the new status, updates the task's status
and 'updatedAt' timestamp, and saves the changes.

Args:
task_id (int): The ID of the task to mark.
status (str): The new status ('in-progress' or 'done').
    """
    tasks = get_tasks()
    task = find_task(tasks, task_id)
    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return
    if status not in ['todo', 'in-progress', 'done']:
        print(f"Error: Invalid status '{status}'. Use 'in-progress' or 'done'.")
        return
    task['status'] = status
    task['updatedAt'] = datetime.now().isoformat()
    save_tasks(tasks)
    print(f"Task {task_id} marked as {status}.")

def list_tasks(filter_status=None):
    """
Lists all tasks, with an option to filter by status.

It loads all tasks and prints them. If a filter_status is provided,
it only prints tasks that match that status.

Args:
filter_status (str, optional): The status to filter by ('todo',
'in-progress', 'done'). Defaults to None.
    """
    tasks = get_tasks()

    if filter_status:
        # Validate the provided status filter
        if filter_status not in ['todo', 'in-progress', 'done']:
            print(f"Error: Invalid status filter '{filter_status}'. Use todo, in-progress, or done.")
            return
        # Filter tasks based on the given status
        filtered_tasks = [task for task in tasks if task['status'] == filter_status]
    else:
        # If no filter is provided, use the entire list of tasks
        filtered_tasks = tasks

    if not filtered_tasks:
        print("No tasks found.")
        return

    # Iterate through the filtered tasks and print their details
    for task in filtered_tasks:
        print(f"ID: {task['id']}")
        print(f"  Description: {task['description']}")
        print(f"  Status: {task['status']}")
        print(f"  Created At: {task['createdAt']}")
        print(f"  Updated At: {task['updatedAt']}")
        print("-" * 20)

def main():
    """
The main function that sets up the command-line argument parser and
executes the corresponding task function based on user input.
    """
    # Create the top-level parser
    parser = argparse.ArgumentParser(description="A simple CLI task tracker.")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Create the parser for the "add" command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='The description of the task')

    # Create the parser for the "update" command
    update_parser = subparsers.add_parser('update', help='Update an existing task')
    update_parser.add_argument('id', type=int, help='ID of the task to update')
    update_parser.add_argument('description', type=str, help='New description for the task')

    # Create the parser for the "delete" command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='ID of the task to delete')

    # Create the parser for the "mark-in-progress" command
    mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help='Mark a task as in-progress')
    mark_in_progress_parser.add_argument('id', type=int, help='ID of the task')

    # Create the parser for the "mark-done" command
    mark_done_parser = subparsers.add_parser('mark-done', help='Mark a task as done')
    mark_done_parser.add_argument('id', type=int, help='ID of the task')

    # Create the parser for the "list" command
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('status', nargs='?', default=None, choices=['todo', 'in-progress', 'done'], help='Filter by status')

    # If no command is provided, print the help message
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    # Parse the arguments from the command line
    args = parser.parse_args()

    # Call the appropriate function based on the command
    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'update':
        update_task(args.id, args.description)
    elif args.command == 'delete':
        delete_task(args.id)
    elif args.command == 'mark-in-progress':
        mark_task(args.id, 'in-progress')
    elif args.command == 'mark-done':
        mark_task(args.id, 'done')
    elif args.command == 'list':
        list_tasks(args.status)
    else:
        # This case is handled by argparse, but is here for completeness
        print("Invalid command. Use --help for a list of commands.")

# This ensures the main() function is called only when the script is executed directly
if __name__ == '__main__':
    main()
