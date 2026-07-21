# exceptions are handled with try-except block
# it asks python to do something
# but it also tells python what to do when exception is raised

try:
    print(5/0)

except ZeroDivisionError:
    print('you cannot divide by zero')

# if code in try blocks works, python skips except block
# but if code in try block caused an error
# it looks for the except block

try:
    print("Enter your birthdate:\n")

    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))

    if not (1 <= month <= 12):
        print("Invalid month.")
    elif not (1 <= day <= 31):
        print("Invalid day.")
    elif year > 2026:
        print("Invalid year.")
    else:
        print(f"Your birthday is {day}/{month}/{year}")

except ValueError:
    print("Please enter only integer values.")

#handling filenotfounderror exception

from pathlib import Path

def count_words(path):
    try:
        contents=path.read_text(encoding='utf-8') # this encoding is needed when the file is not 
        #created in the device, system's encoding doesnot match the encoding of the file that's being read
    except FileNotFoundError:
        print(f" Sorry, the file {path} doesnot exist.")

    else:
        words = contents.split()
        num_words = len(words)
        print(f"the file {path} has about {num_words} of words.") 

filenames=['alice.txt']# add more files as per your wish
for filename in filenames:
    path=Path(filename)
    count_words(path)   