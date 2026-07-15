# class define general behaviour 
# that represents real world things and situation
# when we create individual objects,
# objects is automatically equipped with general behaviour
# making an object from class is called instantiation
# and you work with instance of class

class Book:
    """simple attempt to model a book"""
    def __init__(self, name, author):
        # a function that is part of a class is a method
        # __init__() method is a special method 
        # that python runs automatically
        # leading underscore and trailing underscore is a convention
        # that helps prevent python's default method names from conflicting
        # with your method names
        # self parameter is mandatory for this method
        # it must come first before other parameters
        """initializing name and author"""
        # all variables prefixed with self is available to every method in the class
        self.name = name 
        self.author = author

    def tag(self):
        print(f"{self.name} is a classic.")

    def publication(self):
        print(f"{self.name} is published by Penguin.")

#think class as a set of instruction for how to make an instance
#making an instance from a class
# here we are telling python to create a Book whose name is blahblah and author is blahblah
my_book=Book('The Brothers Karamazov', 'Fyodor Dostoevsky')
# when python read the above line
# it calls the __init__() method
# __init__() methods creates an instance and sets name and author
# python now returns the instance and we have assigned that instance to varaible my_book

# accessing attributes
print(f"{my_book.name}'s author is {my_book.author}.")