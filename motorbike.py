from vehicle import Vehicle

class Motorbike(Vehicle):
    def __init__(self, model, make, year, has_autoclutch) -> None:
        super().__init__(model, make, year)
        self.__autoclutch = has_autoclutch

    def get_gear_no(self):
        return self.__autoclutch
    
    def set_gear_no(self,autoclutch):
        self.__autoclutch = autoclutch

    def display(self):
        autoclutch_status= "Yes" if self.__autoclutch else "No"
        return f"{super().display()}, Autoclutch status: {autoclutch_status}"