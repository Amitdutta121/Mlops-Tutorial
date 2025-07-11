class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")



class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.behiveour = "friendly"
    def speak(self):
        print(f"{self.name} barks because .")



animal = Animal()
animal.speak()

animal = Dog()
animal.speak()