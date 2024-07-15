class Temperature:
    def __init__(self, value, unit='C'):
        self.value = value
        self.unit = unit

    def convert_to_fahrenheit(self):
        if self.unit == 'C':
            return (self.value * 9/5) + 32
        elif self.unit == 'F':
            return self.value

    def convert_to_celsius(self):
        if self.unit == 'F':
            return (self.value - 32) * 5/9
        elif self.unit == 'C':
            return self.value


# Example usage:
temp_celsius = Temperature(-44, 'C')
print(f"{temp_celsius.value}°C is {temp_celsius.convert_to_fahrenheit()}°F")

temp_fahrenheit = Temperature(-44, 'F')
print(f"{temp_fahrenheit.value}°F is {temp_fahrenheit.convert_to_celsius()}°C")
