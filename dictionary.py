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

#nesting 
# a list of dictionaries
# jaba multiple person ko information euta dictionary ley store garna sakdaena
# taba list of dictionaries banaauna sakinxa 
p1={'race':'Mongolian', 'complexity':'Light brown'}
p2={'race':'African', 'complexity':'Black'}
p3={'race':'American', 'complexity':'White'}
p4={'race':'Indian', 'complexity':'Brown'}

persons=[p1,p3,p3,p4]

for person in persons:
    print(person)

#list in a dictionary
person={
    'race': 'Chinese',
    'skills': ['Intelligent', 'High IQ','Problem solver' ] 
}
print(f"the person you are talking about is {person['race']} "
      "and he has following skills:\n")
for skill in person['skills']:
    print(f"{skill}\n")

#dictionary in dictionary
users={
    'person1':{
        'fname' : 'Lionel',
        'lname' : 'Ronaldo',
        'country' : 'Argentougal'
    },
     'person2':{
        'fname' : 'Cristiano',
        'lname' : 'Messi',
        'country' : 'Portina'
    },
}

for username, user_info in users.items():
    print(f"\n Username: {username}")
    full_name = f"{user_info['fname']} {user_info['lname']}"
    country = user_info['country']

    print(f"\t Full name: {full_name.title()}")
    print(f"\t Country: {country.title()}")
