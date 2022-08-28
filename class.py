# create a normal class and define its attributes
# called as class instantiation

class Dog:

    # class variable
    attr1 = "Mammal"
    attr2 = "Dog"

    # the init method or constructor
    def __init__(self,name, breed, color):
        
        # instance variable
        self.name = name
        self.breed = breed
        self.color = color

    # sample method
    def fun(self):
        print("Details of:",self.name)
        print(self.name,"is",self.attr1, "and he is a",self.attr2)
        print("His Breed is",self.breed, "& color is",self.color)
        # print("\n")

    # add instance variable inside the method
    def setHeight(self,height):
        self.height = height

    # retrives instance variable from method
    def getHeight(self):
        return self.height

    
       

# object1 instantiation
Dog1 = Dog("Moti","Pug","Brown")
Dog1.fun()
Dog1.setHeight("1.1 ft\n")
print("The height of",Dog1.name,"is",Dog1.getHeight())

# object2 instantiation
Dog2 = Dog("Dunzo","Bulldog","Black")
Dog2.fun()
Dog2.setHeight("1.6 ft\n")
print("The height of",Dog2.name,"is",Dog2.getHeight())

#class variable can also be accessed using class name also
print(Dog.attr1, Dog.attr2)

print('harry')
