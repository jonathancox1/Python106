#
#
#
#
#Basic Object Oriented Programing
#Notes


#how to create a class
class Hotel():
    pass

#create instances of the class
bates_motel = Hotel()
grand_budapest = Hotel()

#create unique instance of the class
class Hotel():
    #Constructor
    #can contain default properties, must come after required properties
    def __init__(self, name_of_hotel, location, slogan='this is the default slogan'):
        self.name = name_of_hotel
        self.location = location
        self.slogan = slogan

    #Representation
    #can be useful to set the default return of calling the instance
    #ex bates_motel returns Bates Motel, America, this is the default slogan
    def __repr__(self):
        return(f'{self.name}, {self.location}, {self.slogan}')

    #A function inside the class
    def info(self):
        print(f'{self.name} is a hotel in {self.location}')

#create instance of hotel class with properties
bates_motel = Hotel('Bates Motel', 'America')
grand_budapest = Hotel('Grand Budapest', 'Budapest')

print(bates_motel.name)
# Bates Motel

print(bates_motel.info())
# Bates Motel is a hotel in America
print(bates_motel.slogan)
# this is the default slogan

#Reassignment
bates_motel.slogan = 'Happiest Place On Earth!'
print(bates_motel.slogan)

#call __repr__
bates_motel



#import from another file
from python_file_name import Class_Name


#keep all the class files in their own folder called lib
#in that folder there should be a file called
# __init__.py that is empty file in the folder containg the Classes

#access that by
from lib.superhero import Superhero
from lib.villan import Villan

#in those .py files
#access the super Class again
from lib.character import Character


#inherit method from parent class but add its own customizations
#def strike is defined in the superClass
def strike(self, target):
    #super() inherits the following Method and allows you to add
    #customization for this specific class
    super().strike(target)
