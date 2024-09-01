import sys
import os

# Locate the `src` directory and add it to `sys.path`
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'src/'))
sys.path.append(src_path)

# Now import your module
import UserDataBank as data
import pytest

# Example test
obj = data.UserDataBank(r'src\database\data.json')
assert obj.logging('karnikhil90', 'nikhil') == True
assert obj.logging('invalid_user', 'wrong_password') == False
