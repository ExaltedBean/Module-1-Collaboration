# -----------------------------------------------------------
# Student Name: Ean Miller
# File Name: Module 3 Lab Ean Miller.py
# Description:
#   This program defines a Vehicle superclass and an Automobile
#   subclass. The user is prompted to enter information about a
#   car, including year, make, model, number of doors, and roof
#   type. The program stores this data in an Automobile object
#   and displays the information in a formatted output.
#
# Variables:
#   vehicle_type - stores the type of vehicle ("car")
#   year         - stores the vehicle's manufacturing year
#   make         - stores the manufacturer of the vehicle
#   model        - stores the model name of the vehicle
#   doors        - stores the number of doors (2 or 4)
#   roof_type    - stores the type of roof (solid or sun roof)
# -----------------------------------------------------------

print("---- Car Stats Display ----")

vehicle_type = "car"
# Get user input for the vehicle attributes
year = input("Enter the year of the vehicle: ")     
make = input("Enter the make of the vehicle: ")
model = input("Enter the model of the vehicle: ")
doors = input("Enter the number of doors (2 or 4): ")
roof_type = input("Enter the type of roof (solid or sun roof): ")
# defining the vehicle class (which will be used as a superclass)
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
# defining the automobile class (which will be used as a subclass)
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof_type):
        super().__init__(vehicle_type) # Borrowed from superclass Vehicle
        self.year = year    # each attribute is defined by this subclass
        self.make = make
        self.model = model
        self.doors = doors
        self.roof_type = roof_type
# Create an instance of the Automobile class with the user input
my_vehicle = Automobile(vehicle_type, year, make, model, doors, roof_type)
# Display the vehicle information
print(f"""
Vehicle type: {my_vehicle.vehicle_type}
Year: {my_vehicle.year}
Make: {my_vehicle.make}
Model: {my_vehicle.model}
Number of doors: {my_vehicle.doors}
Type of roof: {my_vehicle.roof_type}
""")
