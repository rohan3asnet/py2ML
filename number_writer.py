# we are using json
# the main objective of using json is to store the information
# entered by the useres when the program ends
# json module allows you to convert simple python data into 
# json formatted strings and then load the data from the file the next time
# the program runs

from pathlib import Path
import json

numbers=[2,3,5,7,11,13,17,19]
path=Path('numbers.json')
contents=json.dumps(numbers)
path.write_text(contents)