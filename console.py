import sqlite3
import datetime
import cmd


class TaskTracker(cmd.Cmd):
    intro = "Welcome. Type 'help' to list commands."
    prompt = 'task-cli  '
    db_name = 'task.db'


    def __init__(self):
        super().__init__()
        self.conn = None
        self.cursor = None
        self.connect_to_db()
        self.create_table()


    def connect_to_db(self):
        """Connect to task database"""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
    

    
    def create_table(self):
        """Create the task table"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT,
                status TEXT,
                created_at DATE,
                updated_at DATE          
            )
        ''')
        self.conn.commit()


    def do_add(self, args):
        """Create a new task. Usage: task-cli add "Buy groceries"."""
        description = args.replace('"', '').strip()
        if not description:
            print("Error: Task description cannot be empty.")
            return
        
        status = "todo"
        created_at = datetime.datetime.now().isoformat()
        updated_at = created_at  # Set updated_at to the same as created_at for a new task

        try:
            self.cursor.execute('INSERT INTO tasks (description, status, created_at, updated_at) VALUES (?, ?, ?, ?)',
                                (description, status, created_at, updated_at))
            self.conn.commit()
            task_id = self.cursor.lastrowid  # Get the ID of the last inserted row
            print(f'# Output: Task added successfully (ID: {task_id})')
        except Exception as e:
            print(f"Error: Could not add task. {e}")


    def do_list(self, arg):
        """Read all blog posts. Usage: read"""
        arg = arg.strip()
        if len(arg) == 0:
            self.cursor.execute('SELECT * FROM tasks')
            tasks = self.cursor.fetchall()
        else:
            status = arg
            self.cursor.execute('SELECT * FROM tasks WHERE status=?', (status,))
            tasks = self.cursor.fetchall()
        if len(tasks) == 0:
            print('No tasks found.')
        else:
            print('Tasks:')
            for task in tasks:
                print(f'ID: {task[0]}, Description: {task[1]}, Status: {task[2]}, Created At: {task[3]}, Updated At: {task[3]}')


    def validate_task(self, id):
        self.cursor.execute('SELECT * FROM tasks WHERE id=?', (id,))
        task = self.cursor.fetchone()
        if task is None:
            print(f'Post with ID {id} does not exist.')
            return


    def do_delete(self, arg):
        """Delete a task. Usage: delete <post_id>"""
        task_id = int(arg)
        self.validate_task(task_id)
        self.cursor.execute('DELETE FROM tasks WHERE id=?', (task_id,))
        self.conn.commit()
        print(f'Task {task_id} deleted successfully!')


    
    def update(self, id, content):
        """Helper function to update task"""
        self.validate_task(id)
        updated_at = datetime.datetime.now().isoformat()
        self.cursor.execute('UPDATE tasks SET description=?, updated_at=? WHERE id=?', (content, updated_at, id))
        self.conn.commit()
        print('Post updated successfully!')

    def update_status(self, id, status):
        """Helper function to change status"""
        self.validate_task(id)
        updated_at = datetime.datetime.now().isoformat()
        self.cursor.execute('UPDATE tasks SET status=?, updated_at=? WHERE id=?', (status, updated_at, id))
        self.conn.commit()
        print('Status updated successfully!')

    def do_update(self, args):
        """Update a task. Usage: update <task_id>"""
        args = args.split()
        task_id = int(args[0])
        content = (" ".join(args[1:])).replace('"', '')
        self.update(task_id, content)

    def do_mark_in_progress(self, arg):
        """Mark task as in-progress. Usage: mark_in_progress <task_id>"""
        id = int(arg)
        status = "in-progress"
        self.update_status(id, status)

    def do_mark_done(self, arg):
        """Mark task as done. Usage: mark_done <task_id>"""
        id = int(arg)
        status = "done"
        self.update_status(id, status)
    

    def do_exit(self, arg):
        """Exit the application. Usage: exit"""
        self.conn.close()
        print('Exiting...')
        return True
    

    def do_EOF(self, args):
        """Handle the End-of-File condition"""
        return True

    def emptyline(self):
        """Override emptyline to display only the prompt"""
        print()
    


if __name__ == "__main__":
    task = TaskTracker()
    task.cmdloop()
    



    



