
class Computer:
    instrument_type = "consumer_electronics"
    def __init__(self, model, brand, yom, price, type):
        self.model = model
        self._brand = brand     # private
        self.yom = yom
        self._price = price     # private
        self._type = type       # private
    
    # using the property decorator to alias default attributes! 
    @property
    def brand(self):
        return self._brand
    @property
    def price(self):
        return self._price
    @property
    def type(self):
        return self._type


Dell_3501 = Computer("Inspiron", "DELL", 2020, 780, "Laptop")
Tower_7XX = Computer("Tower 7XR", "DELL", 2019, 3060, "Server")

Dell_3501.brand
Dell_3501._brand
Tower_7XX.price
Tower_7XX._price

class Fan:
    model = "Table fan"     # class attribute
    def __init__(self, model, yom, warranty = True, price=500):
        self.model = model
        self._price = price
        self._yom = yom
        self.warranty = warranty

    def set_price(self, value):
            if (type(value) == int or type(value) == float):
                if value > 50:
                    self._price = value
                elif value <= 50:
                    raise ValueError("Price too small!")
            elif type(value) != int:
                raise TypeError("Invalid Input!")
            return self._price

Nippon = Fan("N012", 2018, False, 400)
Nippon.set_price(30)
Nippon.set_price(67.7764)
Nippon.set_price("hbh")
