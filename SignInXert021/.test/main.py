import tkinter as tk

class SignInXert():
   def __init__(self):
        # Basic interface
        TITLE = "SignInXert v0.2.1 DEV"
        ICONPATH = r".\\src\\icon\\icon.ico"
        self.window = tk.Tk()
        self.window.title(TITLE)
        # self.window.iconbitmap(ICONPATH) # set the icon
        self.window.configure(bg='#CACFD8')
        self.window.geometry('360x620')
        self.window.resizable(False, False)  # Disable resizing
        AppController(self.window)
        
class AppController:
    def __init__(self, parent):
        self.parent = parent
        self.container = tk.Frame(parent)
        self.container.pack(side="top", fill="both", expand=True)
        self.pages = {}

        # Create pages
        for Page in (HomePage, SettingPage,LoginPage,CreatePage):
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
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        welcome = tk.Label(self, text="Welcome To SignInXert v0.2.1",
                           bg="#CACFD8", font=("Arial", 15, "bold"))
        welcome.pack(side="top", pady=10)

        my_icon_path = r".\\src\\icon\\setting.png"
        try:
            self.my_icon = tk.PhotoImage(file=my_icon_path)
        except tk.TclError as e:
            print(f"Error loading image: {e}")
            self.my_icon = None

        button = tk.Button(self,
                           image=self.my_icon,
                           compound=tk.LEFT,
                           command=lambda: controller.show_page("SettingPage"))
        button.config(width=32, height=32)
        button.pack(side="left", padx=5, pady=5)
      
class SettingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        my_icon_path = r".\\SignInXert021\\src\\icon\\arrow3.png"
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

class CreatePage(tk.Frame):pass
class LoginPage(tk.Frame):pass

if __name__ == "__main__":
    SignInXert().window.mainloop()
