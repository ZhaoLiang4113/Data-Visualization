from car import Car
from battery import Battery

class ElectricCar(Car):#指定父类的名称
    def __init__(self,make,model,year):
        super().__init__(make,model,year)#链接父类和子类，父类也称superclass
        self.battery = Battery()

    def describe_battery(self):#在子类中重写某个方法，将不再调用父类中的方法  
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
