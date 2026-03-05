# blood_sugar_safe.py
# Check Blood Sugar Level safely

while True:
    try:
        sugar = float(input("Enter blood sugar level (mg/dL): "))
        if sugar < 0:
            print("Please enter a valid sugar level.")
            continue
        if sugar < 70:
            status = "Low"
        elif sugar <= 140:
            status = "Normal"
        else:
            status = "High"
        print(f"Blood Sugar: {sugar} mg/dL ({status})")
        break
    except ValueError:
        print("Invalid input. Please enter a number for blood sugar.")

        
