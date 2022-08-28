#!/bin/usr/python3

# Declared variables

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

# Formula

BMI1 = height ** 2
BMI = 22

# Conditions

if BMI > 35:
    print(f"Your BMI is {BMI}, you are clinically obese")
elif BMI > 30 < 35:
    print(f"Your BMI is {BMI}, you are obese")
elif BMI > 25 < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight")
elif BMI > 18.5 < 25:
    print(f"Your BMI is {BMI}, you have a normal weight")
else:
    print(f"Your BMI is {BMI}, you are underweight")
