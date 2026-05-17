class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel = 0

    def display_info(self):
        print(f"{self.brand}, {self.model}, {self.price}")
    
    # def start_engine(self):
    #     if self.fuel >= 10:
    #         self.fuel -= 10
    #         print(f"{self.brand} {self.mode} has started the engine and now has fuel {self.fuel}")
    #     else:
    #         print(f"{self.brand} {self.mode} has no fuel to start. Refill is with gas)


# car1 = Car("BMW", "Z4", 500000)
# car2 = Car("Toyota", "Corolla", 180000)
# car3 = Car("Kia", "Cerato", 165000)

# car1.display_info()
# car2.display_info()
# car3.display_info()

showroom = []
showroom.append(Car("Toyota", "Coralla", 25000))
showroom.append(Car("Honda", "Civic", 30000))
showroom.append(Car("Ford", "Focus", 22000))


for car in showroom:
    car.display_info()

