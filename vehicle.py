class Vehicle:
    # __init__ method [Magic Method]
    def __init__(self,model,make,year) -> None:
        self.__make = make      # __variable - Private attributes and Name mangling
        self.__model = model
        self.__year = year
    
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__make
    def get_year(self):
        return self.__make
    def display(self):
        return f"{self.__year} {self.__make} {self.__model}"
