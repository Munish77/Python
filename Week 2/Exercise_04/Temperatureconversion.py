degrees_Kelvin = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
degrees_Celsius = [(temperature - 273.15) for temperature in degrees_Kelvin]
degrees_Fahrenheit = [((temperature - 273.15) * 9/5 + 32) for temperature in degrees_Kelvin]
print(f"degrees Celsius = {degrees_Celsius}")
print(f"degrees Fahrenheit = {degrees_Fahrenheit}")
