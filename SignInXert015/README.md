# SignInXert v0.1.5

SignInXert is a login and user management system that stores user data in a 'userdata.json' file.

## Project Structure

### Files

#### 1. `FileAccess`

- This class is responsible for reading and editing the 'userdata.json' file.

#### 2. `SignInXert`

- This class contains two classes: `UserDataBank` and `Interface`.

##### `UserDataBank`

- This class calls the `FileAccess` class for information.
- It maintains a list to store user data.
- Provides functions:
  - `add_user`: Adds a new user with an auto-generated UID.
  - `get_data`: Retrieves user data.

##### `Interface`

- This class inherits from `UserDataBank` and handles user interactions and data.

## User Data Structure

The user data structure includes the following fields:

- `username`: User's username
- `uid`: Auto-generated user ID
- `password`: User's password
- `gender`: User's gender
- `age`: User's age

## Password Requirements

- Password must be at least 8 characters long.
- Password must contain at least one uppercase letter.
- Password must contain at least one lowercase letter.
- Password must contain at least one number.
- Password must contain at least one special character.

## Usage Example

```python
# Example code snippet for using SignInXert

# Import necessary classes
# Instantiate the Interface class
interface = Interface()

# Call the main_menu method
starter()

# Example 1: Creating a new user
interface.create_user()

# Example 2: Logging in with existing credentials
interface.login()

# Example 3: Getting user data
user_uid_list, user_pass_list = interface.getData()
print("User IDs:", user_uid_list)
print("User Passwords:", user_pass_list)

# Example 4: Displaying version information
interface.version()
```