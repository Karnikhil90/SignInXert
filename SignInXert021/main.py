# This will be the GUI of the older version
# SignInXert v0.2.1 -Update DEV only 

# It will be the same but have the GUI and the json file system 
# 04-05-2024 [12:02 ] Project is Started
# 05-05-2024 [13:35 ] UPDATE is just finshed the two page (Home,setting) and add icons on the button
# 09-05-2024 [14:42 ] UPDATE is just add the login feature . But working well but!!!!!

from UserDataAccess import FileAccess
import tkinter as tk


class UserDataBank:
    def __init__(self):
        self.File = FileAccess.FileAccess('.\\DataBase\\userDatainventroy.json')
        try:
            self.userData = self.File.readData()
            if(self.userData==[-1]):
                self.File.CreateFile()
                print("NEW FILE HAD BEED CREATED ")   
        except Exception as e:
             print(f"Error reading data: {e}")
        
    def readingData(self):
        self.user_uid_stored, self.user_age_stored, self.user_Fullname_stored, self.user_pass_stored = [], [], [], []
        try:
            for data in self.userData:
                self.user_uid_stored.append(data['uid'])
                self.user_pass_stored.append(data['password'])
                self.user_Fullname_stored.append(data['name'])
                self.user_age_stored.append(data.get('age', ''))
        except Exception as e:
            print(f"Error reading data: {e}")
  
    def getData(self):
        return self.user_uid_stored,self.user_pass_stored
        
    def add_user(self, add_user_name:str, add_user_pass:str, add_userFullName:str,add_user_age:str=None):

        newEntry = {
            "uid":add_user_name,
            "password":add_user_pass,
            "name":add_userFullName,
            "age":add_user_age
        }
        
        print("Added entry")
        self.File.addData(newEntry)
        self.userData = []
        self.userData = self.File.readData()
class SignInXert(UserDataBank):
    def __init__(self):
        super().__init__(self)
        # Basic interface
        TITLE = "SignInXert v0.2.1 DEV"
        ICONPATH = r".\\src\\icon\\icon.ico"
        self.window = tk.Tk()
        self.window.title(TITLE)
        self.window.iconbitmap(ICONPATH) # set the icon
        self.window.configure(bg='#CACFD8')
        self.window.geometry('360x620')
        self.window.resizable(False, False)  # Disable resizing
        AppController(self.window)
        # HomePage(self.window, controller=self, user_uid_stored=self.user_uid_stored)
        
class AppController():
    def __init__(self, parent):
        self.parent = parent
        self.container = tk.Frame(parent)
        self.container.pack(side="top", fill="both", expand=True)
        self.pages = {}
        # Create pages
        for Page in (HomePage, SettingPage,PostLoginPage):
            page_name = Page.__name__
            page = Page(parent=self.container, controller=self)
            self.pages[page_name] = page
            page.grid(row=0, column=0, sticky="nsew")

        # Show homepage by default
        self.show_page("HomePage")

    def show_page(self, page_name:str):
        print(page_name+" clicked")
        page = self.pages[page_name]
        page.tkraise()    
        
    def login(self, name, password) -> bool:
        print("Login FUNCTION")
        user_name_stored, user_pass_stored = [],[]
        try:
            user_name_stored, user_pass_stored = getData() 
        except Exception as e:
            print(f"Error as {e}")
        print("DATA\n",user_name_stored)
        temp_found = False

        for i in range(len(user_name_stored)):
            if name== user_name_stored[i]:
                index_no = i
                temp_found = True
        if (temp_found and password == user_pass_stored[index_no]):
            print(f"DEBUG :User found={temp_found} and pass=True") 
            return True
        print(f"DEBUG :User found={temp_found} and pass=False")         

        return False     
        
class HomePage(tk.Frame,AppController):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        # self.user_uid_stored = user_uid_stored
        welcome = tk.Label(self, text="Welcome To SignInXert v0.2.1 DEV",
                           bg="#CACFD8", font=("Arial", 15, "bold"))
        welcome.pack(side="top", pady=10)
        my_icon_path = r".\\src\\icon\\setting.png"
        try:
            self.my_icon = tk.PhotoImage(file=my_icon_path)
        except Exception as e:
            print(f"Error loading image: {e}")
            self.my_icon = None
        button = tk.Button(self,image=self.my_icon,compound=tk.LEFT,
                           command=lambda: controller.show_page("SettingPage"))
        button.config(width=32, height=32)
        button.pack(side="left", padx=5, pady=5)
        
        self.input_user_id = tk.Entry(self)
        self.input_user_id.pack()
        self.input_user_password = tk.Entry(self)
        self.input_user_password.pack(padx=5, pady=5)
        self.input_user_id.bind("<Return>", self.invoke_submit)
        submit_button = tk.Button(self, text="Submit", command=self.print_input)
        submit_button.pack()

    def print_input(self):
        user_input_name = self.input_user_id.get()
        user_input_p = self.input_user_password.get()
        print("User Input:", user_input_name,user_input_p)
        self.input_user_id.delete(0, tk.END)
        self.input_user_password.delete(0, tk.END)
        
        if self.controller.login(name=user_input_name, password=user_input_p):
            print("LOGIN Success")
        else:
            print("LOGIN Failure")
        self.controller.show_page("PostLoginPage")
    def invoke_submit(self, event): self.print_input()             
class SettingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        my_icon_path = r".\\src\\icon\\arrow3.png"
        self.controller = controller

        label = tk.Label(self, text="Settings Page",bg="#CACFD8", font=("Arial", 15, "bold"))
        label.pack(side="top", fill="x", pady=5)

        try:
            self.my_icon = tk.PhotoImage(file=my_icon_path)
        except tk.TclError as e:
            print(f"Error loading image: {e}")
            self.my_icon = None

        button = tk.Button(self, 
                           image=self.my_icon,
                           compound=tk.LEFT,
                           command=lambda: controller.show_page("HomePage")) 
        button.config(width=32, height=32)  # Adjust width and height as needed
        button.place(y=36)        
class PostLoginPage(tk.Frame):
     def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        button = tk.Button(self, 
                           text="CLICK ME!!!!",
                           compound=tk.LEFT,
                           command=lambda: controller.show_page("HomePage"))
        button.pack()
              
def main():
    SignInXert().window.mainloop()
main()