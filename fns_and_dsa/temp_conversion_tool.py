# temp_conversion_tool.py

# === Global Conversion Factors ===
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


# === Conversion Functions ===
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# === User Interaction ===
def main():
    temp_input = input("Enter the temperature you want to convert: ")

    # Validate temperature input
    try:
        temp_value = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

    if unit == "c":
        result = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is equal to {result:.2f}°F")
    elif unit == "f":
        result = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is equal to {result:.2f}°C")
    else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
        

if __name__ == "__main__":
    main()
