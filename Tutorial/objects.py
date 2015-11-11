class Person(object):
    species ="Human"
    def __init__(self, name):
        self.name =name
        self.age=42

    def describe(self):
        print self.name
        print self.age
    
    def introduce(self):
        return "I am {0} and I am {1} years old".format(self.name,self.age)




    """
    @classmethod
    def speak(cls, arg):
        print cls, arg
        return "I am speaking"
    """
"""
print Person.species
print Person.speak("buhja")
"""


alice= Person("Alice")
bob = Person("Bob")


alice.describe()
bob.describe()

print alice.introduce()
print bob.introduce()
