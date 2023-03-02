"""
Temperature Converter: Create a Python program that asks the user for a temperature in Celsius and 
converts it to Fahrenheit using variables to store the values.
(0°C × 1.8) + 32 = 32°F
@author: user1
"""
from os import getcwd

def CelsiusToFahrenheit(Value):
    result = (Value * 1.8) + 32
    return result

celsius = float(input("Enter the temperature in Celsius: "))

fahrenheit = CelsiusToFahrenheit(celsius)

print("The %0.f degrees Celsius is equal to %0.1f degrees Fahrenheit" %(celsius,fahrenheit))
