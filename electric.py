from car import Car
from battery import Battery

class ElectricCar(Car):#ָ�����������
    def __init__(self,make,model,year):
        super().__init__(make,model,year)#���Ӹ�������࣬����Ҳ��superclass
        self.battery = Battery()

    def describe_battery(self):#����������дĳ�������������ٵ��ø����еķ���  
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
