import matplotlib as wf
import numpy as nu
import random

##print(random.choice(weather))
##for i in range(30):

temps = 28
forecast_duration = 30
 
days = 0
weather = ["Sunny", "Cloudy", "Rainy", "Stormy"]

for day in range(1, 31):
    randomly choose weather
    if cloudy:
        change = random(-1, 1)
        if else sunny:
            change = random(1, 3)
        if else rainy:
            change = random(-3, -1)
        if else stormy:
            change = random(-5, -3)

        temperature = temps + change
        print("Day", day, ":", weather, "Temperature:", temperature, "°C")
