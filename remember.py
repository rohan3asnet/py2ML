from pathlib import Path 
import json

# username=input('what is your name: ')

path=Path('username.json')
# contents=json.dumps(username)
# path.write_text(contents)

# print(f"we will remember you next time {username}")

contents=path.read_text()
username=json.loads(contents)

print(f"welcome back, {username}")