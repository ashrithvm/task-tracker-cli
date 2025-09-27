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

