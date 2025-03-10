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
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


# my_tesla = ElectricCar("Tesla", "Model S", "85Kwh")
# print(my_tesla.fuel_type())


# safari = Car("Tata", "Safari")
# print(safari.fuel_type())

# safariThree = Car("Tata", "Nexon")

Car("Tata", "Safari")
Car("Tata", "Nexon")

# print(safari.total_car)
print(Car.total_car)







