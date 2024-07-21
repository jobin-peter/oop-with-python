class Vehicle:
    # __init__ method [Magic Method]
    def __init__(self,make: str, model: str,year:int) -> None:
        # adding __ before var name will make the variable private and won't be able to access from outside class - Encapsulation
        self.__make = make     
        self.__model = model 
        self.__year = year
    
        assert isinstance(self.__make, str) and self.__make, "Make must be a non-empty string"
        assert isinstance(self.__model, str) and self.__model, "Model must be a non-empty string"
        assert isinstance(self.__year, int) and self.__year >= 1995 and len(str(self.__year)) == 4, "Model must be a non-zero integer and only accepts vehicles from 1995"

    '''
    Adding exceptions for methods to catch assert statements
    Assert statements will help to validate the input data for these attributes and will raise the exception
    '''
    def get_make(self):
        try:
            return self.__make
        except AssertionError as e:
            raise AssertionError(f"Assertion Error {e}")
            
    def get_model(self):
        try:
            return self.__model
        except AssertionError as e:
            raise AssertionError(f"Assertion Error {e}")
        
    def get_year(self):
        try:
            return self.__year
        except AssertionError as e:
            raise AssertionError(f"Assertion Error {e}")
        
    
    def display(self):
        return f"{self.__year} {self.__make} {self.__model}"
