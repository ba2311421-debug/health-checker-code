# max_heart_rate_safe.py
# Calculate Maximum Heart Rate safely

while True:
    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            print("Please enter an age greater than 0.")
            continue
        max_heart_rate = 220 - age
        print("Maximum Heart Rate =", max_heart_rate)
        break
    except ValueError:
        print("Invalid input. Please enter a number for age.")