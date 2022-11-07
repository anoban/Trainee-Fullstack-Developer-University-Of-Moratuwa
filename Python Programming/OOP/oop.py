# create a class "dragon"

from typing_extensions import Self


class Dragon:
    def __init__(self, name, age, color, type):
        self.name = name
        self.age = age
        self.color = color
        self.type = type

Anubis = Dragon("Anubis",1E19,"Crimson","Fire breathing")
Anubis.age
Anubis.color
Anubis.type


Achilles = Dragon("Achilles", 767, "Blue", "Water dragon")
Achilles.type
Achilles.color
Achilles.color = "Pink"
Achilles.color

# declaration of a class, where object instantiation needs manual passing of all the atributes on creation!
# i.e when the constructor is called we have to specify all the attributes within the brackets!
class Car:
    def __init__(self, Model, Brand, Make, YOM, EngineCC, RegistrationYear, Color):
        # instance attributes
        self.Model = Model
        self.Brand = Brand
        self.Make = Make
        self.YOM = YOM
        self.EngineCC = EngineCC
        self.reg = RegistrationYear
        self.color = Color

Corolla = Car("Corolla", "Toyota", "Japan", 2011, 2800, 2016, "Metallic Silver")
Corolla.color
Corolla.Make
Corolla.reg
Corolla.EngineCC

# declaration of a class, where object instantiation needs manual attribute inputs with fallback defaults for some attributes!
class Car:
    def __init__(self, Model="Az9X", Brand="AMG", Make="German", YOM=2018, EngineCC, RegistrationYear, Color):
        # instance attributes
        self.model = Model
        self.brand = Brand
        self.make = Make
        self.yom = YOM
        self.cc = EngineCC
        self.reg = RegistrationYear
        self.col = Color

# it is not necessary to define a constructor to a class!
# i.e in such cases a super class constructor is used to initialize class objects!
class Car:
    def __init__(self):
        # pre defined instance attributes
        self.model = "X10"
        self.brand = "BMW"
        self.make = "Bavaria"
        self.yom = 2018
        self.cc = 3650
        self.reg = 2021
        self.col = "Metallic Blue"

# defining a method (behaviour) to carr class!
class Car:
    def __init__(self, Model, Brand, Make, YOM, EngineCC, RegistrationYear, Color):
        # instance attributes
        self.Model = Model
        self.Brand = Brand
        self.Make = Make
        self.YOM = YOM
        self.EngineCC = EngineCC
        self.reg = RegistrationYear
        self.color = Color
    def crash(self, car):
        self.color, car.color = "Scratches","Scratches"
Corolla = Car("Corolla", "Toyota", "Japan", 2011, 2800, 2016, "Metallic Silver")
X3 = Car("X3", "BMW", "German", 2018, 3400, 2019, "Navy Blue")
X3.crash(Corolla)
X3.color
Corolla.color

class customer:
    bank = "Bank of Zombizia"
    def __init__(self, IC_no, name, age, account_type):
        self.icno = IC_no
        self.name = name
        self.age = age
        self.act_type = account_type
        self.balance = 10000
    def lottery(self,boolean):
        if boolean == True:
            self.balance += 100000
            return self.balance
    def loan(self,boolean):
        if boolean == True:
            self.balance -= 4500
            return self.balance

customer.bank

Natalie = customer("9812354V", "Natalie Martinez", 29, "Savings")
Natalie.bank
Natalie.age
customer.bank == Natalie.bank

Natalie.lottery(True)
Natalie.balance
Natalie.loan(True)
Natalie.balance
# perfecto!