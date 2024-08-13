# Import the tkinter library
from tkinter import *
from tkinter import messagebox

class ConnectX:
    def Exit_Click(self):
        self.window.destroy()
        print("System exiting")
    def Home_Click(self):
        print("Home Click")
        self.change_Frame_color("#0079FF")
        self.profile_Data(False)

    def Profile_Click(self):
        print("Profile Click")
        self.change_Frame_color("#F8C471")
        self.profile_Data(True)

    def Setting_Click(self):
        print("Setting Click")
        self.profile_Data(False)
        self.change_Frame_color("#DC7633")
    def show_password(self):
        print("Show Password Clicked")
        messagebox.showinfo("Display Password","Password: "+self.user_password)

    def profile_Data(self, show):
        if show:
            self.hide_all_labels()
            profile = f"Name : {self.name}\n\n"
            profile += f"User Name : {self.user_name}\n\n"
            profile += f"Age : {self.user_age}"
            self.profile_label = Label(self.frame,
                                       text=profile,
                                       font=('Trebuchet MS', 22, 'bold'),
                                       fg='black')
            self.profile_label.place(anchor='nw', x=15, y=80)

            self.profile_button = Button(self.frame,
                                    text="show Password",
                                    fg="white",
                                    command=self.show_password, 
                                    padx=10,
                                    pady=2,
                                    font=("Arial", 11, "bold"),
                                    bg="#5dbea3",
                                    activebackground="#33b249",
                                    activeforeground="red",
                                    highlightthickness=0,
                                )
            self.profile_button.place(anchor='nw', x=15, y=300)
        else:
            self.hide_all_labels()

    def hide_all_labels(self):
        if hasattr(self, 'profile_label'):
            self.profile_label.destroy()
            self.profile_button.destroy()

    def Display_notice(self):
        txt = "Its is under Development"
        lable = Label(self.window,
                               text=txt,
                               font=('Trebuchet MS', 14, 'bold'),
                               fg='#E74C3C',
                               bg='#F7DC6F',
                               compound='left'
                               )
        lable.place(x=110,y=150)

        # Schedule the label to be destroyed after a certain time (e.g., 2000 milliseconds = 2 seconds)
        self.window.after(1000*4, lable.destroy)

        #DAF7A6
    def __init__(self, 
                 name : str,
                 user_name:str,
                 user_age:int,
                 user_password:str,
                 ):
        # Current User Information
        self.name = name
        self.user_name = user_name
        self.user_password = user_password
        if user_age == -1: 
            self.user_age = str('NOT DEFINED')
        else: self.user_age = user_age

        TITLE = "ConnectX"
        # Create the main window
        self.window = Tk()
        # Visual Setup
        self.window.title(TITLE)
        self.window.configure(bg='#0079FF')
        self.window.geometry('380x500')
        self.window.resizable(False, False)  # Disable resizing
        
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
        Profile_button = Button(self.window, 
                                text="profile",
                                fg="white",
                                command=self.Profile_Click, 
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
        Profile_button.place(x = 25*3,y=15*3)
        Exit_button.place(x = 35*7+2,y = 15*3)
        self.Display_notice()

# Default Frames 
        self.frame = Frame(self.window, bg='#0079FF')
        self.frame.place(x=0, y=100, width=380, height=400)

# Change the Background color for feel that The Frame is changed
    def change_Frame_color(self,color):
        self.frame.configure(bg=color)

# Driver Code

def ConnectX_caller(name,username,age:int,userpassowrd):
    ConnectX(name,username,age,userpassowrd).window.mainloop()




