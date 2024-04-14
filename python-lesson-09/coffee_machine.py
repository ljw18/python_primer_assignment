from kitchen_appliance import KitchenAppliance


class SmartCoffeeMachine(KitchenAppliance):
    def __init__(self, model_number, brand, year_manufacture, version, coffee_menu=["flat white"]):
        KitchenAppliance.__init__(self, model_number, brand, year_manufacture)
        self.coffee_menu = coffee_menu
        self.version = version

    def report(self): #attempting polymorphism - method overriding
        print("This is the " + self.version + " model of the " + self.brand + " " + str(self.model_number) + " manufactured in " + str(self.year_manufacture) + ".\n")
            

    def update_menu(self, new_coffee):      
        if new_coffee not in self.coffee_menu:
            self.coffee_menu.append(new_coffee)
            print(f"New menu item added: {new_coffee}\n")   
            

    def make_coffee(self, coffee_type):
        if coffee_type in self.coffee_menu:
            print(f"Great selection. I'll make that for you now!\n")
        else:
            print(f"Sorry that coffee is not yet on our menu.\n")  


