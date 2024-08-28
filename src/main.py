"""
    @author Nikhil Karmakar
    @since 2024
    @version 2.0.1
    @license MIT
    
* Dev version : Recreating from old version(dev0.2.1).
    
$               SignInXert: Its a basic authentication & login system 

when it will start it will ask use for login with user UID & Password.
And a create a new user account by asking the full name , email , age and password.
After putting all the values properly Its will show as verification that all of your datas are correct or not.
This is Going to use OOPs. for Multiple Pages/Framers like Login, creations , profile and a example socila or e-commerce type application.


File Structure:
./ {Root}
    ├── src
        ├──main.py (The main application which is going to run)
        
        ├── lib/* {import self create module}
        ├── icon/*{all the icons are stored here}
        ├── cache/* {To store the data of the user who is logged in}
        ├── config/*{This will contain a json file with some variables from which u can modify APP.(like background color geometry)}
    
        ├──.........{more dir.. will be there as its grow.}

TODO: There will classes UserDataBank, SignInXert and rest are part of the SignInXert.
    *The UserDataBank: use The lib.FileAccess to read and write the data to store the use data continuously.
        *And also to Use as to get the data from the json file.
    *SignInXert: This is the main application will be most likely to as a route and controll all the pages.

* This will be a GUI application using Tkinter in Python.
* Note: This is just a basic version and might need to be expanded upon.
* All will be slowly add in future versions. This version only going to have a very small chuck of it.
* This is re-creating from the original dev version as a cheak and a self learning of GUI in python.


@update
    UPDATE [28-06-2024 - 15:40]: First update write the documentation as big comment and create the base application. 
"""

# imports 

import tkinter as tk
from tkinter import messagebox
from lib.FileAccess import FileAccess



class UserDataBank:
    def __init__(self, filepath="database/data.json"):
        self.File = FileAccess(filepath)
        try:
            self.userData = self.File.readData()
            if self.userData == [-1]:
                self.File.CreateFile()
                print("NEW FILE HAD BEEN CREATED")
        except Exception as e:
            print(f"Error reading data: {e}")
        self.readingData()

    def readingData(self):
        self.user_uid_stored, self.user_age_stored, self.user_Fullname_stored, self.user_pass_stored, self.user_email_stored = [], [], [], [], []
        try:
            for data in self.userData:
                self.user_uid_stored.append(data['uid'])
                self.user_pass_stored.append(data['password'])
                self.user_Fullname_stored.append(data['name'])
                self.user_age_stored.append(data.get('age', ''))
                self.user_email_stored.append(data.get('email', ''))
        except Exception as e:
            print(f"Error reading data: {e}")

        
    
    def getData(self, DataType=None) -> list:
        if DataType == "uid":
            return self.user_uid_stored
        elif DataType == "pass":
            return self.user_pass_stored
        elif DataType in ["fullname", "name"]:
            return self.user_Fullname_stored
        elif DataType == "age":
            return self.user_age_stored
        elif DataType == "email":
            return self.user_email_stored
        elif DataType == "login":
            return self.user_uid_stored, self.user_pass_stored
        else:
            return self.user_uid_stored, self.user_pass_stored, self.user_Fullname_stored, self.user_age_stored, self.user_email_stored

    def add_user(self, add_user_name: str,
                 add_user_pass: str,
                 add_userFullName: str,
                 add_user_age: str = None,
                 add_user_email_ID: str = None
                 ) -> None:
        newEntry = {
            "uid": add_user_name,
            "password": add_user_pass,
            "name": add_userFullName,
            "email": add_user_email_ID,
            "age": add_user_age
        }

        print("Added entry")
        self.File.addData(newEntry)
        self.userData = []
        self.userData = self.File.readData()
        self.readingData()

    def search_user_data(self, uid: str):
        """Search for a user by UID and return the full JSON data"""
        for data in self.userData:
            if data['uid'] == uid:
                return data
        return None



