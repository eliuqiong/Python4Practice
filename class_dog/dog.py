class Dog:
    """try to mimic a dog"""

    def __init__(self, name, age):
        """initialize name and age"""
        self.name = name
        self.age = age
    
    def sit(self):
        """ask the dog to sit when ordered"""
        print(f"{self.name} is now sitting down.")

    def roll_over(self):
        """ask the dog to roll over when ordered"""
        print(f"{self.name} is now rolling over.")


my_dog = Dog("willie",6)

print(f"my dog's name is {my_dog.name}")

my_dog.sit()
my_dog.roll_over()