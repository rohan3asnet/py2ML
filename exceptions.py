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