import datetime
import random
import matplotlib.pyplot as plt
import numpy as np

# Experimental hour and power values (Watt) based on graphic
exp_hour = np.array([0, 4, 8, 10, 12, 14, 16, 18, 19, 20, 21, 23])
power_val = np.array([0, 0, 400, 1600, 2700, 3200, 3000, 2000, 1000, 200, 0, 0])

# Power curve graphic based on hours
plt.scatter(exp_hour, power_val)
plt.show()

# Find the current hour to find out the power generation at that time
now = datetime.datetime.now()
timestamp = now.strftime("On %A, %B %d, %Y at %H:%M o'clock")
hour = now.hour

# Random meter value - during the day (09:00 - 18:00) the energy consumption is supposed to be higher than night
if 9 <= hour <= 18:
    meter = random.randint(3000,9000)
else:
    meter = random.randint(0,2999)

# Interpolation of graphic, based on experimental hour and power values
current_power = np.interp(hour, exp_hour, power_val).astype(int)

if current_power > meter:
    sell = current_power - meter
    with open("simulator.txt", 'a') as f:
        f.write(f"{timestamp} your PV production is {current_power}W and consumption is {meter}W - you can sell {sell}W to the grid\n")
elif hour < meter:
    buy = meter - current_power
    with open("simulator.txt", 'a') as f:
        f.write(f"{timestamp} your PV production is {current_power}W and consumption is {meter}W - you need {buy}W energy from the grid\n")
else:
    with open("simulator.txt", 'a') as f:
        f.write(f"{timestamp} your PV production ({current_power}W) and consumption ({meter}W) are equal \n")