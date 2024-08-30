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
        ├── main.py (The main application which is going to run)
        ├── UserDataBank.py
        
        ├── lib/* {import self create module}
        ├── icon/*{all the icons are stored here}
        ├── cache/* {To store the data of the user who is logged in}
        ├── logs/
        ├── info/
        ├── database/* 
        ├── config/*{This will contain a json file with some variables from which u can modify APP.(like background color geometry)}
    
        ├──.........{more dir.. will be there as its grow.}

! There will classes UserDataBank, SignInXert and rest are part of the SignInXert.
    *The UserDataBank: use The lib.FileAccess to read and write the data to store the use data continuously.
        *And also to Use as to get the data from the json file.
    *SignInXert: This is the main application will be most likely to as a route and controll all the pages.

start:
    when it boot it checks file for which user was logged in.
    Then it calls the HomePage if there is a user logged in.
    Else it calls the LoginPage if there is no user logged in.

conditions:
    ? For Create Account
        If user dont have a account then You can create Just clicking the button.
    



* This will be a GUI application using Tkinter in Python.
* Note: This is just a basic version and might need to be expanded upon.
* All will be slowly add in future versions. This version only going to have a very small chuck of it.
* This is re-creating from the original dev version as a cheak and a self learning of GUI in python.



@update
    UPDATE [28-08-2024 - 15:40]: First update write the documentation as big comment and create the base application. 
    UPDATE [29-08-2024 - 10:30]: Adjusting the file paths & structures.Added lil documentation in the big comments.
        -> Implemented json config Directly from the file using FileAccess module.Set a default value to all the important files
    UPDATE[30-08-2024 -  15:15 -> 18:00 ]: Change the structure of config_app.json and also update that in the main srcipt.
        -> Update the HomePage UI and with a working logout support.
        ->Implemented cache directory and the current logged user also.

@problem
    *[30-08-24] The logout need to be better. But the HomePage's logout and re-read the name of the user need to fix
"""
# import
import tkinter as tk
from tkinter import messagebox
# My own module or Classes
from UserDataBank import UserDataBank
from lib.FileAccess import FileAccess

class SignInXert(tk.Tk):
    def __init__(self, config_filepath: str = "./config/config_app.json"):
        super().__init__()

        # Default values
        default_settings = {
            "title": "SignInXert Dev",
            "geometry": "360x620",
            "font_family": "Arial",
            "background_color": "#FFFFFF",
            "icons": {"root": "./icon",
                      "app_logo": "/app.icon"
                    },
            "cache": {"root": "./cache",
                      "logged": "/logged_user.json"
                    }
        }
        default_filepaths = {
            "users_data": "database/data.json",
            "logs": "logs/log.txt",
            "stater": "SignInXert_Info.txt"
        }

        # Attempt to load configuration
        try:
            file_obj = FileAccess(config_filepath)
            config_data = file_obj.readData()[0]
            # print(config_data)

            # Extract settings and file paths from config_data
            settings = config_data.get('setting', default_settings)
            filepaths = config_data.get('filepath', default_filepaths)

            # Update defaults with settings from file
            TITLE = settings.get('title', default_settings["title"])
            GEOMETRY = settings.get('geometry', default_settings["geometry"])
            FontFamily = settings.get('font_family', default_settings["font_family"])
            background_color = settings.get('background_color', default_settings["background_color"])
            icons = settings.get('icons', default_settings["icons"])
            cache = settings.get('cache', default_settings["cache"])
            print(cache)
            # Extract file paths
            users_data_path = filepaths.get('users_data', default_filepaths["users_data"])

        except (KeyError, IndexError, TypeError) as e:
            print(f"Configuration error: {e}")
            # Use default values if there is an issue with the config file
            TITLE = default_settings["title"]
            GEOMETRY = default_settings["geometry"]
            FontFamily = default_settings["font_family"]
            background_color = default_settings["background_color"]
            icons = default_settings["icons"]
            cache = default_settings["cache"]
            users_data_path = default_filepaths["users_data"]
        self.logged_user_path = cache['root']+cache['logged'] 

        # Set application properties
        self.title(TITLE)
        self.geometry(GEOMETRY)
        self.configure(bg=background_color)

        # Create an instance of UserDataBank to manage user data with the path from config
        self.databank = UserDataBank(users_data_path)

        # Store settings and file paths for other pages
        self.settings = settings
        self.filepaths = filepaths

        # Dictionary to store frames for easy navigation
        self.frames = {}

        # Add all the frames (pages) to the dictionary
        for F in (LoginPage, CreateUserPage, SettingPage, HomePage):
            page_name = F.__name__
            
            if page_name == "LoginPage":
                frame = F(parent=self, controller=self,user_data_path=self.logged_user_path)
            elif page_name == "CreateUserPage":
                frame = F(parent=self, controller=self)
            elif page_name == "SettingPage":
                frame = F(parent=self, controller=self)
            elif page_name == "HomePage":
                frame = F(parent=self, controller=self,user_data_path=self.logged_user_path)
            else:
                raise Exception("Error[404]: page does't exist.")


            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Start the application with the login page
        file_obj = FileAccess(self.logged_user_path)
        user_data = file_obj.readData()
        print(user_data)
        if not user_data:
            self.show_frame("LoginPage")
        else:
            self.show_frame("HomePage")
        
        

    def show_frame(self, page_name):
        """Bring the frame with the given page_name to the front"""
        frame = self.frames[page_name]
        frame.tkraise()

class LoginPage(tk.Frame):
    def __init__(self, parent, controller, color_scheme=None,user_data_path:str = None):
        super().__init__(parent)
        self.controller = controller
        self.Databank_instance = self.controller.databank
        self.user_data_path = user_data_path

        # Default color scheme
        self.color_scheme = color_scheme or {
            "bg": "#f0f0f0",
            "button_bg": "#4CAF50",
            "button_fg": "white",
            "entry_bg": "#e0e0e0",
            "entry_fg": "#333333",
            "label_fg": "#000000",
        }
        self.configure(bg=self.color_scheme["bg"])

        # Configure grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Create and style widgets
        self.label = tk.Label(self, text="Login", font=("Arial", 20, "bold"), bg=self.color_scheme["bg"], fg=self.color_scheme["label_fg"])
        self.label.grid(row=0, column=0, columnspan=2, pady=20, sticky="n")

        self.uid_label = tk.Label(self, text="User ID", font=("Arial", 12), bg=self.color_scheme["bg"], fg=self.color_scheme["label_fg"])
        self.uid_label.grid(row=1, column=0, sticky="e", padx=10)

        self.uid_entry = tk.Entry(self, font=("Arial", 12), bg=self.color_scheme["entry_bg"], fg=self.color_scheme["entry_fg"], bd=2, relief="groove")
        self.uid_entry.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

        self.pass_label = tk.Label(self, text="Password", font=("Arial", 12), bg=self.color_scheme["bg"], fg=self.color_scheme["label_fg"])
        self.pass_label.grid(row=2, column=0, sticky="e", padx=10)

        self.pass_entry = tk.Entry(self, show="*", font=("Arial", 12), bg=self.color_scheme["entry_bg"], fg=self.color_scheme["entry_fg"], bd=2, relief="groove")
        self.pass_entry.grid(row=2, column=1, pady=10, padx=10, sticky="ew")

        self.login_button = tk.Button(self, text="Login", font=("Arial", 12, "bold"), command=self.check_login, bg=self.color_scheme["button_bg"], fg=self.color_scheme["button_fg"], relief="raised")
        self.login_button.grid(row=3, column=0, columnspan=2, pady=20, padx=10, sticky="ew")

        self.create_button = tk.Button(self, text="Create Account", font=("Arial", 12), command=lambda: controller.show_frame("CreateUserPage"), bg="#2196F3", fg="white", relief="raised")
        self.create_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        self.back_button = tk.Button(self, text="Settings", font=("Arial", 12), command=lambda: controller.show_frame("SettingPage"), bg="#FFC107", fg="black", relief="raised")
        self.back_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        """Handle window resize to keep the layout responsive."""
        for widget in self.winfo_children():
            widget.grid_configure(padx=max(event.width // 50, 10), pady=max(event.height // 50, 10))
            widget.update_idletasks()

    def check_login(self):
        """Check if the user credentials are valid using the UserDataBank login method."""
        uid = self.uid_entry.get()
        password = self.pass_entry.get()

        if self.Databank_instance.logging(uid, password):
            # Fetch user data
            user_data = self.Databank_instance.search_user_data(uid)

            # Prepare data for saving
            data_to_save = {
                "logged": {
                    "uid": user_data.get("uid"),
                    "password": user_data.get("password"),
                    "name": user_data.get("name"),
                    "email": user_data.get("email"),
                    "age": user_data.get("age")
                }
            }

            # Save user data
            file_obj = FileAccess(self.user_data_path)
            file_obj.WriteData()
            file_obj.addData(data_to_save)

            name = user_data.get('name', 'User')
            messagebox.showinfo("Login Successful", f"Welcome {name}!")
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
        self.controller.databank.add_user(uid, password, fullname, age,email)

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
    def __init__(self, parent, controller, user_data_path:str=None):
        super().__init__(parent)
        self.controller = controller
        self.user_data_path = user_data_path
        
        # Load user data
        file_obj = FileAccess(user_data_path)
        user_data = file_obj.readData()
        if not user_data:
            user_data = {}
        else:
            user_data = user_data[0].get('logged', {})
        print(user_data)
        
        # Extract user data
        self.uid = user_data.get('uid', 'N/A')
        self.name = user_data.get('name', 'N/A')
        self.email = user_data.get('email', 'N/A')
        self.age = user_data.get('age', 'N/A')

        # Modern UI setup
        self.configure(bg="#F7F9FC")

        # Title label for the home page
        title_frame = tk.Frame(self, bg="#F7F9FC")
        title_frame.pack(pady=20)
        title_label = tk.Label(title_frame, text="Home Page", bg="#F7F9FC", font=("Arial", 20, "bold"))
        title_label.pack()

        # User profile display
        profile_frame = tk.Frame(self, bg="#FFFFFF", padx=20, pady=20, relief="groove", borderwidth=2)
        profile_frame.pack(pady=10, fill="x")

        tk.Label(profile_frame, text="User Profile", font=("Arial", 16, "bold"), bg="#FFFFFF").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(profile_frame, text="User ID:", font=("Arial", 12), bg="#FFFFFF").grid(row=1, column=0, sticky="e")
        tk.Label(profile_frame, text=self.uid, font=("Arial", 12), bg="#FFFFFF").grid(row=1, column=1, sticky="w")

        tk.Label(profile_frame, text="Name:", font=("Arial", 12), bg="#FFFFFF").grid(row=2, column=0, sticky="e")
        tk.Label(profile_frame, text=self.name, font=("Arial", 12), bg="#FFFFFF").grid(row=2, column=1, sticky="w")

        tk.Label(profile_frame, text="Email:", font=("Arial", 12), bg="#FFFFFF").grid(row=3, column=0, sticky="e")
        tk.Label(profile_frame, text=self.email, font=("Arial", 12), bg="#FFFFFF").grid(row=3, column=1, sticky="w")

        tk.Label(profile_frame, text="Age:", font=("Arial", 12), bg="#FFFFFF").grid(row=4, column=0, sticky="e")
        tk.Label(profile_frame, text=self.age, font=("Arial", 12), bg="#FFFFFF").grid(row=4, column=1, sticky="w")

        # Buttons
        button_frame = tk.Frame(self, bg="#F7F9FC")
        button_frame.pack(pady=10)

        settings_button = tk.Button(button_frame, text="Settings", command=lambda: controller.show_frame("SettingPage"), font=("Arial", 12), bg="#007BFF", fg="white", relief="raised")
        settings_button.grid(row=0, column=0, padx=10)

        logout_button = tk.Button(button_frame, text="Logout", command=self.logout, font=("Arial", 12), bg="#DC3545", fg="white", relief="raised")
        logout_button.grid(row=0, column=1, padx=10)

    def logout(self):
        file_obj = FileAccess(self.user_data_path)
        """Handle user logout with confirmation and data removal."""
        # Show confirmation dialog
        if messagebox.askyesno("Logout Confirmation", "Are you sure you want to logout?"):
            # Remove user data
            file_obj.WriteData()
            # Show a logout success message (optional)
            messagebox.showinfo("Logout", "You have been logged out successfully.")
            
            # Navigate back to the login page
            self.controller.show_frame("LoginPage")

            
if __name__ == "__main__":
    app = SignInXert()
    app.mainloop()