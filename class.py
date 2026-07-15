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
        