import random as r
import string
from getpass4 import getpass
import ConnectX


class UserDataBank:
    def __init__(self):
        self.user_uid_stored = ["amit", "nikhil", "manoj", "pratik", "rishab","himanshu"]
        self.user_Fullname_stored = ["amit kumar yadav", "nikhil karmakar", "manoj ram", "pratik brro", "rishab rai","himanshu jha"]
        self.user_pass_stored = ["1234", "4321", "1122", "0000", "1111","2222"]
        self.user_gender_stored =['M','M','M','M','M','M']
        self.user_age_stored = ['18','19','20','21','22','23']

    def add_user(self, add_user_name, add_user_pass,add_userFullName):
        self.user_uid_stored += add_user_name
        self.user_pass_stored += add_user_pass
        self.user_Fullname_stored += add_userFullName

class Interface(UserDataBank):
    def __init__(self):
        super().__init__()

    def is_special_character(self, char):  # Added self parameter
        return char in string.punctuation

    def boolean_choice(self,input_data):
        if input_data.lower() in ['yes','y','0','yep','haa']:
            return True
        elif input_data.lower() in ['no','n','1','nope','nahi']:
            return False

    def back_to_main(self):
        input_data = input("Enter (Yes or No): ")
        if input_data.lower() in ['yes', 'y','1']:
            self.main_menu()
        elif input_data.lower() in ['no', 'n', '0']:
            print("_________________________________________________________")
            print()
            print("\t\t***Error 001***")
            print("\t**Function is still developing**")
        else:
            print("_________________________________________________________")
            print("Invalid Input :(")
            print("------- Try again -------")
            self.back_to_main()

    def main_menu(self):
        print("1. -> Login using user id and pass")
        print("2. -> Create your user id and pass")
        choice = input("Enter your choice: ")
        print("_________________________________________________________\n\n")

        if choice == "1":
            self.login()
        elif choice == "2":
            self.create_user()
        elif choice.lower() in ["version", "v", "update"]:
            self.version()
        else:
            print("\t\t--**Invalid Input :(**--\n")
            print("\t--- Try again ---")
            self.main_menu()

    def create_password(self):
        for attempt in range(4):
            if attempt > 0:
                print(f"Attempt {attempt}/3")
            pass_input = input("Create your password: ")

            len_count = 0
            num_count = 0
            sp_count = 0
            low_count = 0
            upp_count = 0

            if len(pass_input) >= 8:
                len_count += 1

            for char in pass_input:
                if char.isdigit():
                    num_count += 1
                elif char.islower():
                    low_count += 1
                elif char.isupper():
                    upp_count += 1
                elif self.is_special_character(char):
                    sp_count += 1

            if len_count == 0:
                print("** Your password should be at least 8 characters long")
            if num_count == 0:
                print("** You need at least one number")
            if sp_count == 0:
                print("** You need at least one special character")
            if low_count == 0:
                print("** You need at least one lowercase letter")
            if upp_count == 0:
                print("** You need at least one uppercase letter")

            if len_count >= 1 and num_count >= 1 and sp_count >= 1 and low_count >= 1 and upp_count >= 1:
                return pass_input

            elif attempt == 3:
                print("_________________________________________________________")
                print("\tExceeded the maximum number of attempts.")
                print("\tPlease try again later")

                print("\n_________________________________________________________")
                print("Shifted to Main Interface")
                self.main_menu()
                print("_________________________________________________________")
            else:
                print("Enter the password again")

    def create_user(self):
        print("_________________________________________________________\n")
        name_input = input("\tEnter your full name: ")
        first_name = name_input.split(maxsplit=1)[0]
        user_uid = first_name.lower() + str(r.randint(10, 99))

        print("Three Conditions for creating a password:")
        print("1. At least one capital and one lowercase character")
        print("2. At least one number and one special character")
        print("3. Password length must be 8 or more characters")

        user_pass = self.create_password()

        if user_pass:
            print("\n\n_________________________________________________________\n")
            print("Remember Your Details: ")
            print(f"\tUser id: '{user_uid}'")
            print(f"\tUser password: '{user_pass}'")

            self.add_user([user_uid], [user_pass],[name_input])
            print("_________________________________________________________")
            print("Shifted to Main Interface")
            self.main_menu()
            print("_________________________________________________________")

    def login(self):
        user_name_stored, user_pass_stored = self.user_uid_stored, self.user_pass_stored

        user_name_input = input("Enter your user name: ")
        index_no = 0
        temp_found = -1

        for i in range(len(user_name_stored)):
            if user_name_input == user_name_stored[i]:
                index_no = i
                temp_found += 1

        if temp_found != -1:
            print("_________________________________________________________\n\n")
            print("\t\t-----User Present----- ")
            user_pass_input = getpass("Enter your password: ")
            if user_pass_input == user_pass_stored[index_no]:
                print("\n__________________________________________________________\n")
                print("\t\t----Login successful-----")
                print("ConnectX has been Open, Cheak it out.....")
                # ConnectX Opens here
                self.open_window(index_no)
            else:
               print("\n___________________________________________________________\n")
               print("\t\t****Wrong Pasword****")
               
               print("Shifted to Main Interface")
               self.main_menu()
               print("_________________________________________________________")
        else:
            print("\n___________________________________________________________\n")
            print("\t\t****User not present****")
            print("Want to create a new user id ?")
            switch = input("Enter (Yes or No): ")
            if self.boolean_choice(switch):
                self.create_user()
            else:
                print("_________________________________________________________")
                print("Shifted to Main Interface")
                self.main_menu()
            print("___________________________________________________________\n")
   
    def open_window(self, recive_index):

        user_Fullname = self.user_Fullname_stored[recive_index]
        words = user_Fullname.split()
        # Capitalize the first letter of each word and join them back into a string
        capitalized_words = [word.capitalize() for word in words]
        result_string = " ".join(capitalized_words)

    # User Profile Information
        user_Fullname = result_string
        user_uid= self.user_uid_stored[recive_index]
        user_password = self.user_pass_stored[recive_index]

        # To prevent Errors 
        try:
            user_age = self.user_age_stored[recive_index]
        except:
            user_age = -1

                # Parameters : Full name, users_name,users_age,users_password,
        ConnectX.ConnectX_caller(user_Fullname,user_uid,user_age,user_password)
        
    def ProfileData(self, recive_index):
        print("Under construction")
      
        

    def version(self):
        update_message = """
_______________________________________

**SignInXpert v0.1.4 Update:**
    - We are thrilled to introduce ConnectX, our new Social Media app.
        -> Enjoy the convenience of direct login to ConnectX from our user-friendly GUI.
    - This update also includes essential bug fixes and optimizations.
_______________________________________


"""
        print(update_message)
        print("Back to menu : \n")
        self.main_menu()
        print("_______________________________________")

def starter():
    intro_message= """
__________________________________________________________

    *** SignInXpert v0.1.4 : Introducing ConnectX ***

        - Simplifies the login process and user ID creation.
        - Allows users to effortlessly create a user ID.
        - Now you can log in directly to ConnectX, our new Social Media app.

           Created by Nikhil Karmakar
_________________________________________________________
           
"""

    print(intro_message)

# Instantiate the Interface class
interface = Interface()
# Call the main_menu method
starter()
interface.main_menu()
