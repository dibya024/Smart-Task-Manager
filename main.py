from tkinter import Tk
from auth_manager import AuthManager
from task_manager import TaskManager
from ui import TaskApp


root = Tk()
root.state("zoomed")
root.configure(bg="#0D1117")
root.title("Task GUI")


auth_manager = AuthManager()
task_manager = TaskManager()

app = TaskApp(root, auth_manager, task_manager)
app.build_home()

root.mainloop()