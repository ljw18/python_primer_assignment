from coffee_machine import SmartCoffeeMachine


my_coffee_machine = SmartCoffeeMachine(model_number = 3000, brand = 'Cafe Ole', year_manufacture= "2020", version="deluxe")


options = [
    "1. Coffee menu",
    "2. Order a coffee",
    "3. Add a coffee to the menu",
    "4. Coffee machine information",
    "5. Exit" ]

def machine_options():
    print("\nWelcome to the " + my_coffee_machine.brand + " " + str(my_coffee_machine.model_number)+"\n")
    while True:
        
        print(*options, sep= " \n")
        option_choice = input("\nPlease choose an option number: ")
    
        if option_choice == "1":
            print(*my_coffee_machine.coffee_menu, sep= " \n")
                
        elif option_choice =="2":
            coffee_type = input ("What type of coffee would you like? ")
            my_coffee_machine.make_coffee(coffee_type)
    
        elif option_choice =="3":
            new_coffee = input ("What type of coffee would you like to add? ")
            my_coffee_machine.update_menu(new_coffee)
    
        elif option_choice =="4":
            my_coffee_machine.report()
    
        elif option_choice =="5":
            print ("Goodbye...")
            break
        input ("\nPress enter to return to the main menu\n")
            
        
machine_options()
