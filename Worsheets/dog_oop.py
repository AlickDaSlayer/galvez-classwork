
class Dog():
    def __init__(self, dogName, myColour):
        self.__name = dogName
        self.__colour = myColour

    def bark(self, barkTimes):
        for n in range (barkTimes):
            print(self.__name + " says Woof!")
    #end function

    def setColour(self, myColour):
        self.__colour = myColour
    #end procedure

    def getColour(self):
        return self.__colour
    #end function

    def getname(self):
        return self.__name
    #end function

    def printDogDetails(self):
        print(self.__name, self.__colour)
    #end function
class Puppy(Dog):
    def __init__(self, dogName, myColour):
        super().__init__(dogName, myColour) # - Dog Constructor
        self.__shoesChewed = 0
    #end procedure

    def chewShoe(self, myShoesChewed):
        self.__shoesChewed = self.__shoesChewed + myShoesChewed
    #end procedure

    def getShoesChewed(self):
        return self.__shoesChewed
    #end function

    def bark(self, barkTimes):
        super().bark(1)
        for n in range(barkTimes):
            print("Yap!")
    #end function

myDog1 = Dog("Mutt", "Light Brown")
mypuppy1 = Puppy("Malla", "Black")
myDog1.bark(3)
mypuppy1.bark(3)

my_animal_list = [myDog1,mypuppy1]

for animal in my_animal_list:
    animal.bark(3)
