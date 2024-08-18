import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("GUI with Pages")

        # Create a container to hold all pages
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Initialize dictionary to hold pages
        self.pages = {}

        # Create all pages
        for Page in (HomePage, LoginSuccessPage, SettingsPage):
            page_name = Page.__name__
            page = Page(parent=self.container, controller=self)
            self.pages[page_name] = page
            page.grid(row=0, column=0, sticky="nsew")

        # Show Home page initially
        self.show_page("HomePage")

    def show_page(self, page_name):
        # Show a page from the pages dictionary
        page = self.pages[page_name]
        page.tkraise()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Home Page")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Login Success Page",
                            command=lambda: controller.show_page("LoginSuccessPage"))
        button1.pack()

        button2 = tk.Button(self, text="Go to Settings Page",
                            command=lambda: controller.show_page("SettingsPage"))
        button2.pack()

        input_label = tk.Label(self, text="Enter something:")
        input_label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        submit_button = tk.Button(self, text="Submit", command=self.print_input)
        submit_button.pack()

    def print_input(self):
        user_input = self.entry.get()
        print("User Input:", user_input)


class LoginSuccessPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Login Success Page")
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Go to Home Page",
                           command=lambda: controller.show_page("HomePage"))
        button.pack()


class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Settings Page")
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Go to Home Page",
                           command=lambda: controller.show_page("HomePage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
