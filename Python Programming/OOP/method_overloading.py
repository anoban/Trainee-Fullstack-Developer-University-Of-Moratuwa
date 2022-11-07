class person:
    def __init__(self, title="default title"):
        self._name = None
        self.title = title
    def talk(self, words):
        print(words)
    def talk(self, words, exclaim):
        print("{}".format(words), end=exclaim)
person1 = person()
person1.talk("Hello","!\n")
# Python does not support method overloading!
# we can overload methods but only the latest defined method will be applied!!
# that's why the .talk() method executed the instructions of second definition!!