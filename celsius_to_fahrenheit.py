def celsius_to_fahrenheit(temp: float) -> float:
    fahrenheit = (temp * 9/5) + 32
    return fahrenheit
print(celsius_to_fahrenheit(0))    # 32.0
print(celsius_to_fahrenheit(100))  # 212.0
print(celsius_to_fahrenheit(-40)) # -40.0