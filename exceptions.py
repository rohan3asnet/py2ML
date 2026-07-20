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

    