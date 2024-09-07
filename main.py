import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Now import SignInXert
import src.SignInXert as S

config:str="src/config/config_app.json"

S.main(config)