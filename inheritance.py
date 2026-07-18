# one class inherits from another
# orginal class is called parent
# new class is called child
# child class can inherit any or all attributes and methods
# from parent class
# child class can define new attributes and methods of its own
class Computer:
    def __init__(self, company, model, year):
        self.company= company
        self.model= model
        self.year= year

    def get_name(self):
       name=f"{self.company} {self.model} {self.year}"
       return name.title()

    def specs(self, chip, ram, rom):
        print(f"{self.get_name()} has {chip} chip, {ram} RAM and {rom} ROM")

class Laptop(Computer):
    def __init__(self, company, model, year):
        #super fucntion is a special function that allows
        # you to call a method from the parent class
        super().__init__(company, model, year)
        #defining attributes for child class
        self.battery_capacity= 8
        self.processor = Processor()

    def portability(self):
        print(f"Laptop is Portable and has battry capacity of {self.battery_capacity}hr.")



#jastai class create gardaa
# sometimes we tend to create lots of attributes and methods
# which will eventually make your classs lengthy
# so instead of thupaaring everything in one place 
# we can write similar methods and attributes in another class
# meaning we can break large class into smaller classes that work together
# this approach is called composition

#this below class doesnot inherit from any class
class Processor:
    def __init__(self, core1=8, core2=8):
        self.core1=core1
        self.core2=core2

    def describe_processor(self):
        print(f"It has {self.core1} core CPU and {self.core2} core GPU")


pc=Laptop('Macbook', 'Air', 2020)
print(pc.get_name())
pc.portability()
pc.processor.describe_processor()# look at instance pc, find processor attribute 
# and call the method describe_processro() that is associated with Processor instance
# # assigned to the attribute 