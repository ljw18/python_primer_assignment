class KitchenAppliance:
    def __init__(self, model_number, brand, year_manufacture):
        self.model_number = model_number
        self.brand = brand
        self.year_manufacture = year_manufacture
    
    def report(self):
        print("This is the " + self.brand + " " + str(self.model_number) + " manufactured in " + str(self.year_manufacture) + ".\n")