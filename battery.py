class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        else:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
            

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "KWh battery.")
