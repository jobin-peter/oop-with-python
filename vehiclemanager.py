from vehicle import Vehicle
from car import Car
from motorbike import Motorbike

class VehicleManager:
    def __init__(self):
        self.__vehicles = []

    def add_vehicle(self, vehicle):
        if isinstance(vehicle, Vehicle):
            self.__vehicles.append(vehicle)

    def remove_vehicle(self, make, model):
        self.__vehicles = [vehicle for vehicle in self.__vehicles if vehicle.get_make() != make or vehicle.get_model() != model]

    def get_vehicle(self, make, model):
        for vehicle in self.__vehicles:
            if vehicle.get_make() == make and vehicle.get_model() == model:
                return vehicle
        return None

    def display_all_vehicles(self):
        return [vehicle.display() for vehicle in self.__vehicles]