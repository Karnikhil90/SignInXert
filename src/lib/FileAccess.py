import os
import json

class FileAccess:
    def __init__(self, fileAddress):
        self.file_address = fileAddress
        # print(fileAddress)
        try:
            self.ensure_directory_exists()
            self.ensure_file_exists()
        except Exception as e:
            print(f"Initialization error: {e}")

    def ensure_directory_exists(self):
        """Ensure that the directory for the file exists."""
        try:
            dir_name = os.path.dirname(self.file_address)
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
        except Exception as e:
            print(f"Error ensuring directory exists: {e}")

    def ensure_file_exists(self):
        """Ensure that the file exists; create it if not."""
        try:
            if not os.path.isfile(self.file_address):
                self.CreateFile()
        except Exception as e:
            print(f"Error ensuring file exists: {e}")

    def addData(self, receive_data: dict = None):
        print(receive_data)
        file_path = self.file_address
        try:
            # Attempt to read existing data
            try:
                with open(file_path, 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                # If file does not exist, initialize with an empty list
                data = []
            except json.JSONDecodeError:
                # Handle the case where the file is empty or corrupted
                data = []

            # Add new data and write it to the file
            if receive_data:
                data.append(receive_data)

            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error adding data to file: {e}")
    def write_json(self,recive_data): 
        """Write data to JSON file."""
        try:
            with open(self.file_address, 'w') as file:
                json.dump(recive_data, file, indent=4)
        except Exception as e:
            print(f"Error writing data to JSON file: {e}")

    def readData(self) -> list:
        file_path = self.file_address
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File not found: {file_path}. Returning empty list.")
            return []
        except json.JSONDecodeError:
            print(f"Error decoding JSON in file: {file_path}. Returning empty list.")
            return []
        except Exception as e:
            print(f"Error reading data from file: {e}")
            return []

    def CreateFile(self):
        try:
            with open(self.file_address, 'w') as file:
                file.write("[]")
                print("Created a new file with an empty list.")
        except FileExistsError:
            print(f"File already exists: {self.file_address}")
        except Exception as e:
            print(f"Error creating file: {e}")
    
    def WriteData(self,content:str = "[]"):
        """Clear the content of the JSON file by overwriting it with an empty array."""
        try:
            with open(self.file_address, 'w') as file:
                file.write(content)
                print(f"Cleared the content of the file: {self.file_address}")
        except Exception as e:
            print(f"Error clearing file content: {e}")
    def print_json(self,recived_data:any={}):
        try:
            print(json.dumps(recived_data, indent=4))
        except Exception as e:
            print(f"Error printing JSON: {e}")