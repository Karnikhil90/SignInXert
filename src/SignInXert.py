"""
    @author Nikhil Karmakar
    @since 0.0.1
    @version 2.0.3
    @license MIT
    
* Dev version : Recreating from old version(dev0.2.1).
    
$               SignInXert: Its a basic authentication & login system 

when it will start it will ask use for login with user UID & Password.
And a create a new user account by asking the full name , email , age and password.
After putting all the values properly Its will show as verification that all of your datas are correct or not.
This is Going to use OOPs. for Multiple Pages/Framers like Login, creations , profile and a example socila or e-commerce type application.


File Structure:
./ {Root}
    
    ├──main.py {work as a driver code. Calles The SignInXert} 
    ├── util/ {INFORMATION for README.md}
    ├── src
    │    ├── SignInXert.py (The main application which is going to run)
    │    ├── UserDataBank.py
    │    ├── __init__.py {!NOT DEFINED.}
    │    
    │    ├── lib/* {import self create module}
    │    ├── icon/*{all the icons are stored here}
    │    ├── cache/* {To store the data of the user who is logged in}
    │    ├── logs/
    │    ├── info/
    │    ├── example/* {Test projects . NOT THE PART OF APPLICATION}
    │    ├── database/* 
    │    ├── config/*{This will contain a json file with some variables from which u can modify APP.(like background color geometry)}
    │    ├──.........{more dir.. will be there as its grow.}
    ├──LISENCE
    ├──README.md
    ├──.gitignore
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
    UPDATE [31-08-2024 - 15:00 -> 16:45]: UPDATE Setting & save changes of settings like background_color and geometry. By directly chnaging the config/config_app.json file.
        -> update the structure little bit. 
        -> Testing run from a main.py file (root/main.py) Of the main application file SignInXert.By adding ./Test ,/example and __init__.py file .
        -> Added a new library file called JsonEditor at src\lib. For changing Json file of config_app.json as I menstion earlier.
         
    
@problem ['*' = fixed]
    [PROBLEM REPORT TIME] : PROBLEM 
    *[30-08-24] The logout need to be better. But the HomePage's logout and re-read the name of the user need to fix
"""
# import
import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk,PhotoImage
# My own module or Classes
from UserDataBank import UserDataBank
from lib.FileAccess import FileAccess
import lib.JsonEditor as J_Editor

class SignInXert(tk.Tk):
    def __init__(self, config_filepath: str = "src/config/config_app.json"):
        super().__init__()
        self.config_filepath = config_filepath
        self.settings = {}
        self.filepaths = {}
        self.logged_user_path = None
        self.databank = None  # Initialize databank as None
        
        self.config_editor = J_Editor.JsonEditor(config_filepath)
        
        self.load_config()
        self.initialize_frames()
        self.start_initial_page()

    def load_config(self):
        """Load configuration values from the specified file."""
        default_settings = {
            "title": "SignInXert Dev",
            "geometry": "360x620",
            "font_family": "Arial",
            "background_color": "#FFFFFF",
            "icons": {"root": "./icon", "app_logo": "/appaaa.icon"},
            "cache": {"root": "./cache", "logged": "/logged_user.json"}
        }
        default_filepaths = {
            "users_data": "database/data.json",
            "logs": "logs/log.txt",
            "stater": "SignInXert_Info.txt"
        }

        try:
            file_obj = FileAccess(self.config_filepath)
            config_data = file_obj.readData()[0]

            self.settings = config_data.get('setting', default_settings)
            self.filepaths = config_data.get('filepath', default_filepaths)

            self.logged_user_path = self.settings['cache']['root'] + self.settings['cache']['logged']

        except (KeyError, IndexError, TypeError) as e:
            print(f"Configuration error: {e}")
            self.settings = default_settings
            self.filepaths = default_filepaths
            self.logged_user_path = default_settings['cache']['root'] + default_settings['cache']['logged']

        # Initialize UserDataBank with the user data path from the config
        users_data_path = self.filepaths.get('users_data', default_filepaths["users_data"])
        self.databank = UserDataBank(users_data_path)

        # Set application properties
        self.title(self.settings['title'])
        self.geometry(self.settings['geometry'])
        self.apply_background_color(color=self.settings['background_color'])
        
        # Set application icon
        self.set_application_icon()

    def set_application_icon(self):
        """Set the application icon."""
        icon_path = self.settings['icons']['root'] + self.settings['icons']['app_logo']
        try:
            # For .ico files
            self.iconbitmap(icon_path)

            # If you have a PNG file, use this instead:
            self.iconphoto(False, tk.PhotoImage(file=icon_path))
        except Exception as e:
            print(f"Error setting application icon: {e}")

    def initialize_frames(self):
        """Initialize and store all the application frames."""
        self.frames = {}

        for PageClass in (LoginPage, CreateUserPage, SettingPage, HomePage):
            page_name = PageClass.__name__

            if page_name in ["LoginPage", "HomePage"]:
                frame = PageClass(parent=self, controller=self, user_data_path=self.logged_user_path)
            else:
                frame = PageClass(parent=self, controller=self)

            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def start_initial_page(self):
        """Determine and show the initial page based on user data availability."""
        file_obj = FileAccess(self.logged_user_path)
        user_data = file_obj.readData()

        if not user_data:
            self.show_frame("LoginPage")
        else:
            self.show_frame("HomePage")

    def show_frame(self, page_name):
        """Bring the specified frame to the front, refreshing data if necessary."""
        frame = self.frames[page_name]
        
        if hasattr(frame, 'refresh_data'):
            frame.refresh_data()

        frame.tkraise()

    def apply_background_color(self, color):
        """Apply the background color to the app and all frames, excluding specific widget types."""
        self.configure(bg=color)

        # Check if frames are initialized
        if hasattr(self, 'frames'):
            for frame_name, frame in self.frames.items():
                frame.configure(bg=color)  # Set background color for the frame itself

                # Apply the color only to widgets that are frames (containers)
                for widget in frame.winfo_children():
                    if isinstance(widget, tk.Frame):  # Only change color for frames
                        widget.configure(bg=color)
                    else:
                        print(f"Skipping widget {widget} - not a frame")
        else:
            print("Frames are not initialized.")


