import json
from datetime import datetime
import winsound


class TaskManager:
    def __init__(self):
        self.tasks = []

    def load_tasks(self, username):
        filename = f"{username}_tasks.json"

        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self, username):
        filename = f"{username}_tasks.json"

        with open(filename, "w") as file:
            json.dump(self.tasks, file, indent=5)
            
            
            
            
            
            
    def show_list(self):
        return self.tasks
            
        
    def add_task(self, username, task, target_time=None):
        
        self.tasks.append({
            "Task": task,
            "Target Time": target_time,
            "Completed": False
        })

        self.save_tasks(username)
        
        

    def remove_task(self, username, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks(username)
            return True

        return False
    
    def update_task(self, username, index, new_task, target_time):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = {
                "Task": new_task,
                "Target Time": target_time,
                "Completed": False
            }

            self.save_tasks(username)
            return True

        return False
    
    def reset_priority(self, username):
        def parse_time(task):
            t = task.get("Target Time")

            if not t:
                return datetime.strptime("23:59", "%H:%M").time()

            return datetime.strptime(t, "%H:%M").time()

        self.tasks.sort(key=parse_time)
        self.save_tasks(username)

    def mark_completed(self, username, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["Completed"] = True
            self.save_tasks(username)
            return True

        return False
    
    def reminder(self, index):
        
        if not self.tasks:
            return "Empty"
            
        if not(0 <= index < len(self.tasks)):
            return "Invalid"
            
        task= self.tasks[index]
            
        alarm_time= task.get("Target Time")
        if not alarm_time:
            return "No Target time available."
            
        curr_time= datetime.now().strftime("%H:%M")
            
        if curr_time == alarm_time:
            winsound.Beep(1500, 2000);
            return {
                "Status":"ring",
                "Task": task
            }
                
        return {
            "Status": "Waiting...",
            "Task": task,
            "Next Alarm time": alarm_time
        }
        
    
    def reset(self, username):
        
        if not self.tasks:
            return ("Empty task file.")

        self.tasks= []
        self.save_tasks(username)
        
        return "Reset sucessfully."