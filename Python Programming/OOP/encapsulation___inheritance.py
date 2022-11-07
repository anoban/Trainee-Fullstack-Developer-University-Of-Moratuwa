class planet:
    def __init__(self, name, radius, temp, mean_surface_temperature, core_temperature, life):
        # all are private instance attributes
        self._name = name
        self._radius = radius  # numeric
        self._temp = temp       # numeric
        self._msftemp = mean_surface_temperature        # numeric
        self._ctemp = core_temperature      # numeric
        self._life = life       # must be a boolean
        # we cannot add data validations to attributes here!
Pluto = planet("Pluto", 464.28, 3.4E5, 349, 7.194E19, False)
Pluto._life
Pluto._life = "Puff so much for private attributes huh?"
Pluto._life # :((

# by convention we are sxpected not to access such attributes directly by calling object._whateverattribute!!

# @property decorator is used to invoke class attributes via aliases!, that can accept optional data validation restrictions!
class planet(object):
    def __init__(self, name, radius, temp, mean_surface_temperature, core_temperature, life):
        self._name = name
        self._radius = radius  
        self._temp = temp      
        self._msftemp = mean_surface_temperature      
        self._ctemp = core_temperature     
        self._life = life   

        @property
        def name(self):
            return self._name
        @property
        def radius(self):
            return self._radius
        @property
        def temp(self):
            return self._temp
        @property
        def life(self):
            return self._life
        
        @name.setter
        def set_name(self, name):
            if type(name) != str:
                raise TypeError("Invalid Input!")
            elif len(name) < 2:
                raise ValueError("Name too short!")
            elif len(name) > 15:
                raise ValueError("Try a shorter name!")
            else:
                self._name = name
            print("Name of {} is {}".format(self, self._name))

Jupyter = planet("Jupiter", 2.435E45, 786, 108, 6.76E11, False)
Jupyter.name()
Jupyter.set_name("Jupyter")