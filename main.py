# main.py
from car import Car
from motorbike import Motorbike
from vehiclemanager import VehicleManager

def main():
    # Create a Vehicle Manager
    manager = VehicleManager()

    # Create some vehicles
    car = Car("Honda","City", 1996, 4)
    motorbike = Motorbike("Suzuki", "Hayabusa", 2007, True)

    # Add vehicles to the manager
    manager.add_vehicle(car)
    manager.add_vehicle(motorbike)

    # Display all vehicles
    print("All vehicles in the system:")
    for vehicle_info in manager.display_all_vehicles():
        print(vehicle_info)

    # Find a vehicle by make and model
    found_vehicle = manager.get_vehicle("Suzuki", "Hayabusa")
    if found_vehicle:
        print("\nFound vehicle:")
        print(found_vehicle.display())
    else:
        print("\nVehicle not found.")

    # Remove a vehicle by make and model
    manager.remove_vehicle("Honda", "City")

    # Display vehicles after removal
    print("\nVehicles in the system after removal:")
    for vehicle_info in manager.display_all_vehicles():
        print(vehicle_info)

if __name__ == "__main__":
    main()
