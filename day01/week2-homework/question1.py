def convert_temperature(celsius):
  fahrenheit = celsius * 9 / 5 + 32
  kelvin = celsius + 273.15
  print(f"Fahrenheit: {fahrenheit} Kelvin: {kelvin}")
  
celsius = 25
convert_temperature(celsius)