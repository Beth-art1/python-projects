# Assignment 1: Design Your Own Class! 🏗️
# Topic: Classes, Constructors, Inheritance, and Polymorphism

# Parent Class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def make_call(self, contact):
        print(f"📞 Calling {contact} from {self.brand} {self.model}...")

    def phone_info(self):
        print(f"📱 {self.brand} {self.model} - {self.storage}GB storage")

# Child Class (Inheritance + Polymorphism)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, refresh_rate):
        # call parent constructor
        super().__init__(brand, model, storage)
        self.refresh_rate = refresh_rate

    # Polymorphism: Overriding a method from the parent
    def phone_info(self):
        print(f"🎮 {self.brand} {self.model} - {self.storage}GB, {self.refresh_rate}Hz refresh rate")

    def launch_game(self, game):
        print(f"🔥 Launching {game} on {self.brand} {self.model}...")

# Creating objects (instances)
phone1 = Smartphone("Samsung", "Galaxy A55", 128)
phone2 = GamingPhone("Asus", "ROG 8 Pro", 256, 165)

# Using methods
phone1.phone_info()
phone1.make_call("Beth")

phone2.phone_info()      # Demonstrates polymorphism
phone2.launch_game("Farm Heroes")
