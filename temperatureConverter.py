
import temperatureConverter

# Celsius = (F - 32)/ 1.8
# Fahrenheit = (1.8 * C) + 32 

# Celsius to Fahrenheit

tempCelsius = float(input("Enter temperature in CELSIUS: "))
fahrenheit = (1.8 * tempCelsius) + 32
print("The tempurature in Fahrenheit is: {:.2f} ".format(fahrenheit))


# Fahrenheit to Celsius

tempFahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (tempFahrenheit - 32) / 1.8
print("The temperature in Fahrenheit is: {:.2f}" .format(celsius))


