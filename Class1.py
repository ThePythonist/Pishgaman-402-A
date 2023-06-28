import time


class SedanCar:
    # Properties (Vizhegi Ha)
    def __init__(self, hp, color, fuel, gb):
        self.horsepower = hp
        self.color = color
        self.fuel = fuel
        self.gearbox = gb
        self.rpm = 0

    # Methods (Raftar Ha)
    def carbreak(self):
        print("Brrrrrreak")

    def carhorn(self):
        print("Boooooogh")

    def accelerate(self, value):
        for i in range(value):
            time.sleep(2)
            self.rpm += 1000
            print(f"Current round per motor is {self.rpm}")


samand = SedanCar(113, "white", "petrol", "manual")  # Creating instance ( Sakht shey )
dena = SedanCar(113, "black", "petrol", "automatic")  # Creating instance ( Sakht shey )
# samand.carhorn()
# dena.carhorn()
# print(samand.gearbox)
# print(dena.gearbox)
dena.accelerate(3)
