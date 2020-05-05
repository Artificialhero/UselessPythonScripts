
class Person:
    
    #Class attribute
    species = 'Mammal'
    
    def __init__(self, name, age, personality):
        self.name = name
        self.age = age
        self.personality = personality
        
    #INstance methods
    def description(self):
        return "{} is {} years old. Personality is {}".format(self.name, self.age, self.personality)
        
    def speak(self, word):
        return "{} would say {}".format(self.name, word)
    
    #Childclass, inherits person class
class ShrineMaiden(Person):
    def clothes(self, wear):
        return "{} often wears {}".format(self.name, wear)
        
class Witch(Person):
    def clothes(self, wear):
        return "{} often wears {}".format(self.name, wear)

class Maid(Person):
    def clothes(self, wear):
        return "{} often wears {}".format(self.name, wear)
        
#Demonstrating how we inherit child classes from parent classes
reimu = ShrineMaiden("Reimu Hakurei", 16, "Like a teenager")
print(reimu.description())
print(reimu.clothes("Red ribbon"))
print(isinstance(reimu, Person))

marisa = Witch("Marisa Kirisame", 15, "Relaxed and greedy")
print(marisa.description())
print(isinstance(marisa, Person))

player = Person("???","?","???")
print("Is the player a person too? " + str(isinstance(player,Person)))
print("Is the player a maid? " + str(isinstance(player,Maid)))
