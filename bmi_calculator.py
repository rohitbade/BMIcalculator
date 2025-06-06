# bmi_calculator.py

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in centimeter (cm): "))
        
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    except ValueError:
        print("❌ Please enter valid numbers for weight and height.")
