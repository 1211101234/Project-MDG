import sqlite3

import Database

print('MDG Automotive Inventory')

class Automobile:
    def __init__(self):
        self._make = ''
        self._model = ''
        self._year = 0
        self._color = ''
        self._mileage = 0

    def add_vehicle(self):
        try:
            self._make = input('Enter vehicle make: ')
            self._model = input('Enter vehicle model: ')
            self._year = int(input('Enter vehicle year: '))
            self._color = input('Enter vehicle color: ')
            self._mileage = int(input('Enter vehicle mileage: '))
            return True
        except ValueError:
            print('Please try entering vehicle information again using only whole numbers for mileage and year')
            return False

    def __str__(self):
        return '\t'.join(str(x) for x in [self._make, self._model, self._year, self._color, self._mileage])

class Inventory:
    def __init__(self, db_name):
        self.db = Database(db_name)

    def add_vehicle(self):
        vehicle = Automobile()
        if vehicle.add_vehicle() == True:
            self.db.add_vehicle(vehicle._make, vehicle._model, vehicle._year, vehicle._color, vehicle._mileage)
            print('This vehicle has been added, Thank you')

    def view_inventory(self):
        vehicles = self.db.view_inventory()
        print('\t'.join(['ID', 'Make', 'Model', 'Year', 'Color', 'Mileage']))
        for idx, vehicle in enumerate(vehicles):
            print('\t'.join(map(str, vehicle)))

    def delete_vehicle(self):
        self.view_inventory()
        vehicle_id = int(input('Please enter the ID associated with the vehicle to be removed: '))
        self.db.delete_vehicle(vehicle_id)
        print('This vehicle has been removed')

    def update_vehicle(self):
        self.view_inventory()
        vehicle_id = int(input('Please enter the ID associated with the vehicle to be updated: '))
        automobile = Automobile()
        if automobile.add_vehicle() == True:
            self.db.update_vehicle(vehicle_id, automobile._make, automobile._model, automobile._year, automobile._color, automobile._mileage)
            print('This vehicle has been updated')

    def export_inventory(self):
        vehicles = self.db.view_inventory()
        with open('vehicle_inventory.txt', 'w') as f:
            f.write('\t'.join(['ID', 'Make', 'Model', 'Year', 'Color', 'Mileage']) + '\n')
            for vehicle in vehicles:
                f.write('\t'.join(map(str, vehicle)) + '\n')
        print('The vehicle inventory has been exported to a file')

    def close(self):
        self.db.close()

# Main program
inventory = Inventory('mdg_inventory.db')
while True:
    print('#1 Add Vehicle to Inventory')
    print('#2 Delete Vehicle from Inventory')
    print('#3 View Current Inventory')
    print('#4 Update Vehicle in Inventory')
    print('#5 Export Current Inventory')
    print('#6 Quit')
    user_input = input('Please choose from one of the above options: ')
    
    if user_input == "1":
        inventory.add_vehicle()
    elif user_input == '2':
        inventory.delete_vehicle()
    elif user_input == '3':
        inventory.view_inventory()
    elif user_input == '4':
        inventory.update_vehicle()
    elif user_input == '5':
        inventory.export_inventory()
    elif user_input == '6':
        inventory.close()
        print('Goodbye')
        break
    else:
        print('This is an invalid input. Please try again.')
