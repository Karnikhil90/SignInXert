from tkinter import *
import tkinter as tk 

class DefaultBTN:
       Home_button = Button(self.window, 
                                text="Home",
                                fg="white", 
                                command=self.Home_Click,
                                padx=10,
                                pady=2,
                                compound="top",
                                font=("Arial", 11, "bold"),
                                bg="#5dbea3",
                                activebackground="#33b249",
                                activeforeground="red",
                                highlightthickness=0)
        Exit_button = Button(self.window, 
                                text="Exit",
                                command=self.Exit_Click,
                                fg="white", 
                                padx=10,
                                pady=2,
                                compound="top",
                                font=("Arial", 11, "bold"),
                                bg="#5dbea3",
                                activebackground="#33b249",
                                activeforeground="red",
                                highlightthickness=0)     
        Setting_button = Button(self.window, 
                                text="Settings",
                                fg="white", 
                                command=self.Setting_Click, 
                                padx=10,
                                pady=2,
                                compound="top",
                                font=("Arial", 11, "bold"),
                                bg="#5dbea3",
                                activebackground="#33b249",
                                activeforeground="red",
                                highlightthickness=0)

        # user_welc.place(x = 1,y= 5)
        Home_button.place(x = 1,y=15*3)
        Setting_button.place(x= 25*6+4,y = 15*3)
        Exit_button.place(x = 35*7+2,y = 15*3)

class SignInXert:
    
    def __init__(self):
    # Basic interface
        TITLE = "SignInXert v0.2.1 DEV"
        ICONPATH = r".\\SignInXert021\\src\\icon\\icon.ico"
        self.window = Tk()
        self.window.title(TITLE)
        self.window.iconbitmap(ICONPATH) # set the
        self.window.configure(bg='#CACFD8')
        self.window.geometry('360x620')
        self.window.resizable(False, False)  # Disable resizing
        
        for Page in (HomePage,):
            page_name = Page.__name__
            page = Page(parent=self.container, controller=self)
            self.pages[page_name] = page
            page.grid(row=0, column=0, sticky="nsew")
        
        
    def Exit_Click(self):
        self.window.destroy()
        print("System exiting")
    def Home_Click(self):
        print("Home Click")

    def Setting_Click(self):
        print("Setting Click")
        

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Home Page")
        label.pack(side="top", fill="x", pady=10)

        input_label = tk.Label(self, text="Enter something:")
        input_label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        submit_button = tk.Button(self, text="Submit", command=self.print_input)
        submit_button.pack()  
def main():
    SignInXert().window.mainloop()
    
main()