# Activity 2: Polymorphism Challenge 🎭
# Topic ; Polymorphism in Classes
class Dog:
    def move(self):
        print("🐕 Running on the ground...")

class Bird:
    def move(self):
        print("🐦 Flying in the sky...")

class Fish:
    def move(self):
        print("🐟 Swimming in the water...")

# Creating objects
dog = Dog()
bird = Bird()
fish = Fish()

# Calling the move() method for each animal
animals = [dog, bird, fish]

for animal in animals:
    animal.move()  # Each animal responds differently
