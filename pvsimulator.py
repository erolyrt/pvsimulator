import datetime
import random
import matplotlib.pyplot as plt
import numpy as np

''' Power curve graphic, based on hours
plt.scatter(exp_hour, power_val)
plt.show()'''

# Random meter value - during the day (09:00 - 18:00) the energy consumption is supposed to be higher than night
class Meter:

    def get_current_hour(self):
        # Find the current hour to find out the power generation at that time
        hour = datetime.datetime.now().hour
        return hour

    def home_consumption(self):
        hour = self.get_current_hour()
        if 9 <= hour <= 18:
            return random.randint(3000,9000)
        else:
            return random.randint(0,2999)

# Simulator to calculate energy comparison
class PVSimulator(Meter):
    def __init__(self, meter_value):
        self.meter_value = meter_value

    def get_current_power(self):
        # Experimental hour and power values (Watt) based on graphic
        exp_hour = np.array([0, 4, 8, 10, 12, 14, 16, 18, 19, 20, 21, 23])
        power_val = np.array([0, 0, 400, 1600, 2700, 3200, 3000, 2000, 1000, 200, 0, 0])
        # Used get_current_hour function from inherited Meter class
        hour = self.get_current_hour()
        # Interpolation of graphic, based on experimental hour and power values
        current_power = np.interp(hour, exp_hour, power_val).astype(int)
        return current_power

    def calculation(self):
        timestamp = datetime.datetime.now().strftime("On %A, %B %d, %Y at %H:%M o'clock")
        current_power = self.get_current_power()
        if current_power > self.meter_value:
            sell = current_power - self.meter_value
            self.write_to_file(f"{timestamp} your PV production is {current_power}W and consumption is {self.meter_value}W - you can sell {sell}W to the grid\n")
            return sell
        elif current_power < self.meter_value:
            buy = self.meter_value - current_power
            self.write_to_file(f"{timestamp} your PV production is {current_power}W and consumption is {self.meter_value}W - you need {buy}W energy from the grid\n")
            return buy
        else:
            self.write_to_file(f"{timestamp} your PV production ({current_power}W) and consumption ({self.meter_value}W) are equal\n")
            return None

    def write_to_file(self, data):
        with open("simulator.txt", 'a') as f:
            f.write(data)

if __name__ == '__main__':
    meter = Meter().home_consumption()
    PVSimulator(meter).calculation()
