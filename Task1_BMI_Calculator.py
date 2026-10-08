# Oasis Infobyte - Task 1 - BMI Calculator
# ID: OIB/O2/IP3914 - Shifa Shaikh

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 24.9:
    print("Category: Normal weight")
elif bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")