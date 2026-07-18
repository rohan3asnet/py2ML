# # importing a single class
# from computer import Computer

# #importing multiple classed from a module
# from computer import Computer, Laptop

# pc= Computer('Dell', 'Inspiron', 2023)
# print(pc.get_name())
# pc1=Laptop('Lenovo', 'ThinkPad', 2016)
# print(pc1.get_name())

#importing an entire module
import computer

pc= computer.Computer('Dell', 'Inspiron', 2023)
print(pc.get_name())

pc1=computer.Laptop('Lenovo', 'ThinkPad', 2016)
print(pc1.get_name())

# importing all classes from a module
# from module_name import *

# you can use aliases similar to function for classes too.
# explore different modules built by others yourself.