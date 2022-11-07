# customer wants you to build a simple calculator
# user can pass a maximum of three inputs, if inputs are over 3 an exception must be thrown
# if the calculator receives no inputs, then the result must be zero
# users can only enter integers, floating points are not allowed
# users cannot enter non-numeric values, if such are pased exception must be thrown
# users cannot pass values higher than 100, if passed exception must be thrown

# we will import this Python script as a module ans use this class for unittesting!
class Calculator:
    def addNumbers(self, *args):
        total = 0
        for i in args:
            if type(i) == float:
                raise TypeError("Floating point inputs are not accepted!")
            elif type(i) == str:
                raise TypeError("String inputs are not accepted!")
            elif i > 100:
                raise ValueError("Values above 100 are not accepted!")
            elif i == None:
                return 0
            elif type(i) == int:
                total += i
        return total
