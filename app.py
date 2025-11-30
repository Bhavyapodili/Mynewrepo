class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy", "Golden Retriever")
print(f"My dog's name is {my_dog.name} and he is a {my_dog.breed}.")
my_dog.bark()
