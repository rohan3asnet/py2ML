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

pc=Laptop('Macbook', 'Air', 2020)
print(pc.get_name())