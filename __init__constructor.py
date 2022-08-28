# a sample class with init method

class Person:
    # init method or constructor

    def __init__(self, name, age):
        self.name = name
        self.age = age

        # sample method

    def greet(self):
        print("Good Morning, I am",self.name)
        print("My age is", self.age,"years")

per = Person("Omkar",27)
per.greet()

print()