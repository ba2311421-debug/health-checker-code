# bmi_safe.py
# Calculate BMI safely

while True:
    try:
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (m): "))
        if weight <= 0 or height <= 0:
            print("Please enter positive numbers for weight and height.")
            continue
        bmi = round(weight / (height * height), 2)
        print("BMI is:", bmi)
        break
    except ValueError:
        print("Invalid input. Please enter numbers for weight and height.")