from FileAccess import FileAccess

File = FileAccess('userData.json')

def AddingNewUser():
    choice = input("Enter your Input : ")
    if choice.lower() != "exit":
        uid = input("Enter UID : ")
        password = input("Enter password : ")
        name = input("Enter Full Name : ")
        age = input("Enter Age : ")

        newEntry = {
            "uid": uid,
            "password": password,
            "name": name,
            "age": age,
        }

        File.addData(newEntry)
        AddingNewUser()
    elif choice.lower() == "2":
        File.CreateFile()

AddingNewUser()
