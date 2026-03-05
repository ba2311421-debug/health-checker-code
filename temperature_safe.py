# temperature_safe.py
# Check Body Temperature safely

while True:
    try:
        temperature = float(input("Enter body temperature in Celsius: "))
        if temperature > 37.5:
            print("Patient has a fever")
        else:
            print("Temperature is normal")
        break
    except ValueError:
        print("Invalid input. Please enter a number for temperature.")