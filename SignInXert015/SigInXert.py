import random as r
import string
from UserDataAccess import FileAccess

class UserDataBank:
    def __init__(self):
        print("UserDataBank")
        self.File = FileAccess.FileAccess('UserDataAccess\\userData.json')
        try:
            self.userData = self.File.readData()
        except:
            self.File.CreateFile()
            print("\n\tFile Not Found\n\tNew File has been created\n")
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
        
class Interface(UserDataBank):
    def __init__(self):
        super().__init__()

    def is_special_character(self, char):
        return char in string.punctuation

    def boolean_choice(self, input_data):
        if input_data.lower() in ['yes', 'y', '0', 'yep', 'haa']:
            return True
        elif input_data.lower() in ['no', 'n', '1', 'nope', 'nahi']:
            return False

    def back_to_main(self):
        input_data = input("Enter (Yes or No): ")
        if input_data.lower() in ['yes', 'y', '1']:
            self.UserMainChoice()
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

    def UserMainChoice(self):
        print("1. -> Login using user id and pass")
        print("2. -> Create your user id and pass")
        choice = input("Enter your choice: ")
        print("_________________________________________________________\n\n")
        if choice not in ['exit','e']:
            if choice == "1":
                self.login()
            elif choice == "2":
                self.create_user()
            elif choice.lower() in ["version", "v", "update"]:
                self.version()
            else:
                print("\t\t--**Invalid Input :(**--\n")
                print("\t--- Try again ---")
                self.UserMainChoice()
        print("System Exited \n")
    def create_password(self):
        for attempt in range(4):
            if attempt > 0:
                print(f"Attempt {attempt}/3")
            pass_input = input("Create your password: ")

            len_count,num_count = 0,0
            sp_count,low_count,upp_count = 0,0,0

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
                self.UserMainChoice()
                print("_________________________________________________________")
            else:
                print("Enter the password again")

    def create_user(self):
        print("_________________________________________________________\n")
        name_input = input("\tEnter your full name: ")
        # user_age_input = input("Enter your user age: ")
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

            self.add_user(user_uid, user_pass, name_input, )
            print("_________________________________________________________")
            print("Shifted to Main Interface")
            self.UserMainChoice()
            print("_________________________________________________________")

    def login(self):
        self.readingData()
        user_name_stored, user_pass_stored = self.getData()

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
            user_pass_input = input("Enter your password: ")

            if user_pass_input == user_pass_stored[index_no]:
                print("\n__________________________________________________________\n")
                print("\t\t----Login successful-----")

            else:
               print("\n___________________________________________________________\n")
               print("\t\t****Wrong Pasword****")
               
               print("Shifted to Main Interface")
               self.UserMainChoice()
               print("_________________________________________________________")
        else:
            print("\n___________________________________________________________\n")
            print("\t\t****User not present****")
            print("Want to create a new user id ?")
            if self.boolean_choice(input("Enter (Yes or No): ")):
                self.create_user()
            else:
                print("_________________________________________________________")
                print("Shifted to Main Interface")
                self.UserMainChoice()
            print("___________________________________________________________\n")
# * UserCan Manuplate his Info. Like Age Gender, Bio , email, and all credential
    def ProfileData(self, recive_index):
        current_userName,current_userUid,current_userAge="","",""

    def version(self):
        update_message = """
_______________________________________

**SignInXpert v0.1.5 Update: Integration of JSON Managements**
    (+) We are thrilled to introduce new features and improvements.
    (-) We removed the ConnectX in this version Due to Some Reason*.   
    (+) This update also includes essential bug fixes and optimizations.
    (+) Your user data is now stored in a JSON file for improved security and data management.
    
            Build and Design by [Twitter & GitHub: @karnikhil90 ]
_______________________________________
"""


        print(update_message)
        print("Back to menu : \n")
        self.UserMainChoice()
        print("_______________________________________")

def starter():
    intro_message = """
_______________________________________

**SignInXpert v0.1.5 Update:**
    - Introducing JSON DATA storing.
    - Simplifies the login process and user ID creation.
    - Allows users to effortlessly create a user ID.

           Created by Nikhil Karmakar
_______________________________________
"""
           
    print(intro_message)

# Instantiate the Interface class
interface = Interface()
# Call the main_menu method
starter()
interface.UserMainChoice()