import json
import datetime
import cmd
import os

class TaskTracker(cmd.Cmd):
    intro = "Welcome. Type 'help' to list commands."
    prompt = 'task-cli  '
    data_file = 'tasks.json'

    def __init__(self):
        super().__init__()
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from the JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return []

    def save_tasks(self):
        """Save tasks to the JSON file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def do_add(self, args):
        """Create a new task. Usage: add "Buy groceries"."""
        description = args.replace('"', '').strip()
        if not description:
            print("Error: Task description cannot be empty.")
            return

        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'status': 'todo',
            'created_at': datetime.datetime.now().isoformat(),
            'updated_at': datetime.datetime.now().isoformat()
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f'# Output: Task added successfully (ID: {task["id"]})')

    def do_list(self, arg):
        """List all tasks or filter by status. Usage: list [status]"""
        arg = arg.strip()
        filtered_tasks = [task for task in self.tasks if task['status'] == arg] if arg else self.tasks

        if not filtered_tasks:
            print('No tasks found.')
        else:
            print('Tasks:')
            for task in filtered_tasks:
                print(f'ID: {task["id"]}, Description: {task["description"]}, '
                      f'Status: {task["status"]}, Created At: {task["created_at"]}, '
                      f'Updated At: {task["updated_at"]}')

    def validate_task(self, id):
        """Check if a task exists by ID."""
        for task in self.tasks:
            if task['id'] == id:
                return task
        print(f'Task with ID {id} does not exist.')
        return None

    def do_delete(self, arg):
        """Delete a task. Usage: delete <task_id>"""
        task_id = int(arg)
        task = self.validate_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print(f'Task {task_id} deleted successfully!')

    def do_update(self, args):
        """Update a task. Usage: update <task_id> "New description"."""
        args = args.split()
        task_id = int(args[0])
        content = " ".join(args[1:]).replace('"', '')
        task = self.validate_task(task_id)
        if task:
            task['description'] = content
            task['updated_at'] = datetime.datetime.now().isoformat()
            self.save_tasks()
            print('Task updated successfully!')

    def update_status(self, id, status):
        """Helper function to update status"""
        task = self.validate_task(id)
        if task:
            task['status'] = status
            task['updated_at'] = datetime.datetime.now().isoformat()
            self.save_tasks()
            print(f'Task marked as {status}.')

    def do_mark_in_progress(self, arg):
        """Mark task as in-progress. Usage: mark_in_progress <task_id>"""
        task_id = int(arg)
        self.update_status(task_id, "in-progress")

    def do_mark_done(self, arg):
        """Mark task as done. Usage: mark_done <task_id>"""
        task_id = int(arg)
        self.update_status(task_id, "done")


    def do_exit(self, arg):
        """Exit the application. Usage: exit"""
        print('Exiting...')
        return True

    def do_EOF(self, args):
        """Handle the End-of-File condition"""
        return True

    def emptyline(self):
        """Override emptyline to display a blank line before the prompt."""
        print()

if __name__ == "__main__":
    task_tracker = TaskTracker()
    task_tracker.cmdloop()