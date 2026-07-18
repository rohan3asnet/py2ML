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