class LoginPage(tk.Frame):
    def __init__(self, parent, controller, color_scheme=None, user_data_path: str = None):
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
        self.uid_entry.bind("<Return>", self.focus_password)  # Bind Enter key to move to password field

        self.pass_label = tk.Label(self, text="Password", font=("Arial", 12), bg=self.color_scheme["bg"], fg=self.color_scheme["label_fg"])
        self.pass_label.grid(row=2, column=0, sticky="e", padx=10)

        self.pass_entry = tk.Entry(self, show="*", font=("Arial", 12), bg=self.color_scheme["entry_bg"], fg=self.color_scheme["entry_fg"], bd=2, relief="groove")
        self.pass_entry.grid(row=2, column=1, pady=10, padx=10, sticky="ew")
        self.pass_entry.bind("<Return>", self.check_login)  # Bind Enter key to trigger login

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

    def focus_password(self, event=None):
        """Move focus to the password field when Enter is pressed in the UID field."""
        self.pass_entry.focus_set()

    def check_login(self, event=None):
        """Check if the user credentials are valid using the UserDataBank login method."""
        uid = self.uid_entry.get()
        password = self.pass_entry.get()
        print(f"DEBUG [LOGIN cheak] : {uid}: {password}")

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
        self.controller = controller
        self.editor = self.controller.config_editor
        self.refresh=controller.load_config()
        # self.editor.print_json()
        # Field Value for updating json config file
        self.GEOMETRY = 'setting.geometry'
        self.BACKGROUND_COLOR = 'setting.background_color'
        

        # Title label for the settings page
        label = tk.Label(self, text="Settings Page", bg="#CACFD8", font=("Arial", 15, "bold"))
        label.pack(side="top", fill="x", pady=5)

        # Back button to navigate back to the HomePage
        self.back_button = tk.Button(self, text="Back", command=lambda: controller.start_initial_page())
        self.back_button.pack(pady=10)

        # Geometry settings label
        geometry_label = tk.Label(self, text="Change App Geometry:", font=("Arial", 12))
        geometry_label.pack(anchor="w", pady=10)

        # Dropdown to select geometry
        self.geometry_var = tk.StringVar(value="300x400")
        geometry_options = ["300x420", "320x500", "400x600"]
        geometry_dropdown = ttk.Combobox(self, textvariable=self.geometry_var, values=geometry_options)
        geometry_dropdown.pack(anchor="w", padx=20)

        # Apply geometry button
        apply_geometry_button = tk.Button(self, text="Apply Geometry", command=self.apply_geometry)
        apply_geometry_button.pack(anchor="w", padx=20, pady=5)

        # Background color settings label
        color_label = tk.Label(self, text="Change Background Color:", font=("Arial", 12))
        color_label.pack(anchor="w", pady=10)

        # Entry for HEX color code
        self.color_entry = tk.Entry(self)
        self.color_entry.pack(anchor="w", padx=20)

        # Dropdown for predefined colors (You can add the actual values later)
        self.color_var = tk.StringVar(value="Select a color")
        color_options = ["#FFFFFF", "#FF5733", "#33FF57"]  # Example colors, you can update these
        color_dropdown = ttk.Combobox(self, textvariable=self.color_var, values=color_options)
        color_dropdown.pack(anchor="w", padx=20, pady=5)

        # Apply color button
        apply_color_button = tk.Button(self, text="Apply Color", command=self.apply_color)
        apply_color_button.pack(anchor="w", padx=20, pady=5)

    def apply_geometry(self):
        geometry = self.geometry_var.get()
        self.editor._update_field(self.GEOMETRY,geometry)
        self.controller.geometry(geometry)
        self.editor._save_json()
        print(f"Geometry changed to {geometry}")

    def apply_color(self):
        color = self.color_entry.get() or self.color_var.get()
        if color:
            self.controller.apply_background_color(color)
            self.editor._update_field(self.BACKGROUND_COLOR,color)
            self.editor._save_json()
            print(f"Background color changed to {color}")
            # self.refresh()
