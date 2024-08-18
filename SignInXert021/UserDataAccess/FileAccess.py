import json

class FileAccess:
    def __init__(self, fileAddress):
        self.file_address = fileAddress

    def addData(self, receive_data:dict=None):
        file_path = self.file_address
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                data.append(receive_data)
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=2)
        except FileNotFoundError:
            with open(file_path, 'w') as file:
                json.dump([receive_data], file, indent=2)
                print("File not found\nAnd Created a new file")


    def readData(self):
        file_path = self.file_address
        try:
            with open(file_path, 'r') as file:
                read_data = json.load(file)
                return read_data
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Error reading {file_path}. Returning empty list.")
            return [-1]
    def CreateFile(self):
        try:
            with open(self.file_address, 'x') as file:
                file.write("[]")
                print("Writed")
        except json.JSONDecodeError:
            with open(self.file_address, 'w') as file:
                file.write("[]")
            print(f"Error reading {self.file_address}. Creating a new file")
            