class birds: # superclass or parent class
    order = "Saurischia" # class attribute!, shared by all instances 
    def __init__(self,habitat, size, sucklings): # super class constructor!
        print("Building a new instance of Bird!")   # a placeholder print statement to see where this constructor is invoked!
        self.n_legs = 2 # hard coded instance attribute!
        self._hab = habitat     # private instance attributes!
        self._size = size
        self._progeny = sucklings
    # an class method to retrieve size of the bird!
    def getsize(self):
        return self._size
    # a class method to emulate reproduction
    def propagate(self, val):
        self._progeny += val


# create an instance of bird class!
parrot = birds("Coconut trees", "Small", 0)
# __init__() was invoked!!! wooow :))))

parrot.n_legs # a hardcoded instance attribute
parrot.order # a class attribute
parrot.order == birds.order # True!
parrot._hab

parrot._size
parrot.getsize() # wrapper works!
parrot._size == parrot.getsize() # True

parrot._progeny # 0
parrot.propagate(3)
parrot._progeny # 3 woohooo :)))

class crow(birds): # inheritance
    pass # just a carbon copy of birds class!
# inherits the superclass attributes and the instance attributes!
mycrow = crow("Cosmopolitan", "small", 0)
# invokes the parent class's __init__() method!! implicitly
mycrow.order # works!
mycrow.n_legs # 2
mycrow.getsize()

# inheritance with parent instance members!

class peacock(birds): # inheritance from super class
    def __init__(self, habitat, size, sucklings): # explicit invocation of parent class's constructor!
        super().__init__(habitat, size, sucklings)  # inherits all instance members
        self.color = "Blue violet" # adding a new instance attribute
# addition of new attributes cannot be done when the parent class's constructor is called implicitly!
# as in the previous example!

my_peacock = peacock("Wild", "Large", 1)
# this invoked the parent class's __init__() method!!!
my_peacock.color # new method of the subclass!
my_peacock._size
my_peacock.order

# note that inheritance passes down the instance members of parant class!
# but not the instance member values!!!!!

mommys_peacock = peacock() 
# cannot create
# won't inherit values of the instance members!!