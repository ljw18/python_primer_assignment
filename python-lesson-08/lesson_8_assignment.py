class SmartDevice:

    def __init__(self, model_number, brand, screen_size, app_list=[]):
        self.model_number = model_number
        self.brand = brand
        self.screen_size = screen_size
        self.app_list = app_list

    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand,"\n")

    def install_app(self, app_name='Settings'):
        print(f"Installing {app_name}...\n")
        if app_name not in self.app_list:
            self.app_list.append(app_name)
        return self.app_list
    
    def delete_app(self, app_name):
        if app_name in self.app_list:
            self.app_list.remove(app_name)
            print(f"Deleting {app_name}...\n")
        return self.app_list
    
 

device_a = SmartDevice(1233244, 'CLG', 5.7)
device_a.report()

device_a.install_app("Pacman")
device_a.install_app()
device_a.install_app()
device_a.install_app("Pacman")
device_a.install_app("Galaga")
print(device_a.app_list,"\n")

device_a.delete_app("Galaga")
print(device_a.app_list,"\n")




# I tried to add device_b but it kept including the apps that were on device_a but not on device_b - I didn' have a chance to look at why this was occuring

#   device_b = SmartDevice(996688, 'AAA', 6.6)
#   device_b.report()

#   device_b.install_app("Stan")
#   device_b.install_app()
#   device_b.install_app()
#   device_b.install_app("Stan")
#   device_b.install_app("Netflix")
#   print(device_b.app_list,"\n")

#   device_b.delete_app("Netflix")
#   print(device_b.app_list,"\n")

#   print(device_a.app_list)