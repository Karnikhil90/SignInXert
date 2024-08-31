
"""
@author Nikhil Karmakar
@since 0.0.1
@version v0.0.5
@license MIT


UserDataBank:
    This class is designed to manage user data stored in JSON format. It interacts directly with the filesystem to 
    read, write, and manage user data securely and efficiently. The UserDataBank class provides methods to access, 
    add, and search for user data, making it a crucial component for handling user authentication and data storage in 
    the application.
    
    ? Little extra information: 
        *It have been using since the first release of logining stuffs.
        *It will read the data from the json file and store it as list of dictionaries.
        *Now also read the /config directory to configure the app settings.
        *This make the app more profestional to handle the datas apth.
        *It uses the lib(my self made module) to read the json files data.
    Key Features:
    1. Direct access to user data stored in JSON files.
    2. Automatically handles the creation of new data files if they do not exist.
    3. Reads user data from a specified JSON file and stores it in memory as a list of dictionaries.
    4. Provides methods to retrieve specific types of user data (e.g., UID, password, full name, age, email).
    5. Supports adding new user data and automatically updates the stored data list.
    6. Includes a search function to retrieve a user’s full data record by their UID.
    7. Utilizes the FileAccess class (a custom module) to manage file operations, ensuring robust error handling and 
       directory/file management.

# Explanation:
    The UserDataBank class is initialized with a file path to the JSON data file. Upon initialization, it attempts 
    to read the data from the specified file. If the file does not exist or is unreadable, it creates a new file 
    and initializes it with an empty list. The data is then parsed and stored in separate lists corresponding to 
    user UIDs, passwords, full names, ages, and email addresses.

    The class provides a method, `getData()`, that allows the caller to retrieve specific types of data (such as 
    UIDs or passwords) based on the DataType parameter. If no DataType is specified, it returns all stored data.

    Another method, `add_user()`, allows new user data to be added to the JSON file. This method also refreshes 
    the in-memory data lists to include the newly added user.

    The `search_user_data()` method is designed to search for a specific user by their UID and return the 
    complete data dictionary for that user. If no matching user is found, it returns None.

# All Functions Explanation:

1. __init__(self, filepath="database/data.json"):
   - Initializes the UserDataBank class with a specified file path to the JSON data file.
   - Uses the FileAccess class to read data from the file and store it in memory.
   - Creates a new file if the specified file does not exist.

2. readingData(self):
   - Parses the user data stored in memory and separates it into lists for UIDs, passwords, full names, ages, 
     and email addresses.
   - Handles potential errors during the parsing process.

3. getData(self, DataType=None) -> list:
   - Returns a specific type of user data based on the DataType parameter (e.g., "uid", "pass", "fullname", 
     "age", "email").
   - If no DataType is specified, returns all stored data.

4. add_user(self, add_user_name: str, add_user_pass: str, add_userFullName: str, add_user_age: str = None, 
             add_user_email_ID: str = None) -> None:
   - Adds a new user entry to the JSON data file.
   - Refreshes the in-memory data lists to include the newly added user.

5. search_user_data(self, uid: str):
   - Searches for a user by their UID and returns the full JSON data for that user.
   - Returns None if no matching user is found.

# Example Usage:

# Initialize UserDataBank
user_data_bank = UserDataBank(filepath="database/data.json")

# Add a new user
user_data_bank.add_user(add_user_name="john_doe", add_user_pass="secure123", add_userFullName="John Doe", 
                        add_user_age="30", add_user_email_ID="john@example.com")

# Retrieve all UIDs
uids = user_data_bank.getData(DataType="uid")

# Search for a user by UID
user_data = user_data_bank.search_user_data(uid="john_doe")

# Check retrieved data
if user_data:
    print(f"User found: {user_data}")
else:
    print("User not found.")
"""
# imports 

import tkinter as tk
from tkinter import messagebox
from lib.FileAccess import FileAccess

class UserDataBank:
    def __init__(self, filepath:str ="database/data.json"):
        self.File = FileAccess(filepath)
        try:
            self.userData = self.File.readData()
            if self.userData == [-1]:
                self.File.CreateFile()
                print("NEW FILE HAS BEEN CREATED")
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
    
    def getData(self, DataType="all") -> list | dict :
        if DataType == "uid":
            return self.user_uid_stored
        elif DataType in ["pass","password"]:
            return self.user_pass_stored
        elif DataType in ["fullname", "name"]:
            return self.user_Fullname_stored
        elif DataType == "age":
            return self.user_age_stored
        elif DataType == "email":
            return self.user_email_stored
        elif DataType == "login":
            return self.user_uid_stored, self.user_pass_stored
        elif DataType == "all":
            return {
                "uid": self.user_uid_stored,
                "password": self.user_pass_stored,
                "name": self.user_Fullname_stored,
                "email": self.user_email_stored,
                "age": self.user_age_stored
            }
        else: 
            print("ErrorType[UserDataBank]: invalid getData() requested ")
            return None
             

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

    def logging(self, uid: str, password: str) -> bool:
        """Check if the provided UID and password match the stored data."""
        try:
            if uid in self.user_uid_stored:
                index = self.user_uid_stored.index(uid)
                if self.user_pass_stored[index] == password:
                    print("Login successful")
                    return True
                else:
                    print("Incorrect password")
                    return False
            else:
                print("UID not found")
                return False
        except Exception as e:
            print(f"Error during login attempt: {e}")
            return False