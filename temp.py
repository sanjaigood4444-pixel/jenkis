def convert_temperature():
    print("--- Temperature Unit Converter ---")
    try:
        temp = 23
        unit ="C"

        if unit == 'C':
            # Celsius to others
            f = (temp * 9/5) + 32
            k = temp + 273.15
            print(f"{temp}°C is {f:.2f}°F and {k:.2f}K")
            
        elif unit == 'F':
            # Fahrenheit to others
            c = (temp - 32) * 5/9
            k = c + 273.15
            print(f"{temp}°F is {c:.2f}°C and {k:.2f}K")
            
        elif unit == 'K':
            # Kelvin to others
            c = temp - 273.15
            f = (c * 9/5) + 32
            print(f"{temp}K is {c:.2f}°C and {f:.2f}°F")
            
        else:
            print("Invalid unit. Please enter C, F, or K.")
            
    except ValueError:
        print("Invalid input. Please enter a numerical value for temperature.")

# Run the program
convert_temperature()
