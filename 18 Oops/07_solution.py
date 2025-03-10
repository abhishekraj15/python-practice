class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1


    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol Or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport."
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"
    

my_car = Car("Tata", "Safari")
Car("Tata", "Nexon")
print(my_car.general_description())

print(Car.general_description())



# static methond not working










