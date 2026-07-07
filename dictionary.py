#dictionary is a collection of key-value pairs
# each key is connected to a value
# you can use a key to access the value associated with that key
# key's value can be number, string, list or another dictionary
# dictionary is wrapped in braces {}
book_1={'name':'War and Peace', 'author':'Leo Tolstoy', 'publication':'Penguin Books', 'page number': 1300}
#accesing values in dicitonary
print(book_1['name'])
print(book_1)
#adding new key-value pairs
book_1['book purchased'] = 2081
book_1['book price'] = 720
print(book_1)

if book_1['page number'] == 300:
    status = "you are close in finishing volume 1"
elif book_1['page number'] == 700:
    status = 'you have finished volume 2'
elif book_1['page number'] == 1300:
    status = 'you just finished the MasterPiece'

print(status)

#deleting key-value pairs
del book_1['book purchased']
print(book_1)

#using get() to access values
# it is used to set a default value that will be returned
# if the requested key doesn't exist
ball={'size': 'small','color':'white'}
brand_name=ball.get('brand', 'there is no brand name.')
print(brand_name)

#looping through all key value pairs
user_0 = {
    'username' : 'CR7',
    'first_name' : 'Cristiano',
    'second_name' : 'Ronaldo',
}

for key, value in user_0.items():
    print(f"\n Key: {key}")
    print(f"Value: {value}")
#looping through all the keys in a dictionary
for key in user_0.keys():
    print(f"\n Key: {key}")
#these two are same
for key in user_0:
    print(f"\n Key: {key}")
#looping through all values
for value in user_0.values():
    print(f"\n Value: {value}") 