class reader:
    def __init__(self, id, first_name, last_name, age, residence, occupation):
        print("Instantiating a reader object!.....")
        self._id = id
        self.fname = first_name
        self.lname = last_name
        self.age = age
        self.where = residence
        self.what = occupation
  
    def fee(self):
        if self.age < 10:
            print("Too young for a membership! Bring a parent or a guardian!")
        elif self.age in range(10,21):
            print("Monthly membership fee is 250/=")
        elif self.age in range(21,40):
            print("Monthly membership fee is 350/=")
        elif self.age >= 40:
            print("Monthly membership fee is 400/=")

John = reader("1994SV100", "Johnson", "Paddington", 34, "San Jose", "Clerk")
Samantha = reader("1999RF563", "Samantha", "Fox", 22, "Canton", "Nurse")

John.fee()
Samantha.fee()

Kid = reader("2015DF673", "Novah", "Johnson", 9, "Pheonix", None)
Kid.fee()

class students(reader): # inheritance
    def __init__(self, id, first_name, last_name, age, residence, occupation):
        super().__init__(id, first_name, last_name, age, residence, occupation)
        self.discount = None # unique instance attributes
        self.is_eligible = False
    

    def isdiscount(self):
        if int(self._id[0:4]) < 2019:
            self.is_eligible = True
            self.discount = 100
        return self.discount

Jimmy = students("2015DF345", "Jimmy","Jenson", 13, "DC", None)
Jimmy.isdiscount()
Jimmy._id