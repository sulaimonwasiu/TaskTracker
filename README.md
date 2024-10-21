# TaskTracker CLI

TaskTracker is a simple command-line interface (CLI) application for managing tasks. It allows users to create, list, update, and delete tasks, making it easy to keep track of personal or work-related tasks.

## Features

- Create new tasks
- List all tasks or filter by status
- Update task descriptions
- Change task status (e.g., to "in-progress" or "done")
- Delete tasks
- Persistent storage using SQLite and JSON file storage

## Task Properties
Each task should have the following properties:

- id: A unique identifier for the task
- description: A short description of the task
- status: The status of the task (todo, in-progress, done)
- createdAt: The date and time when the task was created
- updatedAt: The date and time when the task was last updated

## Requirements

- Python 3.x
- SQLite (included with Python standard library)
- File system (JSON)

## Installation

1. Clone the repository or download the source code.

   ```bash
   git clone <repository-url>
   cd task-tracker
   ```

2. Ensure you have Python installed. You can check your Python version with:

   ```bash
   python --version
   ```

3. Run the application for both file and database storage:

   ```bash
   python app.py
   ```
   ```bash
   python console.py
   ```

## Usage

When you start the application, you will see a prompt:

```
Welcome. Type 'help' to list commands.
task-cli 
```

### Commands

- **Add a Task**
  ```bash
  task-cli add "Buy groceries"
  ```
  Creates a new task with the provided description.

- **List Tasks**
  ```bash
  task-cli list
  ```
  Displays all tasks. You can also filter by status:
  ```bash
  task-cli list todo
  ```

- **Update a Task**
  ```bash
  task-cli update <task_id> "New task description"
  ```
  Updates the description of the specified task.

- **Mark Task as In Progress**
  ```bash
  task-cli mark_in_progress <task_id>
  ```
  Changes the status of the specified task to "in-progress".

- **Mark Task as Done**
  ```bash
  task-cli mark_done <task_id>
  ```
  Changes the status of the specified task to "done".

- **Delete a Task**
  ```bash
  task-cli delete <task_id>
  ```
  Deletes the specified task.

- **Exit the Application**
  ```bash
  task-cli exit
  ```

### Example Usage

1. Add a new task:
   ```bash
   task-cli add "Prepare presentation"
   ```

2. List all tasks:
   ```bash
   task-cli list
   ```

3. Update a task:
   ```bash
   task-cli update 1 "Prepare presentation for client meeting"
   ```

4. Mark a task as done:
   ```bash
   task-cli mark_done 1
   ```

5. Delete a task:
   ```bash
   task-cli delete 1
   ```

6. Exit the application:
   ```bash
   task-cli exit
   ```

## Database

The application uses an SQLite database named `task.db` to store tasks. The database and table will be created automatically on the first run.

## Link
[Project URL](https://github.com/sulaimonwasiu/TaskTracker)

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to create a pull request or open an issue.