class HomePage(tk.Frame):
    def __init__(self, parent, controller, user_data_path: str = None):
        super().__init__(parent)
        self.controller = controller
        self.user_data_path = user_data_path
        
        # Initialize user data
        self.uid = 'N/A'
        self.name = 'N/A'
        self.email = 'N/A'
        self.age = 'N/A'
        
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
        self.user_id_label = tk.Label(profile_frame, text=self.uid, font=("Arial", 12), bg="#FFFFFF")
        self.user_id_label.grid(row=1, column=1, sticky="w")

        tk.Label(profile_frame, text="Name:", font=("Arial", 12), bg="#FFFFFF").grid(row=2, column=0, sticky="e")
        self.name_label = tk.Label(profile_frame, text=self.name, font=("Arial", 12), bg="#FFFFFF")
        self.name_label.grid(row=2, column=1, sticky="w")

        tk.Label(profile_frame, text="Email:", font=("Arial", 12), bg="#FFFFFF").grid(row=3, column=0, sticky="e")
        self.email_label = tk.Label(profile_frame, text=self.email, font=("Arial", 12), bg="#FFFFFF")
        self.email_label.grid(row=3, column=1, sticky="w")

        tk.Label(profile_frame, text="Age:", font=("Arial", 12), bg="#FFFFFF").grid(row=4, column=0, sticky="e")
        self.age_label = tk.Label(profile_frame, text=self.age, font=("Arial", 12), bg="#FFFFFF")
        self.age_label.grid(row=4, column=1, sticky="w")

        # Buttons
        button_frame = tk.Frame(self, bg="#F7F9FC")
        button_frame.pack(pady=10)

        settings_button = tk.Button(button_frame, text="Settings", command=lambda: controller.show_frame("SettingPage"), font=("Arial", 12), bg="#007BFF", fg="white", relief="raised")
        settings_button.grid(row=0, column=0, padx=10)

        logout_button = tk.Button(button_frame, text="Logout", command=self.logout, font=("Arial", 12), bg="#DC3545", fg="white", relief="raised")
        logout_button.grid(row=0, column=1, padx=10)

    def refresh_data(self):
        """Refresh user data when the page is shown."""
        # Load user data
        file_obj = FileAccess(self.user_data_path)
        user_data = file_obj.readData()
        if not user_data:
            user_data = {}
        else:
            user_data = user_data[0].get('logged', {})

        # Update labels with the latest user data
        self.uid = user_data.get('uid', 'N/A')
        self.name = user_data.get('name', 'N/A')
        self.email = user_data.get('email', 'N/A')
        self.age = user_data.get('age', 'N/A')

        self.user_id_label.config(text=self.uid)
        self.name_label.config(text=self.name)
        self.email_label.config(text=self.email)
        self.age_label.config(text=self.age)

    def logout(self):
        """Handle user logout with confirmation and data removal."""
        file_obj = FileAccess(self.user_data_path)
        # Show confirmation dialog
        if messagebox.askyesno("Logout Confirmation", "Are you sure you want to logout?"):
            # Remove user data
            file_obj.WriteData()
            # Show a logout success message (optional)
            messagebox.showinfo("Logout", "You have been logged out successfully.")
            
            # Navigate back to the login page
            self.controller.show_frame("LoginPage")

def main():
    app = SignInXert()
    app.mainloop()
  
if __name__ == "__main__":
    main()