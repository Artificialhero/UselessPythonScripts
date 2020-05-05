#This is to understand classes and maybe use as template whenever i use it. 
#With help from realpython.com

class Cat:
    #Class Attribute, valid for all cats
    looks = 'CUTE!'
    
    #Initializer / Instance attributes
    def __init__(self, name, age): #self refers to the object itself (Cat.)
        self.name = name
        self.age = age
        
    #Instance method
    def description(self):
        return "{} is {} years old.".format(self.name, self.age)
    #Instance method
    def talk(self, sound):
        return "{} sounds like {}".format(self.name, sound)
        
# Make the cat object
cathulu = Cat("Cathulu", 2)
tindra = Cat("Tindra",9)

#Access the attributes

if cathulu.looks == "CUTE!":
    print("{0} is {1}!".format(cathulu.name, cathulu.looks))
    
#Get oldest cat
def biggestNumber(*args):
    return max(args)

print("The oldest cat is {} years old".format(
    biggestNumber(cathulu.age, tindra.age)))

#Call instance methods
print(cathulu.description())
print(tindra.talk("Meeeuow"))
    
