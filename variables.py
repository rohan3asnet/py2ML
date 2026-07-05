message='hello world!'
print(message)
# variables are labels that you an assign to values
#variable references a certain value
message='changing the varaible value'
print(message)
#string operation
#string is series of characters
#anythin inside Quotes ' ' or " "
first_name='John'
last_name='Doe'
# to insert variable value into string, place f before " "
# put {} around the variables you want to use inside the string
# these strings are called f-strings
full_name=f" {first_name}{last_name}"
# upper(), lower(), title() are called methods
# method is followed by a set of parentheses because
# methods often need additional information to do their work
#but the mentioned methods donot need any information so they are empty
print(full_name.upper())
print(full_name.lower())
print(full_name.title())
print(f"Hello!, {full_name}.")
