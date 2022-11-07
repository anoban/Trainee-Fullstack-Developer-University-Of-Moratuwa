from abc import abstractmethod

class squad: # parent class
    def __init__(self, id, name, age): # constructor
        print("Instantiating a squad object......")
        self._id = id  # private instance attribute
        self.name = name  # public instance attribute
        print("Done....squad object {} has been instantiated!".format(self.name))
        self.age = age
        self.life = 100 # hard coded instance attribute
    @abstractmethod
    def attack(self, target): # an abtract method
        pass
    # this abstarct method just indicates that members of squad class can attack!
    # i.e they have a method\behaviour attack!
    # we do not specify any ways to implement the attack since it will be very vague to implement at this level!!! 



# when a member of elite squad attacks, the target dies instantly!!!
class elite_squad(squad): # subclass with inheritance!!
    def __init__(self, id, name, age):
        super().__init__(id, name, age)
    def attack(self, target): # overriding the inherited .attack() method!!
        print("{} has been successfully eliminated!".format(target.name))
        target.life = None
        print("Operation successful!")

# when a rookie squad attacks target loses 20% of his life!
class rookie(squad):
    def __init__(self, id, name, age):
        super().__init__(id, name, age) # inheritance
    def attack(self, target):  # overriding the inherited .attack() behaviour!!
        target.life -= target.life * .2
        print("Mission accomplished!!")
        print("Remaining life of {} is {}".format(target.name, target.life))

JimmyTheRookie = rookie("Duck", "Jamal", 29)   
JamesTheVeteran = elite_squad("Falcon", "Jameson", 44)
dummyTarget = squad("Target", "Nate", 22)

JimmyTheRookie.attack(dummyTarget)
# Mission accomplished!!
# Remaining life of Nate is 80.0
dummyTarget.life # 80.0
# woohooo :)

JamesTheVeteran.attack(dummyTarget)
# Nate has been successfully eliminated!
# Operation successful!
dummyTarget.name
dummyTarget.life