# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Input: Temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Conversion
fahrenheit = celsius_to_fahrenheit(celsius)

# Output: Temperature in Fahrenheit
print(f"{celsius}°C is equal to {fahrenheit}°F")

'''OUTPUT
Enter temperature in Celsius: 7
7.0°C is equal to 44.6°F '''
