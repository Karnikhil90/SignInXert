
author Nikhil Karmakar<br>
since alpha 0.0.1 <br>
version 2.0.12 <br>
license [MIT](../LICENSE)<br>
##### Dev version : Recreating from old version(dev0.2.1)
    
#
#               SignInXert: Its a basic authentication & login system 

when it will start it will ask use for login with user UID & Password.
And a create a new user account by asking the full name , email , age and password.
After putting all the values properly Its will show as verification that all of your datas are correct or not.
This is Going to use OOPs. for Multiple Pages/Framers like Login, creations , profile and a example socila or e-commerce type application.


## File Structure:
```bash
./ {Root}
    ├──LISENCE
    ├──README.md
    ├──.gitignore
    ├──.pylintrc
    ├──requirement.txt
    ├──.github/workflow/*
    ├──info/ {some stuff for UPDATEs and history of creation}

    
    ├──main.py {work as a driver code. Calles The SignInXert} 
    ├── util/ {INFORMATION for README.md}
    ├── src
    │    ├── SignInXert.py (The main application which is going to run)
    │    ├── UserDataBank.py
    │    ├── __init__.py {!NOT DEFINED.}
    │    
    │    ├── lib/
    │       ├── __init__.py
    │       ├── JsonEditor.py
    │       ├── FileAccess.py
    │
    │    ├── icon/*{all the icons are stored here}
    │    ├── cache/* {To store the data of the user who is logged in}
    │    ├── logs/
    │    ├── info/
    │    ├── example/* {Test projects . NOT THE PART OF APPLICATION}
    │    ├── database/* 
    │    ├── config/*{This will contain a json file with some variables from which u can modify APP.(like background color geometry)}
    │    ├──.........{more dir.. will be there as its grow.}

```

! There will classes UserDataBank, SignInXert and rest are part of the SignInXert.
    *The UserDataBank: use The lib.FileAccess to read and write the data to store the use data continuously.
        *And also to Use as to get the data from the json file.
    *SignInXert: This is the main application will be most likely to as a route and controll all the pages.

### start:
    when it boot it checks file for which user was logged in.
    Then it calls the HomePage if there is a user logged in.
    Else it calls the LoginPage if there is no user logged in.

### conditions:
    ? For Create Account
        If user dont have a account then You can create Just clicking the button.
    

### FEW DESIGINE STUFF's

* This will be a GUI application using Tkinter in Python.
* Note: This is just a basic version and might need to be expanded upon.
* All will be slowly add in future versions. This version only going to have a very small chuck of it.
* This is re-creating from the original dev version as a cheak and a self learning of GUI in python.

#

### @UPDATE
    UPDATE [28-08-2024 - 15:40]: First update write the documentation as big comment and create the base application. 
    UPDATE [29-08-2024 - 10:30]: Adjusting the file paths & structures.Added lil documentation in the big comments.
        -> Implemented json config Directly from the file using FileAccess module.Set a default value to all the important files
    UPDATE[30-08-2024 -  15:15 -> 18:00 ]: Change the structure of config_app.json and also update that in the main srcipt.
        -> Update the HomePage UI and with a working logout support.
        ->Implemented cache directory and the current logged user also.
    UPDATE [31-08-2024 - 15:00 -> 16:45]: UPDATE Setting & save changes of settings like background_color and geometry. By directly chnaging the config/config_app.json file.
        -> update the structure little bit. 
        -> Testing run from a main.py file (root/main.py) Of the main application file SignInXert.By adding ./Test ,/example and __init__.py file .
        -> Added a new library file called JsonEditor at src\lib. For changing Json file of config_app.json as I menstion earlier.
    UPDATE [07-09-2024 -14:00-14:40] : Final update of stucture & add some 
    __init__.py file. Make fixx all the issues* in the runing of application through main.py file or run as a module.
         
#   
#### problem ['*' = fixed]
    [PROBLEM REPORT TIME] : PROBLEM 
    *[30-08-24] The logout need to be better. But the HomePage's logout and re-read the name of the user need to fix
#