from pathlib import Path 
import json

def get_stored_name(path):
    if path.exists():
        contents=path.read_text()
        username=json.loads(contents)
        return username
    else:
        return None


def greet_user():
    """greet user by name"""
    path=Path('username.json')
    username=get_stored_name(path)
    if username:
        print(f'welcome back, {username}')
    else:
        username=input('what is your name: ')
        contents=json.dumps(username)
        path.write_text(contents)
        print(f"we will remember you next time {username}")

greet_user()