class SignInXert(tk.Tk):
    def __init__(self):
        super().__init__()
        TITLE = "SignInXert v0.2.1 DEV"
        self.title("SignInXert Dev (v2.1.0)")
        self.geometry("360x620")
        
        # Create an instance of UserDataBank to manage user data
        self.databank = UserDataBank()

        # Dictionary to store frames for easy navigation
        self.frames = {}
        
        # Add all the frames (pages) to the dictionary
        for F in (LoginPage, CreateUserPage, SettingPage, HomePage):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Start the application with the login page
        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        """Bring the frame with the given page_name to the front"""
        frame = self.frames[page_name]
        frame.tkraise()

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.Databank_instance = self.controller.databank

        # Configure grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Create and style widgets
        self.label = tk.Label(self, text="Login", font=("Arial", 20, "bold"), bg="#f0f0f0")
        self.label.grid(row=0, column=0, pady=20, sticky="n")

        self.uid_label = tk.Label(self, text="User ID", font=("Arial", 12), bg="#f0f0f0")
        self.uid_label.grid(row=1, column=0, sticky="e", padx=10)

        self.uid_entry = tk.Entry(self, font=("Arial", 12), bg="#e0e0e0", fg="#333333", bd=2, relief="groove")
        self.uid_entry.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

        self.pass_label = tk.Label(self, text="Password", font=("Arial", 12), bg="#f0f0f0")
        self.pass_label.grid(row=2, column=0, sticky="e", padx=10)

        self.pass_entry = tk.Entry(self, show="*", font=("Arial", 12), bg="#e0e0e0", fg="#333333", bd=2, relief="groove")
        self.pass_entry.grid(row=2, column=1, pady=10, padx=10, sticky="ew")

        self.login_button = tk.Button(self, text="Login", font=("Arial", 12, "bold"), command=self.check_login, bg="#4CAF50", fg="white", relief="raised")
        self.login_button.grid(row=3, column=0, columnspan=2, pady=20, padx=10, sticky="ew")

        self.create_button = tk.Button(self, text="Create Account", font=("Arial", 12), command=lambda: controller.show_frame("CreateUserPage"), bg="#2196F3", fg="white", relief="raised")
        self.create_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        self.back_button = tk.Button(self, text="Settings", font=("Arial", 12), command=lambda: controller.show_frame("SettingPage"), bg="#FFC107", fg="black", relief="raised")
        self.back_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

    def check_login(self):
        """Check if the user credentials are valid"""
        uid = self.uid_entry.get()
        password = self.pass_entry.get()
        user_ids, passwords = self.Databank_instance.getData('login') # @return uid & password
        search_user_data = self.Databank_instance.search_user_data(uid)
        retrieve_user_name = search_user_data['name']

        if uid in user_ids and password == passwords[user_ids.index(uid)]:
            messagebox.showinfo("Login Successful", f"Welcome {retrieve_user_name}!")
            self.controller.show_frame("HomePage")  # Navigate to home page after successful login
        else:
            messagebox.showerror("Login Failed", "Invalid UID or Password")

class CreateUserPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Create and style widgets
        self.label = tk.Label(self, text="Create Account", font=("Arial", 20, "bold"), bg="#f0f0f0")
        self.label.grid(row=0, column=0, columnspan=2, pady=20, sticky="n")

        self.fullname_label = tk.Label(self, text="Full Name", font=("Arial", 12), bg="#f0f0f0")
        self.fullname_label.grid(row=1, column=0, sticky="e", padx=10)

        self.fullname_entry = tk.Entry(self, font=("Arial", 12), bg="#e0e0e0", fg="#333333", bd=2, relief="groove")
        self.fullname_entry.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

        self.uid_label = tk.Label(self, text="User ID", font=("Arial", 12), bg="#f0f0f0")
        self.uid_label.grid(row=2, column=0, sticky="e", padx=10)

        self.uid_entry = tk.Entry(self, font=("Arial", 12), bg="#e0e0e0", fg="#333333", bd=2, relief="groove")
        self.uid_entry.grid(row=2, column=1, pady=10, padx=10, sticky="ew")

        self.email_label = tk.Label(self, text="Email", font=("Arial", 12), bg="#f0f0f0")
        self.email_label.grid(row=3, column=0, sticky="e", padx=10)

        self.email_entry = tk.Entry(self, font=("Arial", 12), bg="#e0e0e0", fg="#333333", bd=2, relief="groove")
        self.email_entry.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

        self.age_label = tk.Label(self, text="Age", font=("Arial", 12), bg="#f0f0f0")
        self.age_label.grid(row=4, column=0, sticky="e", padx=10)

        self.age_entry = tk.Entry(self, font=("Arial", 12), bg="#e0e0e0", fg="#333333", bd=2, relief="groove")
        self.age_entry.grid(row=4, column=1, pady=10, padx=10, sticky="ew")

        self.pass_label = tk.Label(self, text="Password", font=("Arial", 12), bg="#f0f0f0")
        self.pass_label.grid(row=5, column=0, sticky="e", padx=10)

        self.pass_entry = tk.Entry(self, show="*", font=("Arial", 12), bg="#e0e0e0", fg="#333333", bd=2, relief="groove")
        self.pass_entry.grid(row=5, column=1, pady=10, padx=10, sticky="ew")

        self.create_button = tk.Button(self, text="Create Account", font=("Arial", 12, "bold"), command=self.create_account, bg="#4CAF50", fg="white", relief="raised")
        self.create_button.grid(row=6, column=0, columnspan=2, pady=20, padx=10, sticky="ew")

        self.back_button = tk.Button(self, text="Back to Login", font=("Arial", 12), command=lambda: controller.show_frame("LoginPage"), bg="#FFC107", fg="black", relief="raised")
        self.back_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

    def create_account(self):
        """Create a new user account"""
        fullname = self.fullname_entry.get()
        uid = self.uid_entry.get()
        email = self.email_entry.get()
        age = self.age_entry.get()
        password = self.pass_entry.get()

        # Validate mandatory fields
        if not (fullname and uid and password and email):
            messagebox.showerror("Error", "Full Name, User ID, Email, and Password are mandatory!")
            return

        # Check if the User ID already exists
        user_ids, _ = self.controller.databank.getData('login')
        if uid in user_ids:
            messagebox.showerror("Error", "User ID already exists!")
            return

        # Add the user to the databank
        self.controller.databank.add_user(uid, password, fullname, age)

        # Notify the user and redirect to the login page
        messagebox.showinfo("Success", "Account created successfully!")
        self.controller.show_frame("LoginPage")
class SettingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        my_icon_path = "icon\\arrow3.png"
        self.controller = controller

        # Title label for the settings page
        label = tk.Label(self, text="Settings Page", bg="#CACFD8", font=("Arial", 15, "bold"))
        label.pack(side="top", fill="x", pady=5)

        # Try loading an icon image for the button
        # try:
        #     self.my_icon = tk.PhotoImage(file=my_icon_path)
        # except tk.TclError as e:
        #     print(f"Error loading image: {e}")
        #     self.my_icon = None

        # Button with an icon to navigate back to the home page
        # button = tk.Button(self, 
        #                    image=self.my_icon, 
        #                    compound=tk.LEFT, 
        #                    command=lambda: controller.show_frame("HomePage"))
        # button.config(width=32, height=32)  # Adjust button size as needed
        # button.place(y=36)
        self.back_button = tk.Button(self, text="Back to Login", command=lambda: controller.show_frame("LoginPage"))
        self.back_button.pack()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Title label for the home page
        label = tk.Label(self, text="Home Page",bg="#CACFD8",font=("Arial", 15, "bold"))
        label.pack(pady=10)

        # Button to navigate to the settings page
        settings_button = tk.Button(self, text="Settings", command=lambda: controller.show_frame("SettingPage"))
        settings_button.pack()

        # Button to log out and go back to the login page
        logout_button = tk.Button(self, text="Logout", command=lambda: controller.show_frame("LoginPage"))
        logout_button.pack()


if __name__ == "__main__":
    app = SignInXert()
    app.mainloop()