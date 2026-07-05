# list is collection of items in a  particular order
# make the name of list plural
# square bracket [] represent list
prime_numbers=[2,3,5,7,11]
# to access elements, write the list name followed by index of item
print(prime_numbers[0])
# if the list is long and you want to access the last element 
print(prime_numbers[-1])
message=f"Ronaldo shirt number is {prime_numbers[3]}."
print(message)
#modifying elements in a list
languages=['C','C++','C#']
print(languages)
languages[0]='Java'
print(languages)
# adding elements to a list
languages.append('python')
print(languages)
#inserting elements to a list
languages.insert(0,'Rust')
print(languages)
#removing elements from a list
del languages[0]
print(languages)
# removing an item using pop() method
# sometime you might want to use value after you remove it
# pop remove the last item and let you use it again
popped_value=languages.pop()
print(popped_value)
# removing an element by value
languages.remove('C#')
print(languages)
# sorting list permanently with sort() method
cars=['bmw','bugati','lamborgini','audi','ferrari']
cars.sort()
print(cars)
# # sorting list temporarily with sorted() function
print(sorted(cars))
print(cars)
# reversing the list
cars.reverse()
print(cars)
# finding the length
print(len(cars))