# Task Tracker CLI

A simple command-line interface (CLI) application for tracking and managing your daily tasks. This project was built as part of the [roadmap.sh task tracker project](https://roadmap.sh/projects/task-tracker) to practice CLI development and file handling in Python.

## Features

- ✅ Add new tasks with unique IDs
- ✏️ Update existing task descriptions
- 🗑️ Delete tasks by ID
- 📋 List all tasks or filter by status
- 🔄 Mark tasks as in-progress or completed
- 💾 Persistent storage using JSON file
- ⏰ Automatic timestamps for creation and updates

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ashrithvm/task-tracker-cli.git
   cd task-tracker-cli
   ```


2. Make the script executable (optional):
    ```bash
    chmod +x task_cli.py
    ```

3. (Optional but Recommended) Create a Symbolic Link:
    To make the command available system-wide, create a symbolic link to it in a directory that is in your system's PATH. A common location is `/usr/local/bin`.

    ```bash
    sudo ln -s "$(pwd)/task_cli.py" /usr/local/bin/task-cli
    ```

    You can now run your application from any directory in the terminal like this:

    ```bash
    task-cli add "Finish my project"
    ```

## Usage

### Adding a new task
```bash
task-cli add "Buy groceries"
```

### Updating a task
```bash
task-cli update 1 "Buy groceries and cook dinner"
```

### Deleting a task
```bash
task-cli delete 1
```

### Marking a task as in progress
```bash
task-cli mark-in-progress 1
```

### Marking a task as done
```bash
task-cli mark-done 1
```

### Listing tasks

List all tasks:
```bash
task-cli list
```

List tasks by status:
```bash
# List only todo tasks
task-cli list todo

# List only in-progress tasks
task-cli list in-progress

# List only completed tasks
task-cli list done
```

### Getting help
```bash
task-cli --help
```

## Task Properties

Each task contains the following properties:

- `id`: A unique identifier for the task
- `description`: A short description of the task
- `status`: The status of the task (`todo`, `in-progress`, `done`)
- `createdAt`: The date and time when the task was created
- `updatedAt`: The date and time when the task was last updated

## Data Storage

Tasks are stored in a `tasks.json` file in the same directory as the script. The file is created automatically when you add your first task.

### Example JSON structure:
```json
[
    {
        "id": 1,
        "description": "Buy groceries",
        "status": "todo",
        "createdAt": "2025-09-27T10:30:00.123456",
        "updatedAt": "2025-09-27T10:30:00.123456"
    },
    {
        "id": 2,
        "description": "Walk the dog",
        "status": "in-progress",
        "createdAt": "2025-09-27T11:00:00.654321",
        "updatedAt": "2025-09-27T11:15:00.789012"
    }
]
```

## Project Structure

```
task-tracker-cli/
├── task_cli.py      # Main CLI script
├── tasks.json       # Task data storage (created automatically)
└── README.md        # Project documentation
```

## Implementation Details

The project implements the following core functionalities as specified in the roadmap.sh project requirements:

1. **Task Management**: Add, update, and delete tasks
2. **Status Tracking**: Three status levels (todo, in-progress, done)
3. **Persistent Storage**: JSON file-based storage
4. **CLI Interface**: Command-line argument parsing using `argparse`
5. **Data Validation**: Input validation and error handling
6. **Timestamps**: Automatic tracking of creation and update times

## Error Handling

The application includes robust error handling for common scenarios:

- Invalid task IDs
- Invalid status values
- Missing or corrupted JSON files
- Invalid command-line arguments

## Contributing

This is a learning project, but contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Future Enhancements

Some ideas for extending this project:

- [ ] Task priorities (high, medium, low)
- [ ] Due dates and reminders
- [ ] Task categories/tags
- [ ] Export to different formats (CSV, PDF)
- [ ] Task search functionality
- [ ] Undo/redo operations
- [ ] Task dependencies
- [ ] Time tracking for tasks

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- [roadmap.sh](https://roadmap.sh/) for providing the project specifications
- Python community for excellent documentation and resources

---

**Happy task tracking!** 🚀