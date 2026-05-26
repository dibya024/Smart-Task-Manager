from tkinter import *
from tkinter import messagebox as tmsg
from datetime import datetime
import random
from PIL import Image, ImageTk, ImageEnhance


class TaskApp:
    def __init__(self, root, auth_manager, task_manager):
        self.root = root
        self.auth = auth_manager
        self.task_manager = task_manager
        self.clock_job= None
        
        
        
    def build_home(self):
        
        self.frame1 = Frame(self.root, bg="#161B22")
        self.frame1.pack(expand=True, fill=BOTH)
        
        self.frame2= Frame( self.root, borderwidth= 10, bg= "black", relief= GROOVE, width= 400, height= 2 )
        
        Frame(self.root, height=1, bg="#30363D").pack(side="bottom", fill="x")
        
        self.down_frm= Frame(self.root, bg= "#161B22")
        self.down_frm.pack(fill= X, side= BOTTOM)
        
        self.title_label= Label( self.frame1, text="Welcome to your task review portal", bg="#050B16", fg="#E6EDF3", font=("Segoe UI", 30, "bold" ), padx= 20, pady= 10)
        
        img= Image.open("photo.jpg")
        
        screen_width = self.root.winfo_screenwidth()

        screen_height = self.root.winfo_screenheight()
        
        enhancer= ImageEnhance.Brightness(img)
        img= enhancer.enhance(0.45)
        
        img= img.resize( (screen_width, screen_height))
        self.bg_img= ImageTk.PhotoImage(img)
        
        self.image_label= Label(self.frame1, 
                                image= self.bg_img,
                                bd= 0)
        self.image_label.place(x= 0, y= 0, 
                              relwidth= 1, relheight= 1)
        self.image_label.lower()
        
        
        
        self.title_label.place(relx= 0.5, rely= 0.5, anchor= "center")
        
        
        self.sub_label1 = Label(self.frame1, text="Manage your workflow efficiently",
            font=("Montserrat", 22, "italic"), fg="#E6EDF3", bg="#050B16", padx= 20, pady= 8, bd=0, relief= FLAT)

        self.sub_label1.place(relx=0.73,rely=0.27,anchor= "center")
        
        self.sub_label2 = Label(self.frame1, text="Track Your Tasks",
            font=("Montserrat", 22, "bold"), fg="#E6EDF3", bg="#050B16", padx= 25, pady= 8, bd= 0, relief= "flat")

        self.sub_label2.place(relx=0.22,rely=0.72,anchor= "center")
        

        self.btn1= Button(self.frame1, bg= "#1F6FEB", fg= "white", activebackground = "#388BFD",
                          activeforeground="white",
                          font= ("Segoe UI", 16, "bold"), text= "Click here to proceed", 
                          command= self.open_menu,
                          padx= 25, pady= 10, bd= 0, relief= "flat", cursor= "hand2")
        
        self.btn1.place(relx= 0.5, rely= 0.78, anchor= "center")
        
        
        def on_enter(e):
            self.btn1.config( bg="#388BFD" )

        def on_leave(e):
            self.btn1.config( bg="#1F6FEB" )

        self.btn1.bind("<Enter>", on_enter)
        self.btn1.bind("<Leave>", on_leave)
        
        
        
    def open_signup(self):
        ans= tmsg.askquestion("Sign Up", "Proceed to Sign Up")
        if ans == "yes":
            msg= "Sign Up now."
            
            self.frame2.place( relx=0.5, rely=0.5, anchor="center", width=500, height=350 )
            self.frame2.grid_columnconfigure(0, weight= 1)
            self.frame2.grid_columnconfigure(1, weight= 1)
        
            for widget in self.frame2.winfo_children():
                widget.destroy()
            
            signup_userval= StringVar()
            signup_passval= StringVar()
        
            Label(self.frame2, text="Username", bg= "yellow", fg= "black", font= ("Segoe UI", 12, "bold")).grid(row=0, column=0, padx=10, pady=15)
            Label(self.frame2, text="Password", bg= "yellow", fg= "black", font= ("Segoe UI", 12, "bold")).grid(row=1, column=0, padx=10, pady=15)
        
            entry_user= Entry(self.frame2, textvariable=signup_userval, bg= "#F0F6FC", fg= "black", font= ("Segoe UI", 12), relief= FLAT)
            entry_user.insert(0, "Enter an Username")
            entry_pass= Entry(self.frame2, textvariable=signup_passval, bg= "#F0F6FC", fg= "black", font= ("Segoe UI", 12), relief= FLAT)
            entry_pass.insert(0, "Enter a strong password.")
        
            def clear_user(event):
                if entry_user.get() == "Enter an Username":
                    entry_user.delete(0, END)
                    entry_user.config(fg= "black")
            entry_user.bind("<FocusIn>", clear_user)
            entry_user.grid(row=0, column=1, padx=5, pady=5)  
        
            def clear_pass(event):
                if entry_pass.get() == "Enter a strong password.":
                    entry_pass.delete(0, END)
                    entry_pass.config(fg= "black", show= "*")
            entry_pass.bind("<FocusIn>", clear_pass)
            entry_pass.grid(row=1, column=1, padx=5, pady=5)
        
            def create_acc():
                username= signup_userval.get()
                password= signup_passval.get()
                
                if username =="" or username.strip() == "Enter an Username":
                    tmsg.showinfo("No User", "Please enter an Username!")
                    return
                
                if password == "" or password.strip() == "Enter a strong password.":
                    tmsg.showinfo("No Password", "Please create your password!")
                    return
            
                result= self.auth.signup(username, password)
            
                if result:
                    tmsg.showinfo("Sign Up", "Account created successfully.")
                    # self.root.destroy()
                    self.frame2.place_forget()
                    self.open_signin()
                    
                else:
                    tmsg.showinfo("Sign Up", "Username already exists.")
                
            Button(self.frame2, text= "Create Account", bg= "#007ACC", fg="white",
                command=create_acc, padx= 10, pady= 8, font= ("Segoe UI", 12, "bold"), relief= FLAT).place(relx= 0.3, rely= 0.8, anchor= "center")
            
            Button(self.frame2, text= "Back to Sign in", bg= "#007ACC", fg="white",
                command=self.open_signin, padx= 8, pady= 10, font= ("Segoe UI", 12, "bold"), relief= FLAT).place(relx= 0.7, rely= 0.8, anchor= "center")
        

    
    
    def logout(self):
        self.auth.current_user= None
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.build_home()






    
    
    def open_dashboard(self):
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.state("zoomed")
        self.root.title("Task Dashboard")
        
        dashboard= Frame(self.root, bg= "#050B16")
        dashboard.place(relx= 0.5, rely= 0.5, anchor= "center", relwidth= 1, relheight= 1)
        
        
        sidebar_container= Frame(dashboard, bg= "#161B22", width= 350)
        sidebar_container.pack(side= LEFT, fill= Y)
        sidebar_container.pack_propagate(False)
        
        sidebar_scroll= Scrollbar(sidebar_container)
        sidebar_scroll.pack(side= "right", fill= Y)
        
        sidebar= Text(sidebar_container, bg= "#161B22", relief= "flat", bd= 0, width= 28, yscrollcommand= sidebar_scroll.set)
        sidebar.pack(side= LEFT, fill= BOTH, expand= True)
        
        sidebar_scroll.config(command= sidebar.yview)
        
        sidebar.config(state= "normal")
        
        
        self.content= Frame(dashboard, bg= "#0D1117")
        self.content.pack(side= RIGHT, expand= True, fill= BOTH)
        
        
        Label( self.content, text="Welcome to DEEPTAM", bg="#161B22", fg="#A855F7", font="Helvetica 24 bold", pady= 15).pack(fill=X, padx= 40, pady= (30, 15))
        
        Label( self.content, text="Task Manager Dashboard", bg="#212216", fg="#F7556D", font=("Segoe UI", 18, "bold"), pady= 10).pack(fill=X, padx= 40)

        menu_label= Label(sidebar, text= "Menu", bg= "#161B22", fg= "white", font= ("Segoe UI", 20, "bold"))
        sidebar.window_create(END, window= menu_label)
        sidebar.insert(END, "\n\n")
        
        
        actions = {
        "Show Tasks List": lambda: self.open_ui_show_list(),
        "Add Task": lambda: self.open_ui_add_task(),
        "Remove Task": lambda: self.open_ui_remove_task(),
        "Update Task": lambda: self.open_ui_update_task(),
        "Reset priority": lambda: self.open_ui_reset_priority(),
        "Reminder Alarm": lambda: self.open_ui_reminder(),
        "Reset Task": lambda: self.open_ui_reset(),
        "Check Complition": lambda: self.open_ui_mark_complete()}
    
        colors = ["#1F6FEB",  "#22D3EE",  "#A855F7",   "#F59E0B",   "#10B981",   "#EF4444", "#EC4899",  "#8B5CF6",   "#14B8A6",  "#F97316",   "#3B82F6",  "#84CC16"]   

        random.shuffle(colors)
    
        for i, (text, action) in enumerate(actions.items()):
        
            btn= Button(sidebar, text= text, command= action, bg= colors[i%len(colors)], fg= "white", activebackground= "#388BFD", 
                        activeforeground="white", relief= "groove", bd= 2, font= ("Segoe UI", 16, "bold"), width= 20, height= 2, cursor= "hand2")

            sidebar.window_create(END, window= btn)
            sidebar.insert(END, "\n\n")
        
    
        signout_btn= Button(sidebar,text="Sign Out",bg="#DC2626", fg="white",activebackground="#EF4444",  
        activeforeground="white",relief="flat",bd=0,font=("Segoe UI", 12, "bold"), height= 2,
        command=self.logout)
        sidebar.window_create(END, window= signout_btn)
        sidebar.insert(END, "\n")
        sidebar.config(state= "disabled")
        
        sidebar.update_idletasks()
        sidebar.config(state="disabled")
        
        
        info_frame= Frame(self.content, bg= "#0D1117")
        info_frame.pack(expand= True)
        
        Label(info_frame, text= "Select an option from the sidebar", bg= "#E6EDF3", font= ("Segoe UI", 22, "bold")).pack(pady= 20)
        
        tasks= self.task_manager.show_list()
        
        if tasks:
            Label(info_frame, text= "Today's tasks", bg= "#0D1117", fg= "#22D3EE", font= ("Segoe UI", 18, "bold")).pack(pady= (20, 10))
            
            for i, task in enumerate(tasks[:5]):
                text= f"{i+1} : {task['Task']}"
                
                if task.get("Target Time"):
                    text += f" | {task['Target Time']}"
                    
                if task.get("Completed"):
                    text += " | Comlpeted"
                else:
                    text += " | Pending"
                    
                Label(info_frame, text= text, bg= "#30363D", fg= "white", font= ("Segoe UI", 12), padx= 15, pady= 10).pack(pady= 5)


            
    
    
    
    
    
    def open_signin(self):

        self.frame1.pack_forget()
        self.frame2.place(relx=0.5, rely=0.5, anchor="center",
            width=500, height=300)
        
        for widget in self.frame2.winfo_children():
            widget.destroy()
            
        center_frame = Frame(self.frame2, bg="black")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        userval= StringVar()
        passval= StringVar()
        
        Label( center_frame, text="Username", bg="orange", fg="black", 
              font=("Segoe UI", 10, "bold")).grid(row=0, column=0, padx=15, pady=10)

        Label( center_frame, text="Password", bg="orange", fg="black", 
              font=("Segoe UI", 10, "bold")).grid(row=1, column=0, padx=15, pady=10)

        entry_user = Entry(center_frame, textvariable=userval, width= 20,  font=("Segoe UI", 10))

        entry_user.grid( row=0, column=1, padx=15, pady=10)
        
        entry_pass = Entry( center_frame, textvariable=passval, width= 20, font=("Segoe UI", 10))

        entry_pass.grid( row=1, column=1, padx=15, pady=10)
        
        def clear_pass(event):
            entry_pass.delete(0, END)
            entry_pass.config(show= "*")
        entry_pass.bind("<FocusIn>", clear_pass)
        
        def getVals():
            
            username= userval.get()
            password= passval.get()
            
            res= self.auth.login(username, password)
                
            if res == "blocked":
                tmsg.showerror("Blocked", "No attempts left.")
                tmsg.showwarning( "Application Closed", "Too many failed attempts.\nApplication will now close.")
                self.root.destroy()
                
            elif res:
                self.task_manager.load_tasks(username)
                tmsg.showinfo("Success", "Log in successful.")
                
                self.open_dashboard()
                
            else:
                userval.set("")
                passval.set("")
                
                tmsg.showerror("Error", f"Wrong Credentials.\n{self.auth.attempts} attempts left!")
                
        Button(center_frame, text= "Submit", bg= "red", fg= "white", font=("Segoe UI", 11, "bold"), command= getVals).grid(
            row= 2, column= 0, columnspan= 2, pady= 30)
        
        Button(center_frame, text= "Don't have an account?\nSign Up here", 
               bg= "#0085CC", fg= "white", font=("Segoe UI", 11, "bold"), width= 20, 
               command= self.open_signup).grid(
                row= 3, column= 0, columnspan= 2, pady= 15)
            
            
    def open_menu(self):
        print("Click here to Sign In")
        
        self.btn1.place_forget()
        self.title_label.place_forget()
        self.sub_label1.place_forget()
        self.sub_label2.place_forget()
        
        self.signin_btn= Button(self.frame1, text= "Sign in here", font= "comicsansma 15 bold", bg= "#7400CC", 
                                fg= "white", command= self.open_signin, padx= 50, pady= 10)
        self.signin_btn.place(relx=0.5, rely=0.9, anchor="center", width= 350, height= 50)
        
    
    
    
    def render_task_cards(self, parent, tasks):
        
        for i, task in enumerate(tasks):
            text= f"{i+1} : {task['Task']}"
            
            if task.get('Target Time'):
                text += f" | {task['Target Time']}"
                
            if task.get("Completed"):
                text += f" | Completed"
            else:
                text += " | Pending"
                
            card= Frame(parent, bg= "#21262D", bd= 1, relief= "flat")
            card.pack(fill= X, padx= 40, pady= 8)
            
            Label(card, text= text, bg= "#21262D", fg= "white", font= ("Segoe UI", 12), pady= 12, padx= 15).pack(fill= X)
        

    
    
    
    
    
    def open_ui_add_task(self):
        
        for widget in self.content.winfo_children():
            widget.destroy()
        
        task_var= StringVar()
        time_var= StringVar()
        
        frm= Frame(self.content, bg= self.content["bg"], bd= 2, relief= SUNKEN)
        frm.pack(expand= True, fill= "both")
        
        Button(frm, text= "Back", bg= "red", command= self.open_dashboard).pack(side= BOTTOM, pady= 30, fill= X)
        Label(frm, text= "Add new Task", bg= "#0D1117", fg= "#22D3EE", font= ("Segoe UI", 24, "bold")).pack(pady= 30)
        
        edit_frm= Frame(frm, bg= self.content["bg"])
        edit_frm.pack(pady= 20)
        
        Label(edit_frm, text= "Task : ", bg= "white", fg= "black").grid(row= 0, column= 0, padx= 15, pady= 15)
        Entry(edit_frm, textvariable= task_var, bg= "white", fg= "black").grid(row= 0, column= 1, padx= 15, pady= 15)
        
        Label(edit_frm, text= "Target Time (HH:MM) : ", bg= "white", fg= "black").grid(row= 1, column= 0, padx= 15, pady= 15)
        Entry(edit_frm, textvariable= time_var, bg= "white", fg= "black").grid(row= 1, column= 1, padx= 15, pady= 15)
        
        def save_this_task():
            
            task= task_var.get().strip()
            time_input= time_var.get().strip()
            
            if not task:
                tmsg.showerror("Error", "Task can't be empty!")
                return
            
            if time_input == "":
                target_time= None
            else:
                try:
                    datetime.strptime(time_input, "%H:%M")
                    target_time= time_input
                except ValueError:
                    tmsg.showerror("Error", "Invalid time format!\nUse HH:MM")
                    return 
            
            self.task_manager.add_task(self.auth.current_user, task, target_time)
            
            tmsg.showinfo("Success", "Task Added Successfully!")
            
            self.open_ui_show_list()
            
            task_var.set("")
            time_var.set("")
            
            
        btn_frm= Frame(frm, bg= self.content["bg"])
        btn_frm.pack(pady= 30)
        
        Button(btn_frm, text="Add Task to List", command=save_this_task, bg= "#10B981", fg= "white", font= ("Segoe UI", 12, "bold"), width= 15, height= 2, relief= "flat", cursor= "hand2").pack(side= LEFT, padx=15)





    def open_ui_show_list(self):
        
        for widget in self.content.winfo_children():
            widget.destroy()
        
        frm= Frame(self.content, bg= "#0D1117")
        frm.pack(expand=True, fill="both")
        
        Label(frm,text="Task List",bg="#0D1117",fg="#22D3EE",font=("Segoe UI", 18, "bold")).pack(pady=(30, 10))
        
        tasks= self.task_manager.show_list()
        if len(tasks) == 0:
            tmsg.showerror("Empty List", "No tasks found!")
            return
        
        self.render_task_cards(frm, tasks)
        
        Button(frm, text= "Back", bg= "red", command= self.open_dashboard).pack(side= BOTTOM, pady= 30, fill= X)
            
            
            
            
            
    def open_ui_remove_task(self):
        
        for widget in self.content.winfo_children():
            widget.destroy()
        
        tasks= self.task_manager.show_list()
        
        if not tasks:
            tmsg.showerror("Empty", "Empty Task file.")
            return

        
        frm= Frame(self.content, bg= self.content["bg"])
        frm.pack(expand= True, fill= "both")
        Label(frm, text= "Remove Task", bg= "#0D1117", fg= "#69EF44", font= ("Segoe UI", 24, "bold")).pack(pady= 25)
        frm.config(borderwidth=2, relief=RAISED)
        
        Button(frm, text= "Back", bg= "red", command= self.open_dashboard).pack(side= BOTTOM, pady= 30, fill= X)
        
        if len(tasks) == 0:
            tmsg.showinfo("Task List","No task found.\nAdd new tasks.")
            Button(frm, text= "Add Task", bg= "#0300CC", command= self.open_ui_add_task).pack(pady= 30, fill= X)
            return 
        
        self.render_task_cards(frm, tasks)
        
        Label(frm,text="Select task number to remove",bg="#0D1117",fg="#22D3EE",font=("Segoe UI", 15, "bold")).pack(pady=(25, 10))
        
        edit_frm= Frame(frm, bg= self.content["bg"])
        edit_frm.pack(pady= 20)
        
        num_var= StringVar()
        
        Label(edit_frm, text= "Enter the task serial number", bg= "#CC8100", fg= "#F0F0F6").grid(row= 0, column= 0)
        Entry(edit_frm, textvariable= num_var, bg= "#30363D", fg= "#F0F0F6", insertbackground= "white", font= ("Segoe UI", 12), width= 10, relief= "flat").grid(row=0, column= 1)


        def delete_this_task():
            
            try:
                num= int(num_var.get())
            except ValueError:
                tmsg.showerror("Error", "Enter a valid number!")
                return 
            
            result= self.task_manager.remove_task(self.auth.current_user, num-1)
            
            if result:
                tmsg.showinfo("Success", "Task removed successfully.")
                frm.destroy()
                self.open_ui_show_list()
                
            else:
                tmsg.showerror("Error", "Enter valid input!")
            
            num_var.set("")
            
        btn_frm= Frame(frm, bg= self.content["bg"])
        btn_frm.pack(pady= 10)
        
        Button(btn_frm, text="Remove", command=delete_this_task, bg= "#230FA7", fg= "white", font= ("Segoe UI", 12, "bold"), width= 15, height= 2, relief= "flat", cursor= "hand2").pack(side= LEFT, padx=15)
        Button(btn_frm, text= "Back", command= self.open_dashboard, bg= "#EF4444", fg= "white", font= ("Segoe UI", 12, "bold"), width= 15, height= 2, relief= "flat", cursor= "hand2").pack(side= LEFT, padx=15)



    
    
    def open_ui_update_task(self):
        
        for widget in self.content.winfo_children():
            widget.destroy()
        
        tasks= self.task_manager.show_list()
        
        if len(tasks) == 0:
            tmsg.showinfo("Error", "Empty Task file.")
            return
            
        frm= Frame(self.content, bg= self.content["bg"])
        frm.pack(expand= True, fill= "both")
        Label(frm, text= "Update Task", bg= "#5B0F7B", fg= "#D4D7CC", font= ("Segoe UI", 24, "bold")).pack(pady= 25)
        frm.config(borderwidth=2, relief=RAISED)
        
        
        if len(tasks) == 0:
            tmsg.showinfo("Task List","No task found.\nAdd new tasks.")
            Button(frm, text= "Add Task", bg= "#0300CC", command= lambda: self.open_ui_add_task()).pack(pady= 30, fill= X)
            return 
        
        
        self.render_task_cards(frm, tasks)

        input_frm= Frame(frm, bg= self.content["bg"])
        
        Label(frm,text="Edit Task Details",bg="#0D1117",fg="#22D3EE",font=("Segoe UI", 18, "bold")).pack(pady=(30, 10))
        
        input_frm.pack(pady= 20)
        
        num_var= StringVar()
        task_var= StringVar()
        time_var= StringVar()
        
        Label(input_frm, text= "Enter the task serial number", bg= "#0d1117", fg= "white", font= ("Segoe UI", 12, "bold")).grid(row= 0, column= 0)
        Entry(input_frm, textvariable= num_var, bg= "#30363D", fg= "white", font= ("Segoe UI", 12),insertbackground= "white", relief= "flat", width= 25).grid(row= 0, column= 1, padx= 15, pady= 15)
        
        Label(input_frm, text= "Enter new task : ", bg= "#0d1117", fg= "white", font= ("Segoe UI", 12, "bold")).grid(row= 1, column= 0)
        Entry(input_frm, textvariable= task_var, bg= "#30363D", fg= "white", font= ("Segoe UI", 12),insertbackground= "white", relief= "flat", width= 25).grid(row= 1, column= 1, padx= 15, pady= 15)
        
        Label(input_frm, text= "Enter target time (HH:MM) or skip : ", bg= "#0d1117", fg= "white", font= ("Segoe UI", 12, "bold")).grid(row= 2, column= 0)
        Entry(input_frm, textvariable= time_var, bg= "#30363D", fg= "white", font= ("Segoe UI", 12),insertbackground= "white", relief= "flat", width= 25).grid(row= 2, column= 1, padx= 15, pady= 15)
        

        def update_this_task():
            
            try:
                idx = int(num_var.get())
            except ValueError:
                tmsg.showinfo("Error", "Enter a valid integer!")
                return
            
            if not (1 <= idx <= len(tasks)):
                tmsg.showerror("Error", "Invalid task number!")
                return
            
            new_task= task_var.get().strip()
            t= time_var.get().strip()
            
            if not new_task:
                tmsg.showerror("Error", "Task can't be empty!")
                return

            if t == "":
                target_time= None
            else:
                try:
                    datetime.strptime(t, "%H:%M")
                    target_time= t
                except ValueError:
                    tmsg.showerror("Error", "Invalid time format!")
                    return
       
            result= self.task_manager.update_task(self.auth.current_user, idx-1, new_task, target_time)
            
            if result:
                tmsg.showinfo("Success", "Task Updated Successfully!")
                self.open_ui_show_list()
            else:
                tmsg.showerror("Error", "Failed to update task!")
            
        btn_frm= Frame(frm, bg= self.content["bg"])
        btn_frm.pack(pady= 30)
        
        Button(btn_frm, text="Update", command=update_this_task, bg= "blue", fg= "white", font= ("Segoe UI", 12, "bold"), width= 15, height= 2, relief= "flat", cursor= "hand2").pack(side= LEFT, padx=15)
        Button(btn_frm, text= "Back", command= self.open_dashboard, bg= "#EF4444", fg= "white", font= ("Segoe UI", 12, "bold"), width= 15, height= 2, relief= "flat", cursor= "hand2").pack(side= LEFT, padx=15)

    
    
    
    
    def open_ui_reset_priority(self):
        
        for widget in self.content.winfo_children():
            widget.destroy()
        
        tasks= self.task_manager.show_list()
        if len(tasks) == 0:
            tmsg.showerror("Empty", "No task found.")
            return
        
        frm= Frame(self.content, bg= self.content["bg"])
        frm.pack(expand= True, fill= "both")
        frm.config(borderwidth=2, relief=RAISED)
        
        self.task_manager.reset_priority(self.auth.current_user)
        tasks= self.task_manager.show_list()

        tmsg.showinfo("Sorted","Tasks have been sorted by priority:")
        
        self.render_task_cards(frm, tasks)
            
        Button(frm,text="Back",bg="red",fg="white",command=self.open_dashboard).pack(side=BOTTOM, pady=30, fill=X)
            
    
    
    
    
    def open_ui_reminder(self):   
        
        if hasattr(self, "clock_job"):
            try:
                self.content.after_cancel(self.clock_job)
            except ValueError:
                pass
            self.clock_job= None
        
        for widget in self.content.winfo_children():
            widget.destroy()

        tasks= self.task_manager.show_list()
        
        if len(tasks) == 0:
            tmsg.showerror("Error", "Empty tasks file!")
            return
            
        frm= Frame(self.content, bg= self.content["bg"])
        frm.pack(expand= True, fill= "both")
        frm.config(borderwidth=2, relief=RAISED)
        
        Button(frm, text= "Back", bg= "red", fg= "white", command= self.open_dashboard).pack(side= BOTTOM, pady= 30, fill= X)
        
        self.render_task_cards(frm, tasks)
       
        entry_frm= Frame(frm, bg= self.content["bg"])
        entry_frm.pack()
        
        num_var= StringVar()
        
        Label(entry_frm, text= "Enter the task serial no.", bg= self.content["bg"], fg= "white").pack(pady= 15)
        Entry(entry_frm, textvariable= num_var).pack(pady= 8)

        def start_alarm():
            try:
                idx= int(num_var.get())-1
            except ValueError:
                tmsg.showerror("Error", "Enter a valid input!")
                return
            
            entry_frm.destroy()
        
            def check_alarm():
                result= self.task_manager.reminder(idx)
                
                if result == "Empty":
                    tmsg.showerror("Error", "Empty task file!")
                    return

                if result == "Invalid":
                    tmsg.showerror("Error", "Invalid task number!")
                    return

                if result == "No Target time available.":
                    tmsg.showerror("Error", "No target time available!")
                    return
                
                if result["Status"] == "ring":
                    if hasattr(self, "clock_job"):
                        frm.after_cancel(self.clock_job)
                        
                    tmsg.showinfo("Alarm", f"⏰ Time for {result['Task']['Task']}")
                    return
                
                self.clock_job= frm.after(1000, check_alarm)
                
            check_alarm()
                
        Button(entry_frm, text= "Set Reminder", command= start_alarm).pack(pady= 20)
    
    
    
    
    
    def open_ui_reset(self):
        
        for widget in self.content.winfo_children():
            widget.destroy()
        
        tasks= self.task_manager.show_list()
        
        if len(tasks) == 0:
            tmsg.showerror("Error", "Empty tasks file!")
            return
        
        ans= tmsg.askyesno("Confirm", "Do you want to reset your tasks?")
        
        if ans:
            conf= tmsg.askyesno("Warning", "⚠️ By clicking 'Yes' all your tasks will be removed.\n Click 'Yes' to remove all your tasks and 'No' to return .")
                
            if conf:
                msg= self.task_manager.reset(self.auth.current_user)
                tmsg.showinfo("Success", msg)
                
                # F.pack(expand= True)
                
            else:
                tmsg.showinfo("Cancelled", "Reset Cancelled.")
        else:
            tmsg.showinfo("Cancelled", "Reset Cancelled.")
            
        frm= Frame(self.content, bg= self.content["bg"])
        frm.pack(expand= True, fill= "both")
        
        Label(frm,text="Empty task file",bg="black",fg="white").pack(side=TOP, pady=30, padx= 30)
        Button(frm,text="Click to Add Task",bg="green",fg="white",command=self.open_ui_add_task).pack(pady=30, padx= 30)
        
        Button(frm,text="Back",bg="red",fg="white",command=self.open_dashboard).pack(side=BOTTOM, pady=30, fill=X)
            
            
            
            
            
    def open_ui_mark_complete(self):
        
        for widget in self.content.winfo_children():
            widget.destroy()

        tasks = self.task_manager.show_list()

        if len(tasks) == 0:
            tmsg.showerror( "Empty", "No tasks found!")
            return

        frm = Frame( self.content, bg="#0D1117")
        frm.pack(expand=True,fill="both")

        title = Label( frm, text="Mark Task as Completed", bg="#161B22", fg="#22C55E", font=("Segoe UI", 18, "bold"), pady=15)
        title.pack(fill=X)

        list_frame = Frame(frm,bg="#0D1117")
        list_frame.pack(pady=30)

        self.render_task_cards(frm, tasks)
        
        input_frame = Frame(frm,bg="#0D1117")
        input_frame.pack(pady=30)

        num_var = StringVar()

        Label(input_frame,text="Enter Task Number",bg="#0D1117",fg="white",font=("Segoe UI", 13, "bold")).grid(row=0,column=0,padx=10,pady=10)

        Entry(input_frame,textvariable=num_var,font=("Segoe UI", 12),width=10).grid(row=0,column=1,padx=10,pady=10)

        def complete_task():
            try:
                idx = int(num_var.get()) - 1
                
            except ValueError:
                tmsg.showerror("Error","Enter a valid task number!")
                return

            result = self.task_manager.mark_completed(self.auth.current_user,idx)

            if result:
                tmsg.showinfo("Success","Task marked as completed.")
                frm.destroy()
                self.open_ui_mark_complete()
                
            else:
                tmsg.showerror("Error","Invalid task number!")
                
        btn_frame = Frame(frm,bg="#0D1117")
        btn_frame.pack(pady=20)

        Button(btn_frame,text="Mark Completed",bg="#22C55E",fg="white",font=("Segoe UI", 12, "bold"),padx=20,pady=10,relief="flat",cursor="hand2",command=complete_task).pack(side=LEFT,padx=15)
        
        Button(btn_frame,text="Back",bg="#DC2626",fg="white",font=("Segoe UI", 12, "bold"),padx=20,pady=10,relief="flat",cursor="hand2",command=self.open_dashboard).pack(side=LEFT,padx=15)