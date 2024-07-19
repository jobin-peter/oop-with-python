from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, model, make, year,num_doors) -> None:
        super().__init__(model, make, year)  # Super function is used with __init__() method to initialize the attributes of parent class
        self.__num_doors = num_doors
    
    def get_num_doors(self):
        return self.__num_doors
        
    def set_num_doors(self,num_doors):
        self.__num_doors = num_doors
    
    def display(self):
        return f"{super().display()}, Doors: {self.__num_doors}"
    