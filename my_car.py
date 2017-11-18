from car import Car
from electric import ElectricCar

my_new_car = Car('adui','A4','2016')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = ElectricCar('volkswagen','beetle',2016)
print(my_tesla.get_descriptive_name())
