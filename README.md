

# SignInXert

## Overview

SignInXert is a basic authentication and login system developed to enhance my understanding of Python GUI development using Tkinter. This project represents a significant evolution from my earlier CLI-based versions, reflecting my journey in programming and my passion for creating functional and intuitive applications.

## Project Evolution

Initially, SignInXert was a CLI-based project with several versions aimed at mastering Python basics and logging functionalities. Over time, this project has transitioned into a more sophisticated GUI application, demonstrating advanced concepts and improved user experience. You can explore the earlier versions of this project at [SignInXert CLI Versions](https://github.com/Karnikhil90/MyFirst/tree/main/SignInXert015).

## Current Version

The current version of SignInXert is a fully functional GUI application using Tkinter. It incorporates several features for user authentication and data management, including:

- **Login System:** Allows users to log in using a UID and password.
- **User Creation:** Enables the creation of new user accounts with details like full name, email, age, and password.
- **Data Verification:** Provides verification to ensure user data accuracy.

## File Structure

The project is organized as follows:

```
./ {Root}
    ├── src
        ├── main.py             # The main application entry point
        ├── UserDataBank.py      # Manages user data storage and retrieval
        ├── lib/                 # Custom modules
        ├── icon/                # Icon files
        ├── cache/               # Stores data for logged-in users
        ├── logs/                # Application logs
        ├── info/                # Miscellaneous information
        ├── database/            # User data files
        ├── config/              # Configuration files (e.g., JSON for app settings)
        └── ...                  # Additional directories as the project grows
```

## UserDataBank Class

The `UserDataBank` class is a crucial component of the application designed to manage user data in JSON format. It provides methods for:

- **Initializing with a File Path:** Loads or creates a JSON file for user data.
- **Reading Data:** Parses and separates user data into different lists.
- **Adding Users:** Adds new user entries to the data file and updates in-memory lists.
- **Searching Users:** Retrieves complete user data by UID.

### Key Features

- Direct access to user data stored in JSON files.
- Automatic creation of new data files if they do not exist.
- Methods for retrieving and updating user data.
- Integration with a custom module (`FileAccess`) for robust file handling.

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd SignInXert/src
   ```

3. **Run the Application:**

   ```bash
   python main.py
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Future Plans

This version is a foundational release, with plans to expand features and enhance the application in future versions. Stay tuned for updates!

## Acknowledgments

- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Python JSON Module](https://docs.python.org/3/library/json.html)

## About Me

Self-taught coder | Still Learning | Fluent in Java & Python | C/C++, Rust, & Basic Web Development | Passionate about Embedded Systems

### Connect with Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/karnikhil90/)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/karnikhil90)
[![Social Media](https://img.shields.io/badge/Social%20Media-000000?style=for-the-badge&logo=google&logoColor=white)](https://linktr.ee/karnikhil90)
