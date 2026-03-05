# daily_calories_safe.py
# Calculate Estimated Daily Calories safely

while True:
    try:
        weight = float(input("Enter weight in kg: "))
        if weight <= 0:
            print("Please enter a valid weight greater than 0.")
            continue
        calories = weight * 24
        print("Estimated daily calories:", calories)
        break
    except ValueError:
        print("Invalid input. Please enter a number for weight.")