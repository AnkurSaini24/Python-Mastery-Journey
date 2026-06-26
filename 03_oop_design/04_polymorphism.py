class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# using polymorphism         
def animal_sound(animal):

    print(animal.speak())


# creeating object
dog = Dog()
cat = Cat()

animal_sound(dog)  # output: Woof!
animal_sound(cat)  # output: Meow!