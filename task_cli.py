from datetime import datetime
import json
import os

TASK_FILE="tasks.json"

def get_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE,'r') as f:
        content=f.read()
        if not content:
            return []
        return json.loads(content)

def save_tasks(tasks):
    with open(TASK_FILE,'w') as f:
        json.dump(tasks,f,indent=4)

def generate_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks)+1

def add_task(description):
    tasks=get_tasks()
    new_id=generate_id(tasks)
    timestamp = datetime.now().isoformat()
    new_task={
        'id': new_id,
        'description': description,
        'status': 'todo',
        'createdAt': timestamp,
        'updatedAt': timestamp
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

