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

#storing multiple classes in a module
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


class Processor:
    def __init__(self, core1=8, core2=8):
        self.core1=core1
        self.core2=core2

    def describe_processor(self):
        print(f"It has {self.core1} core CPU and {self.core2} core GPU")