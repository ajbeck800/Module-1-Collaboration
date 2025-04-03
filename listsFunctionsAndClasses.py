#Author: AJ Beck
#File Name: listsFunctionsAndClasses.py
#Description: Python app that accepts vehicle type, year, make, model, number of doors, and type of roof and stores them in classes.

#Write an app that will accept user input for a car. The app will store "car" into the vehicle type in your Vehicle super class. 
#The app will then ask the user for the year, make, model, doors, and type of roof and store the data in the attributes above.
#The app will then output the data in an easy-to-read and understandable format, such as this:
# Vehicle type: car
# Year: 2022
# Make: Toyota
# Model: Corolla
# Number of doors: 4
# Type of roof: sun roof

#Super class which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick
class Vehicle:
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType

#Class which inherits the attributes from Vehicle and also contains year, make, model, number of doors, and roof type
class Automobile(Vehicle):
    def __init__(self, year, make, model, numDoors, roofType):
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.numDoors = numDoors
        self.roofType = roofType
    
#Function to ask user for year, make, model, number of doors, and type of roof
def getAutomobileInfo():
    print("Please enter the following details about your car:")
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    numDoors = input("Number of doors (2 or 4): ")
    roofType = input("Type of roof (solid or sun roof): ")
    return Automobile(year, make, model, numDoors, roofType)

#Display the data
def displayAutomobileInfo(automobile):
    print("\nVehicle Information:")
    print(f"Vehicle type: {automobile.vehicleType}")
    print(f"Year: {automobile.year}")
    print(f"Make: {automobile.make}")
    print(f"Model: {automobile.model}")
    print(f"Number of doors: {automobile.numDoors}")
    print(f"Type of roof: {automobile.roofType}")

#Ask user for input of vehicle type
print("Please enter what type of vehicle you own:")
vehicleType = input("Vehicle type: ")

#Displays information about user's vehicle if it is a car
if vehicleType == "car":
    automobile = getAutomobileInfo()
    displayAutomobileInfo(automobile)