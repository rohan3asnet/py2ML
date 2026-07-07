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
